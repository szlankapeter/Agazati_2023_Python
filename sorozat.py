import random

print("II/A,B,C")
i = 0
lista = []
while i < 9:
    rnd = random.randint(10, 350)
    print(rnd, end="#")
    lista.append(rnd)
    i += 1

rnd = random.randint(10, 350)
lista.append(rnd)
print(rnd)

def parosok():
    i = 0
    parosDb = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            parosDb += 1
        i += 1
    return parosDb

print("II/D,E")
def konzol_kiir():
    parosDb = parosok()
    print(f"\tA párosok száma: {parosDb}")
konzol_kiir()

def file_kiir():
    parosDb = parosok()
    kiFajl = open("kimutatas.txt", "w", encoding="utf-8")
    kiFajl.writelines("II/F\n")
    kiFajl.writelines("\tA párosok száma: {}".format(parosDb))
    kiFajl.close()
file_kiir()

