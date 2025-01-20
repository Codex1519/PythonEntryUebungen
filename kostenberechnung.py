
# Kostenberechnung

"""
Erstelle eine Funktion zur Kostenberechnung.
Dieser wird Preis, Anzahl und Währung als Argumente übergeben
und sie soll daraus die Kosten berechnen und zurück geben.
Standardmäßig soll die Anzahl 100 betragen
und die Währung Euro sein.
"""

def kostenberechnung(preis, anzahl = 100, waehrung = "Euro"):
    return preis * anzahl, waehrung

print(kostenberechnung(2.5))