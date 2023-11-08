from random import randint
postupka = set()
pocet_generaci = 0
while len(postupka)<6:
    cislo = randint(1, 6)
    pocet_generaci += 1
    postupka.add(cislo)
print("Kompletní set:", postupka)
print(f"Celkový počet vygenerovaných čísel je: {pocet_generaci}")

