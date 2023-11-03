import random                                              
moznosti = ("kamen", "nuzky", "papir")
while True:
    hrac = input("napiste 'kamen', 'nuzky', nebo 'papir': ")
    from random import choice 
    pocitac = choice(moznosti)
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

