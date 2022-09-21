# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
CombinarNomes = name1 + name2

LetraMinuscula = CombinarNomes.lower()

t = LetraMinuscula.count("t")
r = LetraMinuscula.count("r")
u = LetraMinuscula.count("u")
e = LetraMinuscula.count("e")

true = t + r + u + e

l = LetraMinuscula.count("l")
o = LetraMinuscula.count("o")
v = LetraMinuscula.count("v")
e = LetraMinuscula.count("e")

love = l + o + v + e

PontosLove = int(str(true) + str(love))

print(PontosLove)

if PontosLove < 10 or PontosLove >90:
  print(f"Sua pontuação no amor é {PontosLove}, seu romance é tão bom quanto coca cola e mentos juntos >:(")
if (PontosLove >= 40) and (PontosLove <= 50):
  print(f"Sua pontuação no amor é {PontosLove}, seu romance é carne unha, alma gêmea, bate o coração")
else:
  print(f"Sua pontuação no amor é {PontosLove}, tudo ok")
