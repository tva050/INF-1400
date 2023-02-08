class Sudoku_reader:
    def __init__(self, filename):
        self.file = open(filename, "r") # Opens the file
        self.current_line = 0

    # Returns a 2D list (9*9) of ints
    def next_board(self):
        try:
            board_txt = self.file.readline()
            board = [[0 for _ in range(9)] for _ in range(9)]
            sym_num = 0
            for i in range(9):
                for j in range(9):
                    board[i][j] = int(board_txt[sym_num])
                    sym_num += 1
            return board
        except:
            print("Reading error")
            quit(-1)
