from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijsnieuw = prijs - (prijs*korting)
    print (f'Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijsnieuw} euro')
    return prijsnieuw
    
# Aanroepen van functie aanbieding_1
# aanbieding_1('aardbei', 4, 0.1)


def inkomsten_totaal(inkomsten= [220, 430, 125, 160, 205, 90, 345], btw = 0.09): 
    totaal = sum(inkomsten)
    btwbedrag = totaal * btw
    return print(f'Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btwbedrag} euro btw betaald dient te worden.')

inkomsten_totaal()

def laag_en_hoog(mijn_lijst = [220, 430, 125, 160, 205, 90, 345]):
    laag_en_hoog = [min(mijn_lijst), max(mijn_lijst)]
    return (laag_en_hoog)

print(laag_en_hoog())

def gemiddelde (mijn_lijst = [220, 430, 125, 160, 205, 90, 345]):
    gemiddelde = sum(mijn_lijst)/ len(mijn_lijst)
    return print(f'De gemiddelde inkomsten deze week zijn {gemiddelde} euro')

gemiddelde()

def meervoudig (invoer_lijst = [10, 5, 3, 2, 1, 2, 9]):
    return (laag_en_hoog(invoer_lijst))

meervoudig()

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie([5,10]))



