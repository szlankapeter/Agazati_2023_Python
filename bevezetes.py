import  random

print("I/A")
nev = input("\tRendező neve: ")
cim = input("\tFilmi címe: ")
rnd = random.randint(0, 10)
print("I/B")
print(f"\tPontozás (0-10): {rnd}")

if rnd < 4:
    print("\tGyenge film")
elif rnd < 8 and rnd > 3:
    print("\t Érdemes megnézni")
else:
    print("\tKihagyhatatlan film")
