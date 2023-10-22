name = input("Napište svoje jméno ")
borrowed_books = {"Veronika decides to die": "Karel Novák", "Alchemist": "Jiří Svoboda", "Animal farm": "Zuzana Malátová", "1982": "Marie Sýkorová", "R.U.R.": "Adam Dítě"}
available_books = {"Lord of the Rings": 1, "Hobbit": 3, "Angels and Demons": 2, "Little Prince": 6}
users_books = {"Dekameron"}
while True:
    if name == "admin":
        action = input("""Vyberte číslo operace, kterou chcete provést:
                       1 - Vaše půjčené knihy
                       2 - Zobrazit seznam dostupných knih
                       3 - Vratit knihu
                       4 - Pujcit si knihu
                       5 - Zobrazit seznam všech pujcenych knih """)
        if action =="1":
            if not users_books:
                print("Nemáte žádnou půjčenou knihu")
            else:
                print(f"Vaše knihy jsou: {users_books}")
        elif action == "2":
            print(f"Seznam dostupných knih/počet: {available_books} ")
        elif action == "3":
                if not users_books:
                      print("Nemáte půjčenou žádnou knihu")
                else: 
                    rbook = input(f"Jakou knihu chcete vrátit?{users_books} ")
                    if rbook in users_books:
                        rbook = users_books.pop()
                        available_books[rbook] =+ 1
                        print(f"Vaše půjčené knihy jsou: {users_books}")
                    elif not rbook in users_books:
                        print("Takovou knihu půjčenou nemáte")
        elif action == "4":
                gbook = input(f"Jakou knihu si chcete půjčit? {available_books} ")
                if gbook in available_books:
                      users_books.add(gbook)
                      del available_books[gbook]
                      borrowed_books[gbook] = name
                      print(f"Vaše půjčené knihy jsou: {users_books}")
                else:
                      print("Tato kniha není k dispozici")
        elif action =="5":
                print(f"Seznam půjčených knih: {borrowed_books}")
        else: 
                print("Špatně zadané číslo operace")
    else:
        action = input("""Napište číslo operace, kterou chcete provést:
                        1 - Vaše půjčené knihy
                        2 - Zobrazit seznam dostupných knih 
                        3 - Vratit knihu 
                        4 - Pujcit si knihu """)
        if action =="1":
            if not users_books:
                print("Nemáte žádnou půjčenou knihu")
            else:
                print(f"Vaše knihy jsou: {users_books}")
        elif action == "2":
                print(f"Seznam dostupných knih/počet: {available_books} ")
        elif action == "3":
                if not users_books:
                      print("Nemáte půjčenou žádnou knihu")
                else: 
                    rbook = input(f"Jakou knihu chcete vrátit?{users_books} ")
                    if rbook in users_books:
                        rbook = users_books.pop()
                        available_books[rbook] =+ 1
                        print(f"Vaše půjčené knihy jsou: {users_books}")
                    elif not rbook in users_books:
                        print("Takovou knihu půjčenou nemáte")
        elif action == "4":
                gbook = input(f"Jakou knihu si chcete půjčit? {available_books} ")
                if gbook in available_books:
                      users_books.add(gbook)
                      available_books[gbook] -= 1
                      print(f"Vaše půjčené knihy jsou: {users_books}")
                else:
                      print("Tato kniha není k dispozici")
        else:
            print("Špatně zadaný výraz")
# pokud si uživatel půjčí knihu, kterou poté vrátí, není odebrán ze seznamu půjčených knih
# kdy používám del/pop/remote