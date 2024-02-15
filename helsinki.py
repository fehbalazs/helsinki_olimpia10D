def beolvas():
    tomb = []
    nevek = {}
    forras = open("helsinki.txt", "r")
    for sor in forras:
        sor = sor.strip().split()
        sor[0] = int(sor[0])
        sor[1] = int(sor[1])
        nevek ={"Helyezes":sor[0],
                 "Sportolok_szama":sor[1],
                 "Sportag":sor[2],
                 "Verseny_szam":sor[3],   
        }
        tomb.append(nevek)
        nevek ={}
    forras.close()
    return tomb

def pontszerhely(tomb):
    szamolas = 0
    for i in range(len(tomb)):
        szamolas +=1
    return szamolas

def arany(tomb):
    szamlalas = 0
    for i in range(len(tomb)):
        if tomb[i]["Helyezes"] == 1:
            szamlalas += 1
    return szamlalas

def ezust(tomb):
    ezustsz = 0
    for i in range(len(tomb)):
        if tomb[i]["Helyezes"] == 2:
            ezustsz += 1 
    return ezustsz

def bronz(tomb):
    bronzszam = 0
    for i in range(len(tomb)):
        if tomb[i]["Helyezes"] == 3:
            bronzszam += 1
    return bronzszam

def pontszam(tomb):
    pont = 0
    for i in range(len(tomb)):
        if tomb[i]["Helyezes"] == 1:
            pont += 7
        if  tomb[i]["Helyezes"] == 2:
            pont += 5
        if tomb[i]["Helyezes"] == 3:
            pont += 4
        if tomb[i]["Helyezes"] == 4:
            pont += 3
        if tomb[i]["Helyezes"] == 5:
            pont += 2
        if tomb[i]["Helyezes"] == 6:
            pont += 1
    return pont

def talaj(tomb):
    torna = 0
    for i in range(len(tomb)):
        if tomb[i]["Sportag"] == "torna":
            if tomb[i]["Helyezes"] == 1 or tomb[i]["Helyezes"] == 2 or tomb[i]["Helyezes"] == 3:
                torna += 1
    return torna

def uszas(tomb):
    uszas = 0
    for i in range(len(tomb)):
        if tomb[i]["Sportag"] == "uszas":
            if tomb[i]["Helyezes"] == 1 or tomb[i]["Helyezes"] == 2 or tomb[i]["Helyezes"] == 3:
                uszas = 1
    return uszas

def melyiktobb(uszas,torna):
    if uszas> torna:
        print("Uszas sportagban szeretek tobb érmet")
    if uszas<torna:
        print("Torna sportágban szeretek több érmet")
    else:
        print("Egyenlő az érmek száma")

def maxember(tomb):
    maxsportolok = 0
    for i in range(len(tomb)):
        if tomb[i]["Sportolok_szama"] > maxsportolok:
            maxsportolok = tomb[i]["Sportolok_szama"]
    for i in range(len(tomb)):
        if tomb[i]["Sportolok_szama"] == maxsportolok:
            print("Helyezés",tomb[i]["Helyezes"])
            print("Sportág:",tomb[i]["Sportag"])
            print("Veseny szám:",tomb[i]["Verseny_szam"])
            print("Sportolók száma",tomb[i]["Sportolok_szama"])

#main
helyezesek = beolvas()
print(helyezesek)


print("3.feladat:")
pontszerzohelyek = pontszerhely(helyezesek)
print("Pontszerző helyek száma:",pontszerzohelyek)


print("4.feladat:")
aranyerem = arany(helyezesek)
print("Arany:", aranyerem)
ezusterem = ezust(helyezesek)
print("Ezüst:", ezusterem)
bronzerem = bronz(helyezesek)
print("Bronz:", bronz(helyezesek))
osszes = arany(helyezesek) + ezust(helyezesek) + bronz(helyezesek)
print("Összes:",osszes)


print("5.feladat:")
pontszamok = pontszam(helyezesek)
print("Olimpiai pontok száma:", pontszamok)


print("6.feladat:")
sportag = melyiktobb(uszas(helyezesek),talaj(helyezesek))


print("7.feladat")
maxemberr = maxember(helyezesek)