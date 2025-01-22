class Person:
    def __init__(self, vorname, nachname = None):
        self.vorname = vorname
        self.nachname = nachname

    def get_fullname(self):
        if self.nachname is not None:
            return f"{self.vorname} {self.nachname}"
        else:
            return self.vorname
    
class Fahrzeug:
    def __init__(self, kennzeichen, besitzer = None):
        self.kennzeichen = kennzeichen
        self.besitzer = besitzer

    def fahren(self):
        print("brum")   

    def info(self):
        return f"Das Fahrzeug {self.kennzeichen} gehört {self.besitzer.get_fullname()}"

p1 = Person("Hans")
f1 = Fahrzeug("M-AB-123", p1)

print(f1.info())