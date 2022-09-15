# Calculando a gorjeta

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Bem vindo(a) a calculadora de gorjeta!")

conta = float(input("Qual o total da sua conta?: R$"))
gorjeta = int(input("Quanto de gorjeta gostaria de dar em porcentagem? 10, 12, ou 15? "))
pessoas = int(input("Quantas pessoas vão dividir a conta? "))


a = (gorjeta / 100) * conta


total = (a + conta) / pessoas

totalfinal = round(total, 2)

print((f"O A quantia paga por cada um será R${totalfinal}."))
