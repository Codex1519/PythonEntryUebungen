
# Roboter 2

# In dieser Aufgabe geht wieder um eine Roboterklasse.
# Uns interessiert nicht das Aussehen und die Beschaffenheit eines Roboters,
# sondern nur seine Position in einer imaginären „Landschaft”,
# die zweidimensional sein soll
# und durch ein Koordinatensystem beschrieben werden kann.
# Ein Roboter hat also zwei Attribute für die x- und die y-Koordinate.
# Es empfiehlt sich, diese Informationen in einer 2er-Liste zusammenzufassen,
# also beispielsweise position = [3, 4],
# wobei dann 3 der x-Position und 4 der y-Position entspricht.
# Der Roboter ist in eine der vier Richtungen „west”, „south”, „east”
# oder „north” orientiert, was wir in einem Attribut speichern wollen.
# Außerdem sollten unsere Roboter auch Namen haben.
# Allerdings dürfen die Namen nicht länger als 10 Zeichen sein.
# Sollte jemand versuchen,
# dem Roboter einen längeren Namen zuzuweisen,
# soll der Name auf 10 Zeichen abgeschnitten werden.
# Um die Roboter im Koordinatensystem bewegen zu können,
# benötigen wir eine move()-Methode.
# Die Methode erwartet einen Parameter „distance”,
# der angibt, um welchem Betrag sich der Roboter in Richtung
# der eingestellten Orientierung bewegen soll.
# Wird ein Roboter x beispielsweise mit x.move(10) aufgerufen
# und ist dieser Roboter östlich orientiert,
# also x.orientation == "east", und ist [3, 7] die aktuelle Position des
# Roboters, dann bewegt er sich 10 Felder östlich
# und befindet sich anschließend in Position [13, 7].

class roboter():
    def __init__(self):
        self.position = [0, 0]
        self.orientierung = "north"
        self.name = "roboter"
    
    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Orientierung: {self.orientierung}"
    
    def move(self, distance):
        if self.orientierung == "north":
            self.position[1] += distance
        elif self.orientierung == "south":
            self.position[1] -= distance
        elif self.orientierung == "east":
            self.position[0] += distance
        elif self.orientierung == "west":
            self.orientierung -= distance
        else: 
            print("Falsche Eingabe")#
        
    def set_name(self, name):
        if len(name) > 10:
            self.name = name[:10]
        else:
            self.name = name
    
    def get_name(self):
        return self.name
    
    def set_orientierung(self, orientierung):
        self.orientierung = orientierung
    
    def get_orientierung(self):
        return self.orientierung
    
    def set_position(self, position):
        self.position = position
    
    def get_position(self):
        return self.position
    
x = roboter()
print(x)
x.move(10)
print(x)
x.set_name("roboter2")
print(x)
x.set_orientierung("east")
print(x)
x.set_orientierung("west")
print(x)