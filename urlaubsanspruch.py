
#  Urlaubsanspruch
#
#  Für die Bestimmung des Urlaubsanspruch der Beschäftigten einer Firma
#  soll ein Programm entwickelt werden.
#  Die Grundlage für die Berechnung des Urlaubsanspruch
#  bildet die Betriebsvereinbarung.
#  Das Programm soll die Anzahl der Urlaubstage für
#  jeweils einen Beschäftigten berechnen.
#
#  Betriebsvereinbarung:
#  Allen Beschäftigten stehen 26 Tage Urlaub zu.
#  Minderjährige Beschäftigte erhalten 30 Tage Urlaub.
#  Beschäftigte, die älter als 55 Jahre sind, erhalten 28 Tage Urlaub.
#  Beschäftigte mit einer Behinderung ab 50 % erhalten
#  zusätzlich 5 weitere Tage Urlaub.
#  Beschäftigte mit einer Betriebszugehörigkeit von mehr als 10 Jahren
#  erhalten 2 zusätzliche Tage Urlaub.

# Funktion zum Berechnen des Urlaubsanspruchs
def urlaubsanspruch(alter, behinderung, betriebszugehörigkeit):
    urlaub = 26
    if alter < 18:
        urlaub = 30
    elif alter > 55:
        urlaub = 28
    if behinderung >= 50:
        urlaub += 5
    if betriebszugehörigkeit > 10:
        urlaub += 2
    return urlaub

print("Urlaubsanspruch für Beschäftigten: " + str(urlaubsanspruch(25, 60, 15)))
print("Urlaubsanspruch für Beschäftigten: " + str(urlaubsanspruch(18, 40, 5)))
print("Urlaubsanspruch für Beschäftigten: " + str(urlaubsanspruch(60, 70, 20)))
