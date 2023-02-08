from Person import Person

class ansatt(Person):
    
    def __init__(self, alderen, navnet, stilling, lønn):
        super().__init__(alderen, navnet)
        self.stilling = stilling
        self.lønn = lønn
        
    def getStilling(self):
        return self.stilling
    
    def setStilling(self, stilling):
        self.stilling = stilling
    
    def getLønn(self):
        return self.lønn
    
    def setLønn(self, lønn):
        self.lønn = lønn
    
    def __str__(self):
        return super().__str__() + " Stilling: " + self.stilling + " Lønn: " + str(self.lønn)

class student(Person):
    
    def __init__(self, alderen, navnet, studie, studentnummer):
        super().__init__(alderen, navnet)
        self.studie = studie
        self.studentnummer = studentnummer
    
    def getStudie(self):
        return self.studie
    
    def setstudie(self, studie):
        self.studie = studie
    
    def getStudentnummer(self):
        return self.studentnummer
    
    def setStudentnummer(self, studentnummer):
        self.studentnummer = studentnummer
     
    def __str__(self):
        return Person.__str__(self)+" utdanningen er: "+self.studie\
            +" og studentnummeret er: "+str(self.studentnummer)

if __name__ == "__main__":
    ansatt1 = ansatt(23, "Ola Nordmann", "Lektor", 300000)
    student1 = student(23, "Ola Nordmann", "Romfysikk", 123456)
    print(ansatt1)
    print(student1)