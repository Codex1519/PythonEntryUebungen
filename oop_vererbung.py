class Person:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
    
    def get_fullname(self):
        if self.nachname is not None:
            return f"{self.vorname} {self.nachname}"
        else:
            return self.vorname

class Mitarbeiter(Person):
    def __init__(self, vorname, nachname, personalnummer):
        super().__init__(vorname, nachname)
        self.personalnummer = personalnummer
    
p1 = Person("Hans", "Meier")
ma = Mitarbeiter("Hans", "Meier" ,123)
ma.get_fullname

print(Person.get_fullname(p1))