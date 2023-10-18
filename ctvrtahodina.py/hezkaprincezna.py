#zeptám se uživatele, jestli je princezna hezká nebo ošklivá a jestli je chudá nebo bohatá. 
krasa = input("Je princezna hezká nebo ošklivá?")
jmeni = input("Je princezna bohatá nebo chudá?")
if krasa == "hezká" and jmeni == "bohatá":
    print("Tu si rozhodně vezmi")
elif krasa == "hezká" and jmeni == "chudá":
    print("Tu si vezmi, pokud ji zvládneš živit")
elif krasa == "ošklivá" and jmeni == "bohatá":
    print("Tu si vezmi a za její prachy ji pošli na plastickou operaci")
elif krasa == "ošklivá" and jmeni == "chudá":
    print("Alespoň ti neuteče")
else: 
    print("Špatně zadaný výraz")