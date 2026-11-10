from datetime import *
import calendar
from math import *
# Kirjuta programm, mis sind tervitab ja kuvab ekraanile tänane kuupäev moduli datetime kasutades ja date.today() funktsiooni abil.

tana=date.today()
print(f"Täna on {tana}")
# Kasuta erinevate formaatide kuvamiseks ekraanile järgmised funktsioonid:

# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(tana1)
# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(tana2)
# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(tana3)
# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(tana4)
# Omadused day, month, year kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.

kuulõpuni=calendar.monthrange(tana.year, tana.month)[1]-tana.day
# tana=10.11.2026
# calendar.monthrange(2026,11)[1]-10
aasta_lopuni = (date(tana.year, 12,31) - tana).days #(31.12.2026 - 10.11.2026).days-> 51

print(f"Jäänud päevad kuu lõpuni: {kuulõpuni}")
print(f"Jäänud pävad aasta lõpuni: {aasta_lopuni}")

#Arvuta oma vanus aastates, kuudes ja päevades.

# Üleasanne 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.
print("Tehe 3 +8 / (4 - 2) * 4 = ",3 + 8 / (4 - 2) * 4)

# Ülesanne 3
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.
R=float(input("Sisesta ringi raadius =>"))
print("Ringi pindala:", round(pi*R**2,2)) #round() funktsioon ümardab arvu 2 kohta pärast koma.
print("Ringi ümbermõõt:", round(2*pi*R,2))
print("Ringi pindala:", round((2*R)**2,2))
print("Ringi ümbermõõt:", round(4*2*R,2))
