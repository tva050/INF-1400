# ABC-formel
# x = (-b +- sqrt(b**2 - 4*a*c)) / 2*a

from math import *

class NegativRotError(Exception):
    pass
 
class FeilAntallArgumenter(Exception):
    pass

class IkkeNumberiArgumenter(Exception):
    pass

def abfformel(*args):
    # tar inn en Tuppel
    if len(args) != 3:
        raise FeilAntallArgumenter("Feil antall argumenter")
    
    #Sjekk om det er tall, når vi får tid
    if args == isinstance(args, int):
        raise IkkeNumberiArgumenter("Bare sett inn tall, ikke bokstaver")
    
    # Hent ut verdiene for de tre argumentene
    a,b,c =args[0:] # Dette kalles "slicing"
    
    # regne ut det som er i roten
    underRot = b**2 - 4*a*c # b**2 er b^2
    
    if underRot < 0:
        raise NegativRotError("Negativ rot")
    
    x1 = (-b+sqrt(underRot))/2*a
    x2 = (-b-sqrt(underRot))/2*a
    return x1, x2

if __name__ == "__main__":
    try:
        x1, x2 = abfformel(3,1,-5)
        print("x1=", x1, "x2=", x2)
    except NegativRotError as nerr:
        print("Feilen er:", nerr)
    except FeilAntallArgumenter as ferr:
        print("Feilen er:", ferr)
    except IkkeNumberiArgumenter as ierr:
        print("Feilen er:", ierr)
    print("Taskk for denne gangen!")
    