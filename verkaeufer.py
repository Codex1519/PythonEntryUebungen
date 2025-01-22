
# Verkäufer

# Gegeben ist eine Liste von Verkäufern mit ihren getätigten Verkäufen
# für ein bestimmtes Produkt.
# Die Liste besteht aus 4 Tupel der Art (Vorname, Nachname, Anzahl, Einzelpreis):
"""
[('John', 'Baker', 46, 18.67),
('Randy', 'Baker', 48, 27.99),
('Tina', 'Baker', 53, 27.23),
('Andrea', 'Baker', 40, 31.75),
('Eve', 'Baker', 44, 18.99),
('Henry', 'Baker', 50, 23.56)]
"""
# Sortiere die Liste zuerst nach den Verkaufserlösen,
# also dem Produkt aus der Anzahl und dem Einzelpreis.
# Dann gebe die Liste nochmals nach den Nachnamen sortiert aus.
# Bei Gleichheit des Nachnamens sortiere anhand des Vornamens weiter.

# Löse es einmal per Higher-Order-Funktionen und einmal klassisch.

verkaeufe = [('John', 'Baker', 46, 18.67),
            ('Randy', 'Baker', 48, 27.99),
            ('Tina', 'Baker', 53, 27.23),
            ('Andrea', 'Baker', 40, 31.75),
            ('Eve', 'Baker', 44, 18.99),
            ('Henry', 'Baker', 50, 23.56)]

sortiert_nach_erlösen = sorted(verkaeufe, key=lambda x: int(x[2])* float(x[3]), reverse = True)
print(sortiert_nach_erlösen)


sortiert_nach_nachnamen = sorted(sortiert_nach_erlösen, key=lambda x: (x[1], x[0]))
print(sortiert_nach_nachnamen)


def nach_erlös_sortiert():
    for i in range(len(verkaeufe)-1):
        for j in range(len(verkaeufe)-i-1):
            if (verkaeufe[j] * verkaeufe[j][3] < (verkaeufe[j + 1][2] * verkaeufe[j + 1][3])):
                verkaeufe[j], verkaeufe[j + 1] = verkaeufe[j + 1], verkaeufe[j]
    return verkaeufe