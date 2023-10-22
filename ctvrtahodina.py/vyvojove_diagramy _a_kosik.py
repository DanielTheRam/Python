print(True or False) #True, OR = pokud jedno z nich je pravda
print(True or True) #True
print(False or False) #False    
print(False and False) #False, AND = pokud jsou obě pravda
print(True and True) #True
print(False and True) #False

kosik = {"rohlík": 5, "banán": 3, "máslo": 1, "sýr": 2, "šunka": 2}
for i in kosik:
    print(f"položka: {i}, množství: {kosik[i]}")
print(kosik)
print (f"rohlík: {kosik['rohlík']}")
print(f"počet sýrů a šunky: {kosik['sýr'] + kosik['šunka']}")
print(f"všechny hodnoty košíku: {kosik.values()}")