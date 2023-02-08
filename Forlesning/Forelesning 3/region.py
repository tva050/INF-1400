from Værstasjon import Stasjon

class Region:
    
    def __init__(self, navn):
        self.navn = navn
        self.stasjoner = []
    
    def legg_til_stasjon(self, stasjon):
        self.stasjoner.append(stasjon)
        
    def __str__(self):
        s = self.navn + "\n"
        s+= "stasjoner:" + "\n"
        for stasjon in self.stasjoner:
            s+= str(stasjon) + "\n"
        return s
    
if __name__ == "__main__":
    nord = Region("Nord")
    
    nord.legg_til_stasjon(Stasjon(10, 12))
    nord.legg_til_stasjon(Stasjon(6, 15))
    
    print(nord)