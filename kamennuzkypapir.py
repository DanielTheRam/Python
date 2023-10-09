import random                           #toto a 5. radek jsem jediny googlil, konvence se píší na první řádek

moznosti = ("kamen", "nuzky", "papir")
hrac = input("napiste 'kamen', 'nuzky', nebo 'papir': ")
pocitac = random.choice(moznosti)
print(pocitac)

if hrac == "kamen" and pocitac == "nuzky":
    print("vyhrals")
elif hrac == "kamen" and pocitac == "papir":
    print("prohrals")
elif hrac == "nuzky" and pocitac == "papir":
    print("vyhrals")
elif hrac == "nuzky" and pocitac == "kamen":
    print("prohrals")
elif hrac == "papir" and pocitac == "kamen":
    print("vyhrals")
elif hrac == "papir" and pocitac == "nuzky":
    print("prohrals")
elif hrac == pocitac:
    print("remiza - oba jste zvolili stejnou moznost")
else:
    print("spatny vyraz")
