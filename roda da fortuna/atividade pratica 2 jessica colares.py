# Atividade Prática 2

# Jessica de Figueredo Colares
# Numero de matrícula: 22060036

# Roda da fortuna

import random

print("Regras da Roda da Fortuna!\nDigite X para para rodar a Roda da Fortuna, caso não goste do resultado você poderá rodar mais 3 vezes.\n Fortuna ou Infortúnio! O que será?: \n")

sua_sorte = input()

(random.randrange(-8, 8))
x = random.randrange(-8, 8)


lista = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
lista_resultado = ['infortunio', 'infortunio', 'infortunio', 'infortunio', 'infortunio', 'infortunio', 'infortunio', 'infortunio', 'fortuna', 'fortuna', 'fortuna', 'fortuna', 'fortuna', 'fortuna', 'fortuna', 'fortuna']

for contador in range(len(lista)):
    if lista[contador] == x:
        print('\nResultado da roleta:\n' + lista_resultado[contador])

continuar_jogando = True
tentativa = 0

while continuar_jogando & (tentativa < 3):
    print('\nDeseja continuar jogando? Aperte S para continuar ou aperte D para desistir:'
          '\n você tem tentativas restantes:', tentativa+1,'/3\n')
    sua_sorte = input()
    if sua_sorte == 's' or sua_sorte == 'S':
        tentativa = tentativa+1
        x = random.randrange(-8, 8)
        for contador in range(len(lista)):
            if lista[contador] == x:
                print('Resultado da roleta:\n' + lista_resultado[contador])
    elif sua_sorte == 'd' or sua_sorte == 'D':
        continuar_jogando = False
    else:
        print('digite uma resposta válida')
