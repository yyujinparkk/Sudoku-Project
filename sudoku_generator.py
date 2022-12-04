import math  # library needed to use sqrt to get box_length
import random  # library needed to generate random integers


class SudokuGenerator:  # holds all functions in a class which can be used to generate a puzzle

    def __init__(self, row_length, removed_cells):  # constructor function
        self.row_length = row_length  # initializes row_length as a variable
        self.removed_cells = removed_cells  # initializes removed_cells as a variable
        self.board = [[0 for i in range(self.row_length)] for j in range(self.row_length)]
        # variable which holds the 9x9 board
        self.box_length = int(math.sqrt(self.row_length))
        # box size will always be 3x3 since row_length is stored at 9x9

    def get_board(self):  # function which updates and fetched current board, also can print it
        return self.board  # returns it if you would like to print it

    def valid_in_row(self, row, num):  # determines if the parameter num is anywhere in the parameter row, rows
        # represent which sublist
        for j in range(len(self.board[0])):  # loop which lets us go through different sub lists
            if self.board[row][j] == num:  # if any specific index equals the num parameter, return False
                return False  # means the num is not valid in this spot
        return True  # 1/3 of parts proving num is valid in this spot

    def valid_in_col(self, col, num):  # determines if the parameter num is anywhere in the parameter col, cols
        # represent a specific index of every list
        for i in range(len(self.board)):  # goes through every sub lists selected index
            if self.board[i][col] == num:  # if any of the col equals the num parameter, return False
                return False  # means the num is not valid in this spot
        return True  # 2/3 of parts proving num is valid in this spot

    def valid_in_box(self, row_start, col_start, num):  # determines if the parameter num is valid in the correct
        # 3x3 box
        for j in range(row_start, row_start + 3):  # goes through the first box rows and then iterates 2nd and 3rd
            for i in range(col_start, col_start + 3):  # goes through the first box cols and then iterates 2nd and 3rd
                if self.board[j][i] == num:  # if any number in the box equals the num parameter, Return False
                    return False  # means the num is not valid in this spot
        return True  # 3/3 of parts proving num is valid in this spot

    def is_valid(self, row, col, num):  # function used to test if parameter num satisfies all requirements of validity
        # at the parameter row and col
        a = self.valid_in_row(row, num)  # calls valid_in_row to test row validity
        b = self.valid_in_col(col, num)  # calls valid_in_col to test col validity
        if row < 3:  # allows you to iterate at the start of the box you're currently in
            row_start = 0  # the 0 row index is the start of the three boxes in the top row
        elif row < 6:  # allows you to iterate at the start of the box you're currently in
            row_start = 3  # the 3 row index is the start of the three boxes in the middle row
        else:  # allows you to iterate at the start of the box you're currently in
            row_start = 6  # the 6 row index is the start of the three boxes in the bottom row
        if col < 3:  # allows you to iterate at the start of the box you're currently in
            col_start = 0  # the 0 col index is the start of the three boxes in the left row
        elif col < 6:  # allows you to iterate at the start of the box you're currently in
            col_start = 3  # the 3 col index is the start of the three boxes in the middle row
        else:  # allows you to iterate at the start of the box you're currently in
            col_start = 6  # the 6 col index is the start of the three boxes in the right row
        c = self.valid_in_box(row_start, col_start, num)  # calls valid_in_box with the starting box indexes
        if a and b and c:  # if all functions return true, then return True
            return True  # means the number is completely valid in this place on the board
        else:  # if even one of the functions return false, then return False
            return False  # means the number is not valid in this place on the board

    def fill_box(self, row_start, col_start):  # function which allows random, non-repeating numbers to be placed in the
        # boxes along the diagonals of the board
        rand_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list which removed numbers after they are randomly selected so that,
        # they can't reappear.
        for j in range(row_start, row_start + 3):  # allows us to iterate through rows the parameter row_start defines
            for i in range(col_start, col_start + 3):  # allows us to iterate indexes of the sub lists the parameter
                # col_start defines
                rand_num = random.choice(rand_list)  # randomly selects a number from the rand_list
                rand_list.remove(rand_num)  # removes number selected above from rand_list
                self.board[j][i] = rand_num  # changes the board specific row and col to equal the number selected above
        return self.board  # returns/changes the board and allows it to be re-printed if called

    def fill_diagonal(self):  # calls fill_box to the fill the boxes along the diagonal
        self.fill_box(0, 0)  # fills top left 3x3 box
        self.fill_box(3, 3)  # fills dead center 3x3 box
        self.fill_box(6, 6)  # fills bottom right 3x3 box

    def fill_remaining(self, row, col):  # provided function
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # provided function
        self.fill_diagonal()  # calls fill_diagonal function
        self.fill_remaining(0, self.box_length)  # calls fill_remaining function

    def remove_cells(self):  # function used to remove cells based on difficulty level
        count = 0  # counter representing how many cells have been removed
        while count < self.removed_cells:  # if counter exceeds the difficulty value of removed cells
            rand1 = random.randint(0, 8)  # allows us to randomly select a row (sublist)
            rand2 = random.randint(0, 8)  # allows us to randomly select a col (index in sublist)
            if self.board[rand1][rand2] != 0:  # whichever row and index are selected, if value is not zero, remove cell
                self.board[rand1][rand2] = 0  # sets selected row and index value equal to zero
                count += 1  # if a cell is successfully removed, increment the counter by one


def generate_sudoku(size, removed):  # provided function
    sudoku = SudokuGenerator(size, removed)  # generates board using class SudokuGenerator constructor
    sudoku.fill_values()  # calls fill_values to fill board entirely
    board = sudoku.get_board()  # retrieves board representing a filled out Sudoku puzzle (possible solution)
    sudoku.remove_cells()  # calls remove_cells to remove a set number of cells based on selected difficulty
    board = sudoku.get_board()  # retrieves board representing a puzzle that is solvable at specific difficulty
    return board  # returns the board allowing it to be printed if called
