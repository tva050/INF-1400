class Board:
    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.nums = [[None for _ in range(self.n_rows)] for _ in range(self.n_cols)]

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n" 
        r += "[["
        for num in self.nums:
            for elem in num:
                r += str(elem.getValue()) + ", " 
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + "]"
        return r