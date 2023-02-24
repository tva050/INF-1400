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

    def __init__(self, navn, ansvarsområde, sertifikat, kan_sikkerhet):
        super().__init__(navn, ansvarsområde)
        self.serifikat = sertifikat
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

class Bussjåfør(Person):
    
    def __init__(self, navn, sertifikat):
        super().__init__(navn, "Sjåfør")
        self.sertifikat = sertifikat
    
    def endreAnsvar(self, ansvar):
        raise RuntimeError("Bussjåfør kan ikke endre ansvar")
    
    def __str__(self):
        s = "=== Bussjåfør ===\n"
        s += super().__str__()
        return s

if __name__ == "__main__":
    per = Båtfører("per", "kaptein", "A5L1", True)
    anne = Bussjåfør("Anne", "D1E")
    
    print(per)
    print()
    print(anne)