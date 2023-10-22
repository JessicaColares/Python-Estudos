import sys

def paraHex(valor):
    return hex((valor + (1 << 8)) % (1 << 8))

def main():
    if len(sys.argv) != 3:
        print("Uso: montador.py <arquivoSaida.mem> <arquivoEntrada.asm>")
        return

    nomeSaida = sys.argv[1]
    nomeEntrada = sys.argv[2]

    mapearInstrucao = {
        "add": 0x80,
        "shr": 0x90,
        "shl": 0xA0,
        "not": 0xB0,
        "and": 0xC0,
        "or": 0xD0,
        "xor": 0xE0,
        "cmp": 0xF0,
        "ld": 0x00,
        "st": 0x10,
        "in": 0x70,
        "out": 0x78,
        "data": 0x20,
        "jmpr": 0x30,
        "jmp": 0x40,
        "clf": 0x60,
        "jc": 0x58,
        "ja": 0x54,
        "je": 0x52,
        "jz": 0x50,
        "jca": 0x5C,
        "jce": 0x5A,
        "jcz": 0x59,
        "jae": 0x56,
        "jaz": 0x55,
        "jez": 0x53,
        "jcae": 0x5E,
        "jcaz": 0x5D,
        "jcez": 0x5B,
        "jaez": 0x57,
        "jcaez": 0x5F,
        "halt": 0x70,
        "word": 0x00,
        "move": 0xF8,
    }

    with open(nomeEntrada, 'r') as arquivoEntrada:
        linhas = arquivoEntrada.readlines()

    code = []
    dataSection = False

    for linhaAsm in linhas:
        linhaAsm = linhaAsm.strip().lower()

        if not linhaAsm:
            continue

        if linhaAsm.startswith('.code'):
            dataSection = False
            continue
        elif linhaAsm.startswith('.data'):
            dataSection = True
            continue

        if dataSection:
            if linhaAsm.startswith('word'):
                valor = linhaAsm.split()[1].strip()
                try:
                    code.append(hex(int(valor, 0)))
                except ValueError:
                    code.append(valor)
        else:
            commentIndex = linhaAsm.find(';')
            if commentIndex != -1:
                linhaAsm = linhaAsm[:commentIndex]

            tokens = linhaAsm.split()
            instrucao = tokens[0]
            operandos = tokens[1:]

            if instrucao in mapearInstrucao:
                linhaHex = mapearInstrucao[instrucao]

                for operando in operandos:
                    if operando == "r1":
                        linhaHex += 0x04
                    elif operando == "r2":
                        linhaHex += 0x08
                    elif operando == "r3":
                        linhaHex += 0x0C
                    elif operando.startswith("R"):
                        regNum = int(operando[1])
                        linhaHex += regNum
                    else:
                        pass

                code.append(hex(linhaHex))

    with open(nomeSaida, 'w') as arquivoSaida:
        arquivoSaida.write("v3.0 hex words plain\n")
        for i in range(16):
            for j in range(16):
                if len(code) > (i * 16) + j:
                    arquivoSaida.write('{:02x}'.format(int(code[(i * 16) + j], 16)) + " ")
                else:
                    arquivoSaida.write("00 ")
            arquivoSaida.write("\n")

if __name__ == "__main__":
    main()
