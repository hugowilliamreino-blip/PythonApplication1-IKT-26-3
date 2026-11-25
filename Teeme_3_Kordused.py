while True:
    print("Vali tsükkel (1-3):")
    print("1. For-tsükkel")
    print("2. While-tsükkel tingimusega")
    print("3. While-tsükkel lõpmatu")
    print("0. Välju")
    valik= input("Sisesta valik: ")
    if valik=="1":
        print("For-tsükkel")
        for i in range(5):
            print(f"Tsükli kord: {i+1}")
    elif valik=="2":
        print("While-tsükkel tingimusega")
        i=0
        while i<5:
            print(f"Tsükli kord: {i+1}")
            i+=1
    elif valik=="3":
        print("While-tsükkel lõpmatu")
        i=0
        while True:
            print(f"Tsükli kord: {i+1}")
            i+=1
            if i>=5: break
    elif valik=="0":
        print("Väljun programmist.")
        break
    else:
        print("Vale valik, proovi uuesti.")
