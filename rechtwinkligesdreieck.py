# Rechtwinklige Dreiecke

# Gesucht ist die Menge aller rechtwinkligen Dreiecke mit ganzzahligen Seitenlängen jeweils unter 20.
# Jedes Dreieck soll durch ein Tupel mit den drei Seitenlängen dargestellt werden.
# Beispiel: (3, 4, 5)
# Beachten Sie: In rechtwinkligen Dreiecken gilt der Satz des Pythagoras:
# a² + b² = c².

berechnungen =[]
for a in range(1,20):
    for b in range(a, 20):
        for c in range(b,20):
            if a**2 + b**2 == c**2:
                berechnungen.append((a,b,c))

print("Folgende Berechnungen haben sich ergeben:", berechnungen)