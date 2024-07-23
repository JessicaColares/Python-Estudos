import sys

# Mapeamento de instruções e registradores
instrucoes = {
    'add': 0x80, 'shr': 0x90, 'shl': 0xA0, 'not': 0xB0, 'and': 0xC0, 'or': 0xD0, 'xor': 0xE0, 
    'cmp': 0xF0, 'ld': 0x00, 'st': 0x10, 'data': 0x20, 'jmpr': 0x30, 'jmp': 0x40, 'clf': 0x60,
    'jc': 0x58, 'ja': 0x54, 'je': 0x52, 'jz': 0x50, 'jca': 0x5C, 'jce': 0x5A, 'jcz': 0x59, 'jae': 0x56,
    'jaz': 0x55, 'jez': 0x53, 'jcae': 0x5E, 'jcaz': 0x5D, 'jcez': 0x5B, 'jaez': 0x57, 'jcaez': 0x5F,
    'in data': 0x70, 'in addr': 0x74, 'out data': 0x78, 'out addr': 0x7C, 'halt': 0xFF, 'swap': 0x60
}

registradores = {'r0': 0x00, 'r1': 0x01, 'r2': 0x02, 'r3': 0x03}

# Escrever o arquivo de saída
def output_file(memory, file):
    assert len(memory) <= 256
    header = 'v3.0 hex words addressed\n'
    with open(file, 'w') as f:
        f.write(header)
        for i, byte in enumerate(memory):
            f.write(f'{i:02x}: {byte}\n')

# Ler o arquivo em assembly
def read_assembly(input_file_name):
    try:
        with open(input_file_name, 'r') as file:
            lines = file.readlines()
            code = []
            for line in lines:
                line = line.strip().lower()
                if line and not line.startswith(';'):  # Ignorar linhas em branco e comentários
                    code.append(line)
            return code
    except FileNotFoundError:
        print(f'Erro: O arquivo {input_file_name} não foi encontrado.')
        sys.exit(1)

# Traduz a instrução para código de máquina em hexadecimal
def traduzir_instrucao(instrucao):
    parts = instrucao.replace(',', ' ').split()
    nominal = parts[0].lower()  # Aqui ajuda a ler comandos tanto em maiúsculo como minúsculo
    
    # Tradução da instrução: data
    if nominal == 'data': 
        if len(parts) < 3:
            raise ValueError(f'Instrução {instrucao} inválida, faltam argumentos.')
        reg = parts[1].lower()
        value = parts[2]
        if reg in registradores:
            reg_code = registradores[reg]
            if value.startswith('0x'):
                return f'{instrucoes[nominal] + reg_code:02x} {int(value, 16):02x}'
            elif value.startswith('0b'):
                return f'{instrucoes[nominal] + reg_code:02x} {int(value, 2):02x}'
            else:
                return f'{instrucoes[nominal] + reg_code:02x} {int(value):02x}'
        else:
            raise ValueError(f'Registrador inválido: {reg}')
        
    # Tradução das instruções: add, ld, st, swap, shr, shl, and, or, xor, cmp e not
    elif nominal in ['add', 'ld', 'st', 'swap', 'shr', 'shl', 'and', 'or', 'xor', 'cmp', 'not']:
        if len(parts) < 3:
            raise ValueError(f'Instrução {instrucao} inválida, faltam argumentos.')
        reg1 = parts[1].lower()
        reg2 = parts[2].lower()
        if reg1 in registradores and reg2 in registradores:
            reg1_code = registradores[reg1]
            reg2_code = registradores[reg2]
            base_instrucao = instrucoes[nominal]
            # Montar o código da máquina, preservando a base da instrução e combinando os códigos dos registradores
            combined_code = (reg1_code << 2) + reg2_code  # Corrigir a combinação dos registradores
            return f'{base_instrucao + combined_code:02x}'
        else:
            raise ValueError(f'Registradores inválidos: {reg1}, {reg2}')
        
    # Tradução das instruções: jmp, ja, jc, je, jz, jca, jce, jcz, jae, jaz, jez, jcae, jcaz, jcez, jaez, jcaez
    elif nominal in ['jmp', 'ja', 'jc', 'je', 'jz', 'jca', 'jce', 'jcz', 'jae',
                     'jaz', 'jez', 'jcae', 'jcaz', 'jcez', 'jaez', 'jcaez']:
        if len(parts) < 2:
            raise ValueError(f'Instrução {instrucao} inválida, faltam argumentos.')
        address = parts[1].lower()
        if address.startswith('0x'):
            address_value = int(address, 16)
        elif address.startswith('0b'):
            address_value = int(address, 2)
        else:
            address_value = int(address)
        return f'{instrucoes[nominal]:02x} {address_value:02x}'
    
    # Tradução das instruções: clf e halt
    elif nominal in ['clf', 'halt']:
        return f'{instrucoes[nominal]:02x}'
    
    # Tradução das instruções in data, in addr, out data, out addr
    elif nominal in ['in', 'out']:
        if len(parts) < 3:
            raise ValueError(f'Instrução {instrucao} inválida, faltam argumentos.')
        io_type = parts[1]
        reg = parts[2].lower()
        full_nominal = f'{nominal} {io_type}'
        if full_nominal in instrucoes and reg in registradores:
            reg_code = registradores[reg]
            return f'{instrucoes[full_nominal] + reg_code:02x}'
        else:
            raise ValueError(f'Instrução ou registrador inválido: {full_nominal}, {reg}')

    # Tradução da instrução jmpr
    elif nominal == 'jmpr':
        if len(parts) < 2:
            raise ValueError(f'Instrução {instrucao} inválida, faltam argumentos.')
        reg = parts[1].lower()
        if reg in registradores:
            reg_code = registradores[reg]
            return f'{instrucoes[nominal] + reg_code:02x}'
        else:
            raise ValueError(f'Registrador inválido: {reg}')
    
    else:
        raise ValueError(f'Instrução desconhecida: {instrucao}')

# Função para montar o programa
def assembler(input_file_name, output_file_name):
    memory = ['00' for _ in range(256)]
    code = read_assembly(input_file_name)
    address = 0
    for instrucao in code:
        machine_code = traduzir_instrucao(instrucao)
        machine_code_parts = machine_code.split()
        for part in machine_code_parts:
            memory[address] = part
            address += 1
    output_file(memory, output_file_name)

# Verificação dos argumentos de linha de comando
if len(sys.argv) != 3:
    print(f'Uso: python {sys.argv[0]} <arquivo_entrada.asm> <arquivo_saida.m>')
    sys.exit(1)

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

assembler(input_file_name, output_file_name)
