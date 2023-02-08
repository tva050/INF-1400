
class Flaske:
    
    def __init__(self, volum):
        self.volum = volum
        self.nivå = 0
    
    def fyll(self, ml):
        if self.nivå + ml <= self.volum:
            self.nivå += ml
        else:
            print("Flaske er full")
    
    def tøm(self):
        self.nivå = 0
    
    def __str__(self):
        return "Flaske-volum: " + str(self.volum) + " nivå: " + str(self.nivå)
                
julebrus = Flaske(1500) #ml
solo = Flaske(500) #ml

