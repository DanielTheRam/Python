# KAMEN NUZKY PAPIR
moznosti = ("kamen", "nuzky", "papir")

hrac = input("napiste 'kamen', 'nuzky', nebo 'papir': ")
import random                           #toto a 6. radek jsem jediny googlil
pocitac = random.choice(moznosti)
print(pocitac)

if hrac == "kamen" and pocitac == "nuzky":
    print("vyhrals")
elif hrac == "kamen" and pocitac == "papir":
    print("prohrals")
elif hrac == "kamen" and pocitac == "kamen":
    print("remiza")
elif hrac == "nuzky" and pocitac == "papir":
    print("vyhra")
elif hrac == "nuzky" and pocitac == "kamen":
    print("prohrals")
elif hrac == "nuzky" and pocitac == "nuzky":
    print("remiza")
elif hrac == "papir" and pocitac == "kamen":
    print("vyhrals")
elif hrac == "papir" and pocitac == "nuzky":
    print("prohrals")
elif hrac == "papor" and pocitac == "papir":
    print("remiza")
else:
    print("spatny vyraz")
