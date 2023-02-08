
class Odd_number(list):
    # Gone to add only odd numbers
    def append(self, number):
        if not isinstance(number, int):
            raise TypeError("Ikkje braa, heltall")
            print("will not go trough")
        if number%2 == 0:
            raise ValueError("Not alowde with parttall")
        super().append(number)
    
    def testOddOnly(self, number):
        # Opptetter et object av type Odd_number
        #legg til noen element i odd-listen
        try:
            self.append(number)
        except TypeError as terr:
            print("ÅÅ nei ble feil, og feilmeldingen er", terr)
        except ValueError:
            print("oida, ble en feil, men jeg skal hjelpe deg :)")
            self.append(number+1)
        else:
            print("alt gikk bra så da kan denne koden får lov til å kjøre.")
        finally:
            print("Her kan vi legge kode som vil kjøre uansett, \
                feks når vi rydde opp noe.")
    

if __name__=="__main__":
    
    odd = Odd_number()
    odd.testOddOnly(5)
    odd.testOddOnly("hei")
    odd.testOddOnly(6)
    print("ferdig")
    
    
    