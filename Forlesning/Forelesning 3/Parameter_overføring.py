

def add_one(number):
    number = number + 1
    
def flip(words):
    tmp = words[0]
    words[0] = words[1]
    words[1] = tmp

class Data:
    def __init__(self, number):
        self.number = number
        
    def print_info(self):
        print("this is the number:", self.number)

    def change_number(self, new_value):
        self.number = new_value

if __name__ == "__main__":
    greeting=["Hello", "World"]
    
    tall = Data(5)
    
    tall.change_number(10)
    
    tall.print_info()

