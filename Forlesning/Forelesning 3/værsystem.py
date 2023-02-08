from region import Region
from Værstasjon import Stasjon


class Værsystem:
    
    def __init__(self):
        self.regioner = {}
        
    def legg_til_region(self, region,navn):
        self.regioner[navn] = region
        
    def legg_til_stasjon_på_regioner(self, regnavn, stasjon):
        self.regioner[regnavn].legg_til_stasjon(stasjon)
    
    def print_stasjon(self,navn):
        print(self.regioner[navn])
        
if __name__ == "__main__":
    
    system = Værsystem()
    
    system.legg_til_region(Region("Nord"), "Nord")
    system.legg_til_region(Region("Sør"), "Sør")
    
    system.legg_til_stasjon_på_regioner("Nord", Stasjon(10, 12))
    system.legg_til_stasjon_på_regioner("Nord", Stasjon(6, 15))
    
    system.legg_til_stasjon_på_regioner("Sør", Stasjon(10, 12))
    
    system.print_stasjon("Nord")
    system.print_stasjon("Sør")