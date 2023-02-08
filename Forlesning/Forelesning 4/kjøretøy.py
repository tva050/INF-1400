class Kjøretøy:
    def __init__(self, regnummer, årstall):
        self.regnummer = regnummer
        self.årstall = årstall
    
        #standard get/set metoder
    def getRegnummer(self):
        return self.regnummer
    
    def setRegnummer(self):
        return self.regnummer
    
    def getÅrstall(self):
        return self.årstall
    
    def setÅrstall(self):
        return self.årstall
    
    def __str__(self):
        return "Regnummer: " + self.regnummer +"\n" +" Årstall: " + str(self.årstall)

class Motorsykkel(Kjøretøy):
    def __init__(self, regnummer, årstall):
        super().__init__(regnummer, årstall)
    
    """ def __str__(self):
        return "Motorsykkel: " + super().__str__() """

class Varebil(Kjøretøy):
    def __init__(self, regnummer, årstall, ant_liter):
        super().__init__(regnummer, årstall)
        self.ant_liter = ant_liter
    
    def getAntLiter(self):
        return self.ant_liter
    
    def setAntLiter(self):
        return self.ant_liter
    
    def __str__(self):
        return "Varebil: " + super().__str__() + "\n" + "Antall liter: " + str(self.ant_liter)
    
class Personbil(Kjøretøy):
    def __init__(self, regnummer, årstall, ant_seter):
        super().__init__(regnummer, årstall)
        self.ant_seter = ant_seter

    def getAntSeter(self):
        return self.ant_seter
    
    def setAntSeter(self):
        return self.ant_seter
    
    def __str__(self):
        return "Personbil: " + super().__str__() + "\n" + "Antall seter: " + str(self.ant_seter)
    
class Garasje:
    def __init__(self, gID):
        self.gID = gID
        # Lager en tom liste for kjøretøy
        self.kjøretøyliste = []
    
    def getGID(self):
        return self.gID
    
    def setGID(self):
        return self.gID
    
    def parkerKjøretøy(self, kjøretøy):
        self.kjøretøyliste.append(kjøretøy)
    
    def finnantall(self):
        return len(self.kjøretøyliste)
    
    def finnIGarasje(self, regnummeret):
        for kjøretøy in self.kjøretøyliste:
            if kjøretøy.getRegnummer() == regnummeret:
                return True
        return False
    

if __name__ == "__main__":
    
    p1 = Personbil("AY12345", 2010, 5)
    p2 = Personbil("YA22336", 2020, 3)
    
    v1 = Varebil("EE22222", 2010, 3000)
    
    m1 = Motorsykkel("AA111", 1999)
    
    g1 = Garasje(123)
    g1.parkerKjøretøy(p1)
    g1.parkerKjøretøy(v1)
    g1.parkerKjøretøy(m1)
    
    
    print("antall kjøretøy i garasjen: ", str(g1.finnantall()))
    print("finn i garasje: ", str(g1.finnIGarasje("EE22222")))
    


        