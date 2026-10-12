import math
print(dir(math))
print(math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))
print("Tere tulemast!")
# print("See on IKT-26-3 programm.",end="")
# print("Mul on", 3, "kassi",end="-")
# print("Aasta on", 2026,end="\n")
# print("2026", "10", "01", sep="/")
nimi = "Mari"
vanus = 17
print(nimi, "on", vanus, "aastat vana")
vanus = vanus + 1
print(vanus)
vanus += 1
print(vanus)
KAIBEMAKS = 0.24
hind = 100
print("Hind koos käibemaksuga:", hind * (1 + KAIBEMAKS))

# nimi=input("Sisesta oma nimi: ")
# vanus=int(input("Sisesta oma vanus: ")) #str->int
# print(nimi, "on", vanus, "aastat vana")

a = input("Esimene arv: ")
b = input("Teine arv: ")
print(a + b)

a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a + b)

a = float(input("Esimene arv: ")) # str->float 2.5
b = float(input("Teine arv: "))
print(a + b)
print(a ** b) # 2.5 ** 3.0 astendamine
print( a * b)
print(a / b)
print(a // b)
print(a % b)
print(a - b)
