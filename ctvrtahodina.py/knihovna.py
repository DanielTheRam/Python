def get_volne_knizky(borrowed_books):
    available_books = []
    for book in borrowed_books:
        if borrowed_books[book] == "":
            available_books.append(book)
    return available_books

borrowed_books = {"Veronika decides to die": "Karel Novák", "Alchemist": "", "Animal farm": "Zuzana Malátová", "1982": "Marie Sýkorová", "R.U.R.": "Adam Dítě"}
name = input("Napište svoje jméno ")
while True:
    volne_knizky = get_volne_knizky(borrowed_books)
    action = input("""Vyberte číslo operace, kterou chcete provést:
                    1 - Zobrazit seznam knih
                    2 - Vratit knihu
                    3 - Pujcit si knihu""")
    if action =="1":
        if name == "admin":
                print(f"Seznam knih: {borrowed_books.keys()}")
        else:
            print(f"Seznam knih: {get_volne_knizky(borrowed_books)}")
    elif action == "2":
        kniha = input("Jakou knihu chcete vrátit? ")
        if kniha in borrowed_books:
             borrowed_books[kniha] = ""
        else:
            print("Kniha je asi jiné knihovny lol.")
    elif action == "3":
        gbook = input(f"jakou knihu si chcete půjčit? {get_volne_knizky(borrowed_books)}")
        if gbook in borrowed_books:
             borrowed_books[gbook] = name
        else: 
             print("Kniha není dostupná")    
    else: 
        print("špatně zadané číslo operace")
print(get_volne_knizky())