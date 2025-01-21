

# Karten mischen

# Schreibe ein Skript, das das Mischen der 32 Karten eines Skatspiels simuliert.
# Jede Karte wird durch ein Tupel der Form (farbe, wert) dargestellt.
# Farben sind: Kreuz, Pik, Herz und Karo.
# Werte sind: Ass, König, Dame, Bube, Zehn, Neun, Acht, Sieben.

# In dem Skript wird zunächst eine Liste mit den 32 Karten-Tupeln erstellt.

# Durch wiederholtes Vertauschen zweier zufällig ausgewählter
# Listenelemente soll die Lists dann noch gemischt werden.
# (Mischen ohne random.shuffle())
import random


def main():
    kartendeck = kartenErstellen()
    
    print(kartendeck)

def kartenErstellen():
    werte = ("Ass", "König", "Dame", "Bube", "Zehn", "Neun", "Acht", "Sieben")
    farben = ("Kreuz", "Pik", "Herz", "Karo")
    
    kartendeck = list()
    
    for farbe in farben:
        for wert in werte:
            karte = f'{farbe} {wert}'
            kartendeck.append(karte)
    
    return kartendeck

def kartenMischen(deck):
    for _ in range(100):
        i = random.randint(0,len(deck) -1)
        j = random.randint(0, len(deck)-1)
        deck[i], deck[j] = deck[j], deck[i]
    return deck


if __name__ == '__main__':
    main()
