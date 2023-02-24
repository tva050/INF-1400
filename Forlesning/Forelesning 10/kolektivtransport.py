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
    

if __name__ == "__main__":
    per = Person("Per")
    print(per)