print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro.")
print("Sua missão é encontrar o tesouro.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("Antes de começar a caçada ao tesouro, responda uma pergunta simples.")
nome = input("Qual é o seu nome? \n")

print(f"{nome}, você está numa ilha, tudo o que sabe é que existe um tesouro numa caverna ao norte desta ilha. Você como bom pirata, não vai negar um bom tesouro e procura a caverna. Você encontra a caverna e entra nela.")

escolha1 = input("Logo no começo da caverna existem dois caminhos para seguir, deseja ir para a direita ou para a esquerda? Digite direita ou esquerda: \n").lower()
if escolha1 == "esquerda":
    escolha2 = input("Você encontra um belo lago, azul claro iluminado por uma fenda na caverna. \n Você se sente um pouco cansado ou cansada por ter caminhado pela ilha, gostaria de dar uma pausa para descansar ou quer nadar no lago azul? Digite pausa ou nadar: \n").lower()    
    if escolha2 == "pausa":
        escolha3 = input("Você decide sentar um pouco para repor as energias, de longe vem surgindo um espírito de um barqueiro com sua gôndola, ele atraca na margem do lago azul e te dá uma carona até o outro lado do lago.\nDepois de caminhar um pouco você encontra 3 portas, cada uma com cores diferentes. Uma porta na cor vermelho, uma amarelo e uma azul, qual das portas você deseja entrar? Digite vermelho, amarelo ou azul: \n").lower()          
        if escolha3 == "vermelho":
            print(f"{nome}, assim que você pisa dentro da sala uma armadilha é acionada e toda a sala é envolvida pelas chamas, você morreu!")
        elif escolha3 == "azul":
            print(f"{nome}, você entra numa sala, você vê pequenos pontos na escuridão, conforme se aproximam você persebe que são olhos. São olhos de esqueletos, eles avançam para cima de você e te acertam com suas espadas, você morreu!")
        elif escolha3 == "amarelo":
            print(f"{nome}, você entra numa sala escura, mas conforme anda tochas se acendem. Estátuas de mármore adormam o lugar, no final da sala você encontrou o tesouro! E atrás da parede do tesouro tem uma passagem secreta que te leva para fora da caverna.")
        else:
            print(f"{nome}, você escolheu uma porta que não existe, você foi picado por uma cobra e morreu!")
    else:
        print(f"{nome}, decide nadar no belo lago azul, mas aparece uma tilápia gigante! A tilápia gigante comeu você, você morreu! ")
else:
  print(f"{nome} caiu num buraco, você morreu!")

input("\nChegamos ao fim, aperte qualquer botão para sair :)")
