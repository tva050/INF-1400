from board import Board
from sudoku_reader import Sudoku_reader
from square import Square
from element import Element
import time


class Sudoku_board(Board): # inherits from Board
    def __init__(self, nums):  
        super().__init__(nums) # calls the init function from Board
        self._set_up_nums(nums) # calls the function that sets up the squares on the board
        self._set_up_elems()  # calls the function that sets up the links between the squares and elements (rows, columns, boxes)
        

    def _set_up_nums(self, nums):
        # Sets up the squares on the board (ints into Square objects)
        self.nums = [[Square(nums[i][j]) for j in range(self.n_rows)] for i in range(self.n_cols)]
        

    def _set_up_elems(self):
        global rows, columns, boxes # makes the lists global so that they can be used in the solve function
        # Making empty lists that will contain the elements (rows, columns, boxes)
        rows = []
        columns = []
        boxes = []
        

        # linkt between squares to our rows and columns. 
        for i in range(9):
            rows.append(Element("row"))
            columns.append(Element("column"))
            boxes.append(Element("box"))
        # Making the rows and columns
        for i in range(9):
            for j in range(9):
                rows[i].square_to_element(self.nums[i][j])  
                columns[j].square_to_element(self.nums[i][j])
    
        # The boxes are made by dividing the rows and columns into 3x3 boxes, and then adding the squares to the boxes
        for i in range(9):
            for j in range(9):
                boxes[(j//3)*3+i//3].square_to_element(self.nums[i][j]) 
                   

    def solve(self): # solving code written with help from:  https://www.youtube.com/watch?v=G_UYXzGuqvM   
        for row in range(9):  # goes through the rows
            for column in range(9):  # goes through the columns
                if self.nums[row][column].getValue() == 0: # checks if the square is empty
                    for number in range(1,10):  # goes through the numbers 1-9
                        if rows[row].possible(number) and columns[column].possible(number) and boxes[(column//3)*3+row//3].possible(number):  # checks if the number is possible/legal in the row, column and box
                            self.nums[row][column].setValue(number)  # sets the value of the square to the number that is possible/legal
                            self.solve()  # calls the solve function again, recursive method
                            self.nums[row][column].setValue(0)  # sets the value of the square back to 0 if the board is not solved
                    return
        print(self)  # prints the board if it is solved
        

if __name__ == "__main__":
    start = time.time() 
    
    reader = Sudoku_reader("sudoku_1M.csv") # reads the csv file
    for i in range(10):  # 10 boards
        board = Sudoku_board(reader.next_board())
        print("---------------------------------","\n","Board", i+1,":")  # prints the board number
        board.solve()  # solves the board
    
    end = time.time() 
    print("Run Time:",end - start)  