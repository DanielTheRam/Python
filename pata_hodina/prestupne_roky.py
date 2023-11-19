vychozi_rok = 1000
roky = ""
with open('leapyears.txt', 'w', encoding='utf-8') as f:
    while vychozi_rok <= 2024:
        if (vychozi_rok % 4 == 0 and (vychozi_rok % 400 == 0 or (vychozi_rok % 100 != 0 and vychozi_rok % 400 !=0))): 
            roky += str(vychozi_rok) +"\n" 
        vychozi_rok += 4
        f.write(f"""Year
{roky}""")    #do souboru zapisovat po jednom, vyhgnout se velkym promennym. Zjednodušit podmínku
