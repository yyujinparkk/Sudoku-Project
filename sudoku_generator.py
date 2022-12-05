import math
import random

class SudokuGenerator:

    def __init__(self, row_length, removed_cells):  # Initializes row_length, removed_cells, the board, and box_length
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(self.row_length)] for j in range(self.row_length)]  # Creates a 2D list of 0s
        self.box_length = int(math.sqrt(self.row_length))  # Converts the square root float value into an integer

    def get_board(self):  # Returns the board which is a 2D list of numbers
        return self.board

    def print_board(self):  # Prints the board out by iterating through the whole list then sub-lists
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()
        return

    def valid_in_row(self, row, num):  # Iterates through each index of the given sublist checking if num appears
        for j in range(len(self.board[0])):
            if self.board[row][j] == num:
                return False
        return True

    def valid_in_col(self, col, num):  # Iterates through all sub-lists checking if num appears in the given index
        for i in range(len(self.board)):
            if self.board[i][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):  # Checks indexes of given row/column to end of box for num
        for j in range(row_start, row_start + 3):
            for i in range(col_start, col_start + 3):
                if self.board[j][i] == num:
                    return False
        return True

    def is_valid(self, row, col, num):  # valid_in_row() valid_in_col() and valid_in_box() to check if an input is valid
        a = self.valid_in_row(row, num)
        b = self.valid_in_col(col, num)
        if row < 3:  # Based on given row determines where row_start will be for valid_in_box()
            row_start = 0
        elif row < 6:
            row_start = 3
        else:
            row_start = 6

        if col < 3:  # Based on given col determines where col_start will be for valid_in_box()
            col_start = 0
        elif col < 6:
            col_start = 3
        else:
            col_start = 6

        c = self.valid_in_box(row_start, col_start, num)
        if a and b and c:  # Checks all 3 functions stored a, b, and c if all return True function returns True
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):  # Uses a list of numbers from 1-9 to check whether the num has been used
        rand_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(row_start, row_start + 3):
            for i in range(col_start, col_start + 3):  # Iterates through 2D list and sub-lists
                rand_num = random.choice(rand_list)  # Makes a random choice from rand_list
                rand_list.remove(rand_num)  # Removes whatever selection from rand_list was made, so it cannot be reused
                self.board[j][i] = rand_num  # Replaces position in board with the given number selected
        return self.board

    def fill_diagonal(self):  # Calls the fill_box() method at the correct indexes to fill the boxes along diagonal
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):  # Given function that fills remaining values of board after diagonal filled
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

    def fill_values(self):  # Given function that calls both fill_diagonal() and fill_remaining()
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):  # Uses a counter to determine when the correct number of cells has been removed
        count = 0
        while count < self.removed_cells:  # While the loop is True randomly generates positions within the board
            rand1 = random.randint(0, 8)
            rand2 = random.randint(0, 8)
            if self.board[rand1][rand2] != 0:  # If selected position is not 0 will make it 0 and add to counter
                self.board[rand1][rand2] = 0
                count += 1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

