import OOP

lista = []

def beolvas():
    beFajl = open("balkezesek.txt", "r", encoding="utf-8")
    beFajl.readline()
    tomb = beFajl.readlines()
    i = 0
    while i < len(tomb):
        tisztitott = tomb[i].strip()
        adatok = OOP.Balkezesek(tisztitott)
        lista.append(adatok)
        i += 1
def jatekosSzam():
    print("III/A,B")
    print(f"\tA balkezes játékosok száma: {len(lista)}")

def atalgSuly():
    i = 0
    osszeg = 0
    db = len(lista)
    while i < len(lista):
        osszeg += lista[i].suly
        i += 1

    print("III/C:")
    tizedes = 2
    print("\tA versenyzők átlag súlyértéke: {0:.2f} font".format(osszeg/db))

def legmagasabb():
    print("III/D")
    i = 0
    max = 0
    while i < len(lista):
        if lista[i].magassag > lista[max].magassag:
            max = i
        i += 1
    print(f"\tA legmagasabb játékos: {lista[max].nev},{round(lista[max].magassag * 2.54)} cm")

beolvas()
jatekosSzam()
atalgSuly()
legmagasabb()
