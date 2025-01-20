import random
# Zwei Zahlen genau vergleichen

# Schreibe ein Programm, das testet und ausgibt,
# welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
# Die beiden Zahlen sollen zufällig erzeugt werden.

zahl1 = int(input("Bitte geben Sie eine Zahl ein: "))
zahl2 = int(input("Bitte geben Sie eine weitere Zahl ein: "))

if zahl1 > zahl2:
    print("Zahl 1 ist größer als Zahl 2")
elif zahl1 < zahl2:
    print("Zahl 2 ist größer als Zahl1")
else:
    print("Beide Zahlen sind gleich groß")