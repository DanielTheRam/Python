import random
postupka = set()
pocet_generaci = 0

while True:
    cislo = random.randint(1, 6)
    pocet_generaci += 1

    if cislo not in postupka:
        postupka.add(cislo)

    if postupka == {1, 2, 3, 4, 5, 6}:
        print("Kompletní set:", postupka)
        print(f"Celkový počet vygenerovaných čísel je: {pocet_generaci}")
        break
