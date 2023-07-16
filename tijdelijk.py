#Bestand tijdelijk.py aangemaakt.
#Opdracht 2
prijzen = {
    'aardbei' : 3,
    'vanille' : 4,
    'chocolade' : 5
}

#Opdracht 3
aanbieding = prijzen['vanille'] * 0.8

#Opdracht 4
reclame_tekst = (f'Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}0')

#Opdracht 5
#Ik kreeg al een resultaat zonder decimalen. Ik heb daarom een 0 achter de variabele 
#aanbieding geplaatst. 
reclame_tekst2 = reclame_tekst[:62]
#print (reclame_tekst2)

#Opdracht 6
reclame_tekst3 = reclame_tekst.upper()
#print(reclame_tekst3)

#Opdracht 7
reclame_tekst4 = reclame_tekst3.split(' ')
#print(reclame_tekst4)
#Opdracht 8 
for el in reclame_tekst4:
    print (el)
#print() #Voor duidelijkere output

#Opdracht 9
for el in reclame_tekst4:
    print(el.lower())

#Opdracht 10
print('hieronder opdracht 10')
for el in reclame_tekst4:
    if len(el) > 5:
        print(el.upper())
    else:
        print(el.lower())
