
# Häufigkeiten

# Schreibe eine Funktion hauefigkeiten(),
# die zu jedem Zeichen eines übergebenen Strings die Häufigkeit ermittelt,
# mit der dieses Zeichen im String vorkommt.
# Zurückgegeben wird ein Dictionary,
# in dem jedem Zeichen dessen Vorkommenshäufigkeit zugeordnet wird.

# Beispiel:
# print(haeufigkeiten('Erdbeere'))
# {'E': 1, 'r': 2, 'd': 1, 'b': 1, 'e': 3}

from collections import Counter

def haeufigkeiten(text):
    return dict(Counter(text))

print(haeufigkeiten('Erdbeere'))