# preço da montanha russa

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("Você pode andar na montanha russa.")
  idade = int(input("Qual é a sua idade? "))
  if idade < 12:
    conta = 5
    print("O preço a pagar é R$5.00")
  elif idade <= 18:
    conta = 7
    print("O preço a pagar é R$7.00.")
  elif idade >= 45 and idade <= 55:
    print("O valor é por nossa conta.")
  else:
    conta = 12
    print("O preço a pagar é R$12.00")
  foto = input("Você quer tirar foto? sim ou não? ")
  if foto == "sim":
    conta += 3
  print(f"O valor final será R${conta}")
      
else:
    print("Você precisa ser mais alto para andar na montanha russa.")
