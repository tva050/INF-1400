""" 
class Animal:
    
    def __init__(self, sound):
        self.sound = sound
        
    def roar(self):
        print("Hear my sound:", self.sound)

class WildAnimal(Animal):
    
    def __init__(self, sound, habitat):
        super().__init__(sound)
        self.habitat = habitat

class Pet(Animal):
    
    def __init__(self, sound, name):
        super().__init__(sound)
        self.name = name

class Cat(Pet, WildAnimal):
    
    def __init__(self, sound ,name, age):
        super().__init__(sound, name)
        self.age = age
        

if __name__ == "__main__":
    miss = Cat("Miau", "Kitty", 48) """
    
class Pet:
    
    def __init__(self, sound, name):
        self.name = name
        self.sound = sound
        
    def roar(self):
        print("Hear my sound:", self.sound)
        
class Cat(Pet):
    
    def __init__(self, sound ,name, age):
        super().__init__(sound, name)
        self.age = age
    
    def roar(self):
        print(self.sound, "cux imma cat")

if __name__ == "__main__":
    fido = Pet("Woof", "Fido")
    fido.roar()
    
    miss = Cat("Miau", "Kitty", 48)
    miss.roar()
    