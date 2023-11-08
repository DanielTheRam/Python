all_books = {"Veronika decides to die": "Karel Novák", 
                  "Alchemist": "", 
                  "Animal farm": "Zuzana Malátová",
                  "1982": "Marie Sýkorová", 
                  "R.U.R.": "Adam Dítě",
                  "Clown": "",
                  "Miracle": "",
                  "My fair lady": ""}
name = input("Napište svoje jméno ")
tveknihy = ""
dostupne = {kniha: jmeno for kniha, jmeno in all_books.items() if jmeno == ""}
while True:
    action = input("""Vyberte číslo operace, kterou chcete provést:
                    1 - Zobrazit seznam knih
                    2 - Vratit knihu
                    3 - Pujcit si knihu""")
    if action =="1":
        if name == "admin":
                print(f"Seznam knih: {all_books}")
        else:
            print(f'Seznam knih: {dostupne}')
    elif action == "2":
        kniha = input("Jakou knihu chcete vrátit? ")
        if kniha in all_books:
             all_books[kniha] = ""
        else:
            print("Kniha je asi jiné knihovny lol.")
    elif action == "3":
        gbook = input(f"jakou knihu si chcete půjčit? ")
        if gbook in all_books:
             all_books[gbook] = name
             tveknihy += gbook
             print(f"Vaše knihy jsou: {tveknihy}")
        else: 
             print("Kniha není dostupná")    
    else: 
        print("špatně zadané číslo operace")
