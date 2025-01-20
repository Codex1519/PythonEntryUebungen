
# Nettopreis

"""
Schreibe eine Funktion zum Berechnen des Nettopreises.
Dieser Funktion soll der Bruttopreis übergeben werden
und sie soll den Nettopreis zurück geben.
Der Mehrwertsteuersatz soll als zweiter Parameter
übergeben werden können.
Der Standardwert des Mehrwertsteuersatzes soll 19 sein.
"""

def nettopreis(bruttopreis, mwst = 19):
    nettopreis = bruttopreis / (100 + mwst) * 100
    return round(nettopreis, 2)

def summe(initial = 0, *args):
    sum = initial
    for a in args:
        sum += a
    return sum


print(nettopreis(150))