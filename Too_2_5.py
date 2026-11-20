# Kood:

print("Ruutvõrrandi lahendamine") # Jutumärgid olid erinevad.
a=float(input("Sisesta a => "))
b=float(input("Sisesta b => ")) # Lõppust oli sulg puudu.
c=float(input("Sisesta c => ")) # Float oli puudu.
D=b*b-4*a*c
if D>0: # Koolon oli puudu.
    x1=(-b+D**0.5)/(2*a) # 2*a ümbert olid sulud puudu.
    x2=(-b-D**0.5)/(2*a)
    print("Kaks lahendit:", x1, x2)
elif D==0: # elif mitte esle if ja == mitte =.
    x=-b/(2*a)
    print("Üks lahend:", x)
else:
    print("Reaalarvulised lahendid puuduvad")
print()
print("Palga arvutamine")
tunnid=float(input("Sisesta töötunnid nädalas => "))
tunnitasu=float(input("Sisesta tunnitasu (€) => "))
if tunnid<0 and tunnid>168:
    print("Vigane tundide arv")
elif tunnid<=40:
    palk=tunnid*tunnitasu
    print("Nädalapalk:", palk, "€")
else:
    palk=40*tunnitasu+(tunnid-40)*tunnitasu*1.5 # 1 ja 5 vahel peab olema punkt mitte koma.
    print("Nädalapalk koos ületundidega:", palk, "€")
print()
try:
    print("Parkimise hind")
    tunnid=int(input("Sisesta parkimise aeg tundides => "))
    if tunnid<=0: # Võrdusmärk oli valel pool.
        print("Vigane aeg")
    elif tunnid>=3:
        print("Hind: 5 €")
    elif tunnid>=8:
        print("Hind: 10 € (päevapilet)")
    else: # Koolon oli puudu.
        print("Hind: 2 €") # Sulg oli lõpust puudu.
except:
    print("Viga!")