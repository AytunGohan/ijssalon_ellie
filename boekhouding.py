from helper import *
from presentatie import *
import csv
inkomsten = {
    'aardbeien-ijs-totaal' : 1000,
    'vanille-ijs-totaal': 2000,
    'chocolade-ijs-totaal': 1500,
    'waterijsjes-totaal': 750,
}
totaal_inkomsten = som(inkomsten)

#Functie presenteer gebruiken voor inkomsten en totaal_inkomsten
presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])