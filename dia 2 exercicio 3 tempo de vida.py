# Quanto tempo de vida ainda resta

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

anos = 90 - age_int
dias = anos * 365
semanas = anos * 52
meses = anos * 12

print(f"You have {dias} days, {semanas} weeks, and {meses} months left.")
