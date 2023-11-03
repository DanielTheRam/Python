# KAMEN NUZKY PAPIR 2
import random  
moznosti = ("kamen", "nuzky", "papir")
konec_hry = True
while konec_hry:
    hrac = input("napiste 'kamen', 'nuzky', nebo 'papir': ")                         
    pocitac = random.choice(moznosti)
    print(pocitac)
    if hrac == "kamen" and pocitac == "nuzky":
        print("vyhrals")
        konec_hry = False
    elif hrac == "kamen" and pocitac == "papir":
        print("prohrals")
    elif hrac == pocitac:
        print("remiza")
    elif hrac == "nuzky" and pocitac == "papir":
        print("vyhrals")
        konec_hry = False
    elif hrac == "nuzky" and pocitac == "kamen":
        print("prohrals")
    elif hrac == "papir" and pocitac == "kamen":
        print("vyhrals")
        konec_hry = False
    elif hrac == "papir" and pocitac == "nuzky":
        print("prohrals")
    else:
        print("spatny vyraz")

