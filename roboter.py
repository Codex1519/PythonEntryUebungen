
# Roboter

# Wir haben folgende Roboterklasse geschrieben:

class Robot:

    def __init__(self, name):
        if name == "Hugo":
            self.name = "Marvin"
        else:
            self.name = name
        
    def __str__(self):
        return self.name



# Letzte drei Zeilen:
x = Robot("Marvin")
y = Robot("Hugo")
print(x.name, y.name)  # Marvin Hugo

# Diese Klasse erfreut sich nun auf einmal weltweit großer Beliebtheit.
# Wir haben allerdings ein Problem:
# Die internationale Robotergewerkschaft konnte ein weltweites Verbot durchsetzen,
# dass Roboter nicht mehr „Hugo” genannt werden dürfen.
# Schreibe nun die Klasse so um,
# dass Roboter automatisch „Marvin” genannt werden,
# wenn jemand versucht, sie „Hugo” zu taufen
# oder versucht den Roboter in „Hugo” umzubenennen.
# Für die Benutzer der Klasse darf sich natürlich nichts ändern,
# d.h. die letzten drei Zeilen müssen unverändert bleiben können
# (nur muss jetzt zweimal "Marvin" ausgegeben werden).

# Bitte auch das Umbenennen testen:
# Nach dem Versuch, einen Roboter in „Hugo” umzubenennen,
# muss dieser Roboter „Marvin” heissen.



