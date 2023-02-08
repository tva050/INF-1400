
class Person:
    """ En klasse som representerer en person som har et navn og en aldere """
    def __init__(self, alderen:int, navnet:str)->None:
        self.alder = alderen
        self.navn = navnet
        
    def getAlder(self):
        """ Returnerer alderen til personen som et heltall """
        return self.alder
    
    def setAlder(self, alderen):
        """ Sjekker om alderen er over 0 år og setter den til alderen """
        if alderen < 0:
            self.alder=0
        self.alder = alderen

    def getNavn(self):
        return self.navn
    
    def setNavn(self, navnet):
        self.navn = navnet
    
    def __str__(self): # Gjør om alder til string siden, den er opprinnelig int
        return "Navn: " + self.navn + " Alder: " + str(self.alder)



if __name__ == "__main__":
    print("Nå starter det! ")
    person1 = Person(23, "Ola Nordmann")
    person2 = Person(25, "Kari Nordmann")
    print(person1)
    person1.alder = 35 # ikke greit, fyfyfy!
    print(person1)