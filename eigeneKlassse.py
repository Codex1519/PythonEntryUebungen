# Eigene Klasse

# Suche dir ein Objekt aus deiner Umgebung/Fantasie.
# Schreibe eine eigene Klasse dazu mit
# Konstruktor
# Objekt-Attributen
# Objekt-Methoden
# Statischem Attribut
# ToString-Methode - __str__()
# Gettern & Settern

# Erzeuge dann einige Objekte, verändere sie und lasse sie wieder anzeigen.

class Auto:
    # Konstruktor 
    def __init__(self):
        self.marke = "VW"
        self.modell = "Golf"
        self.farbe = "schwarz"
        self.ps = 150
        self.km = 0

    # Objekt-Methoden
    def fahren(self, km):
        self.km += km
        
    
    # Statisches Attribut
    anzahl_autos = 0
    
    # ToString-Methode
    def __str__(self):
        return f"Marke: {self.marke}, Modell: {self.modell}, Farbe: {self.farbe}, PS: {self.ps}, KM: {self.km}"
    
    # Getter & Setter
    
    def get_marke(self):
        return self.marke
    
    def set_marke(self, marke):
        self.marke = marke
        
    def get_modell(self):
        return self.modell
    
    def set_modell(self, modell):
        self.modell = modell
        
    def get_farbe(self):
        return self.farbe
    
    def set_farbe(self, farbe):
        self.farbe = farbe
    
    def get_ps(self):
        return self.ps
    
    def set_ps(self, ps):
        self.ps = ps 
    
    def get_km(self):
        return self.km
    
    def set_km(self, km):
        self.km = km
    
# Erzeuge Objekte

auto1 = Auto()
auto2 = Auto()

print(auto1)

auto1.fahren(200)
print(auto1)


