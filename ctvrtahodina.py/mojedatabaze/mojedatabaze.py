from sqlite4 import SQLite4
import random
databaze = SQLite4("Růžové_Cukrátko.db")
databaze.connect()
# if databaze.select("knp") == "":
databaze.create_table("knp", ["jméno", "skóre"])
databaze.insert("knp", {"jméno": "člověk", "skóre": 0})
databaze.insert("knp", {"jméno": "počítač", "skóre": 0})
clovek = ""
pocitac = ""
tabulka = databaze.select("knp")
for i in tabulka:
    if i[0] == "člověk":
        clovek = i[1]
    if i[0] == "počítač":
        pocitac = i[1]
#místo tohoto foru použíj database.execute() s selectem v sql 
hra = True
print(f"hrac:{clovek}, počítač:{pocitac}")
moznosti = ("k", "n", "p")
vysledek_hrac = 0
vysledek_pocitac = 0
jmeno = input("Zadejte svoje jméno: ")
while True:
    hrac = input("""Napište: kámen,nůžky,papír """)
    
    pocitac_tip = random.choice(moznosti)
    if hrac == pocitac_tip:
        print("Nerozhodně")
    elif hrac == "k" and pocitac_tip == "n" or hrac == "n" and pocitac_tip == "p" or hrac == "k" and pocitac_tip == "n":
        vysledek_hrac += 1
        print("Vyhráls")
        clovek += vysledek_hrac
        databaze.update("knp", {"jméno": "člověk", "skóre": clovek})
        break
    elif hrac == "k" and pocitac_tip == "p" or hrac == "n" and pocitac_tip == "k" or hrac == "p" and pocitac_tip == "n":
        vysledek_pocitac += 1 
        pocitac += vysledek_pocitac
        databaze.update("knp", {"jméno": "počítač", "skóre": pocitac})
        print("Prohráls")
        break
    else:
        print("Špatně zadaný výraz")


