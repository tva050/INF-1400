
class Stasjon:
    
    def __init__(self, regn, temp):
        self.regn = regn
        self.temp = temp
    
    def hent_regn(self):
        return self.regn
    
    def hent_temp(self):
        return self.temp
    
    def __str__(self):
        return "stasjon med regn:" + str(self.regn) \
                + "temp: " + str(self.temp)

if __name__ == "__main__":
    eidkjosen = Stasjon(10, 12)
    print(eidkjosen)