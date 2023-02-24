class Administrasjon:
    
    def __init__(self, avdelinger):
        self.ansatte = []
        self.avdelinger = avdelinger
    
    def leffTilAnsatt(self, navn, type):
        if type != "Fører" or type != "Admin":
            raise ValueError("Ansatte må være fører eller admin")

class Person():
    
    def __init__(self, navn, ansvarsområde):
        self.navn = navn
        self.ansvarsområde = ansvarsområde
    
    def endreAnsvar(self, ansvar):
        self.ansvarsområde = ansvar
    
    def __str__(self):
        return "Person som heter " + self.navn + " med ansvar for: " + self.ansvarsområde
    
class Båtfører(Person):

    def __init__(self, navn, ansvarsområde, serifikat, kan_sikkerhet):
        super().__init__(navn, ansvarsområde)
        self.serifikat = serifikat
        self.kan_sikkerhet = kan_sikkerhet
    
    # Polygrafi
    def __str__(self):
        s = "=== Båtfører ===\n"
        s += super().__str__()
        if self.kan_sikkerhet:
            s += "\nPerson har sikkerhetskurs"
        else:
            s += "\nPersonen har IKKE sikkerhetskurs"
        return s

class Busssjåfør(Person):
    
    def __init__(self, navn, serifikat):
        super().__init__(navn, "Sjåfør")
        
            

if __name__ == "__main__":
    per = Båtfører("per", "kaptein", "A5L1", True)
    print(per)