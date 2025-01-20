
# Teilersumme

"""
Schreibe eine Funktion, die überprüft, ob bei einer Zahl
die Summe aller Teiler kleiner als die Zahl ist.
Die Zahl selber soll hierbei nicht zu den Teilern zählen.

Bei 81 würde True zurück gegeben werden, da
1 + 3 + 9 + 27 = 40
und 40 < 81

Bei 80 würde False zurück gegeben werden, da
1 + 2 + 4 + 5 + 8 + 10 + 16 + 20 + 40 = 106
und 106 > 80
"""

def teilersumme(zahl: int) -> bool:
    summe = 0
    for i in range(1, zahl):
        if zahl % i == 0:
            summe += i
    return summe < zahl

print(teilersumme(90))
    