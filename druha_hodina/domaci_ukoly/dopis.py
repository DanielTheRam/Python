import datetime
name = input("Napište své jméno ")
surname = input("Napište své příjmení ")
recipient = input("Napište jméno příjemce ")
sex = input("Zadejte pohlaví příjemce - Muž/Žena ")
company = input("Zadejte název společnosti")
date = datetime.date.today()

if sex == "Muž":
    adressing = "Vážený pane"
elif sex == "Žena":
    adressing = "Vážená paní"
else: 
    print("špatně zadané pohlaví")
dopis = f"""
{adressing} {recipient}

s velkým nadšením se přihlašuji o pracovní pozici ve vaší společnosti {company}.

Jsem profesionální popíječ kávy, scroller Instagramu a TikToku. 
Své flákání jsem začal rozvíjet už od mala, kdy jsem se do 16 let nechal krmit od matky. 
Jelikož jsem nyní již dospělý člověk a máma se mnou nemůže být všude, chystá mi alespoň svačiny, tak se nebojte, že vám sním všechny snacky z kuchyně.

Abych svůj pracovní výkon, který nebude nijak měřitelný, mohl podávat správně, potřebuji kvalitní wifi a zásuvku, kde mohu nabíjet telefon.
Věděli jste, že se iPhony rychle vybíjí? Strašné, že?

Jelikož je mi čerstvých 18 let a vysoká mě neláká, nemám od první práce vysoká očekávání.
Stačí mi 100k měsíčně, firemní byt a služební auto - přeci nebudu jezdit sockou. 
Ale pozor, nebudu jezdit v žádné kraksně, jejiž pořizovací cena neměla alespoň 7 cifer. 

S odpovědí moc dlouho nečekejte. O člověka jako mě se firmy velmi perou. 
{name} {surname}
{date}
"""
print(dopis)