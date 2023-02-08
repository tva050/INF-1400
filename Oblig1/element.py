class Element:
    def __init__(self, type):
        self.squares = [] # list of squares in the element
        self.type = type 
    
    def square_to_element(self, square):  # adds a square to the element (row, column or box) to which it belongs
        self.squares.append(square) # adds the square to the list of squares in the element
        if self.type == "row":  
            square.row = self
        elif self.type == "column":
            square.column = self
        elif self.type == "box":
            square.box = self
                
    def possible(self, possible_number):
        for i in range(9):  # checks if the number is already in the element, if it is, it is not possible 
            if self.squares[i].getValue() == possible_number: 
                return False
        return True # if the number is not in the element, it is possible
        
        
        
                 