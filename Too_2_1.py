# 1 Juku kinno
# Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.
# Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.

eesnimi = input("Sisesta eesnimi: ")
if eesnimi.lower()=="juku":
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    # Kui Juku läheb kinno, küsi tema vanus ja otsusta, millist piletit on vaja osta:
    vanus=int(input("Sisesta Juku vanus: "))
    if 0<vanus<=6:
        pilet="tasuta pilet"
    elif 4<vanus<=14:
        pilet="lastepilet"
    elif 14<vanus<=65:
        pilet="täispilet"
    elif 65<vanus<=100:
        pilet="sooduspilet"
    else:
        pilet="tundmatu pilet"
    print("Juku vajab", pilet)
else:
    print("Täna kinno ei minda.")

# 2 Pinginaabrid
# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest.
# Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. 
# Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.
# Kasuta: isalpha(), capitalize()

pinginaabrid=["Mati", "Kati"] #list, kus on pinginaabrite nimed
nimi1=input("Sisesta esimese inimese nimi: ")
nimi2=input("Sisesta teise inimese nimi: ")
print(f"Tere {nimi1.capitalize()} ja {nimi2.capitalize()}!")

if nimi1.isalpha() and nimi2.isalpha():
    if nimi1 in pinginaabrid and nimi2 in pinginaabrid:
        print("Te olete täna pinginaabrid.")
    else:
        print("Te ei ole täna pinginaabrid.")
else:
    print("Palun sisesta kehtivad nimed.")

# 3 Remont
# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? 
# Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()

pikkus=float(input("Sisesta toa pikkus meetrites: "))
laius=float(input("Sisesta toa laius meetrites: "))
pindala=pikkus*laius
print(f"Toa põranda pindala on {round(pindala, 2)} ruutmeetrit.")
remont=input("Kas soovid remonti teha? (jah/ei): ").lower()
if remont=="jah":
    print("Teema remonti!")
    try:
        rm_hind=float(input("Sisesta ruutmeetri hind: "))
        remondi_hind=pindala*rm_hind
        ise=input("Kas teed remondi ise? (jah/ei): ").lower()
        if ise=="jah":
            print(f"Remondi koguhind on {round(remondi_hind, 2)} eurot.")
        else:
            try:
                töö_hind=hind(input("Sisesta töö hind ruutmeetri kohta: "))
                koguhind=remondi_hind+(pindala*töö_hind)
                print(f"Remondi koguhind koos tööga on {round(koguhind, 2)} eurot.")
            except ValueError:
                print("Palun sisesta kehtiv number töö hinna jaoks.")
    except ValueError:
        print("Palun sisesta kehtiv number: ")
else:
    print("Remonti ei tehta.")

# 4 Allahindlus
# Küsi toote alghind. Kui alghind on üle 700 euro, arvuta hind 30% soodustusega. 
# Muul juhul jääb hind samaks. Kuva lõplik hind kahe komakohaga.

try:
    alghind=float(input("Sisesta toote alghind eurodes: "))
    if alghind>700:
        lõpphind=alghind*0.7
    else:
        lõpphind=alghind
    print(f"Lõplik hind on {round(lõpphind, 2)} eurot.")
except:
    print("Palun sisesta kehtiv number alghinna jaoks.")
