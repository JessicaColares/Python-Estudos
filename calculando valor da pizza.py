# Calculando o valor da conta da pizza

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
  conta = 15
  if add_pepperoni == "Y":
    conta +=2
  if extra_cheese == "Y":
    conta += 1
  print(f"Your final bill is: ${conta}.")
elif size == "M":
  conta = 20
  if add_pepperoni == "Y":
    conta +=3
  if extra_cheese == "Y":
    conta += 1
  print(f"Your final bill is: ${conta}.")
elif size == "L":
  conta = 25
  if add_pepperoni == "Y":
    conta +=3
  if extra_cheese == "Y":
    conta += 1
  print(f"Your final bill is: ${conta}.")
