class Square: 
    def __init__(self, value): 
        self.value = value
        self.row = None 
        self.column = None 
        self.box = None
    
    def getValue(self):   # returns the value of the square
        return self.value  
    def setValue(self, value): # sets the value of the square
        self.value = value
        
    # checks each element (row, column and box) if the number is possible/legal by using the possible function in element.py
    def check_if_legal(self, number): 
        if self.row.possible(number):
            if self.column.possible(number):
                if self.box.possible(number):
                    return True
        else:
            return False 
    
        
    
    