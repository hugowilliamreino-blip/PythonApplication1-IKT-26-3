try:    
    x=int(input("Sisesta arv: "))
    if x>0:
        print("Arv on negatiivne")
    elif x<0:
        print("Arv on negatiivne")
    else:
        print("Arv on null")
except ValueError:
    print("Sisestatud väärtus ei ole täisarv")

# Hinne
try:    
    hinne=int(input("Sisesta arv: "))
    if hinne==5:
        print("Hinne on väga hea")
    elif hinne==4:
        print("Hinne on hea")
    elif hinne==3:
        print("Hinne on rahuldav")
    elif hinne>=1 and hinne<3:
        print("Hinne on puudulik")
    else:
        print("Sisestatud hinne ei ole kehtiv")
except ValueError:
    print("Sisestatud väärtus ei ole täisarv")

# Summa
try:
    summa=float(input("Sisesta summa"))
    if summa>2000:
        hind=summa*0.8
    elif summa>1000:
        hind=summa*0.9
    else:
        hind=summa
except ValueError:
    print("Sisestatud väärtus ei ole arv")

vanus = int(input("Vanus: "))
if vanus >= 18:
    juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
    if juhiluba.lower() == "jah":
        print("Võid autot juhtida.")
    else:
        print("Kõigepealt tee juhiload.")
else:
    print("Oled autojuhtimiseks liiga noor.")

# isalpha(), isupper(), istitle() funktsioonide kasutamine
nimi = input("Sisesta nimi: ")
print("Ainult tähed:", nimi.isalpha())
print("Suurtähtedega:", nimi.isupper())
print("Algab suurtähega:", nimi.istitle())
if nimi.isalpha():
    print("Nimi sobib.")
else:
    print("Nimes tohib olla ainult tähti!")

# Kirjutage ise isdigit(), isalnum(), islower() funktsioonide kasutamine

if nimi.isdigit():
    print("Nimi sisaldab ainult numbreid.")