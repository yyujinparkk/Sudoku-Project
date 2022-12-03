import math
import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(self.row_length)] for j in range(self.row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        print(self.board)
        return None

    def valid_in_row(self, row, num):
        row_list = row
        for i in self.board[row_list]:
            if i == num:
                return False
        return True

    def valid_in_col(self, col, num):
        col_list = col
        for row in self.board:
            if row[col_list] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        new_list = []
        n = 0
        for row in self.board:
            c = row[col_start:col_start + 3]
            new_list.append(c)
            n += 1
            for i in new_list:
                if num in i:
                    return False
            if n >= 3:
                return True

    def is_valid(self, row, col, num):
        a = SudokuGenerator.valid_in_row(self, row, num)
        b = SudokuGenerator.valid_in_col(self, col, num)
        c = SudokuGenerator.valid_in_box(self, row, col, num)
        if a and b and c:
            return True
        else:
            return False
    def fill_box(self, row_start, col_start): #Still needs to check if the random integer is in box before adding
        for j in range(row_start - 1, row_start + 2):
            for i in range(col_start - 1, col_start + 2):
                rand_num = random.randint(1, 9)
                if SudokuGenerator.valid_in_box(self, row_start, col_start, rand_num) is True:
                    self.board[j][i] = rand_num
        return self.board

    def fill_diagonal(self):
        SudokuGenerator.fill_box(self, 0, 0)
        SudokuGenerator.fill_box(self, 3, 3)
        SudokuGenerator.fill_box(self, 6, 6)
        return self.board

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
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

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        pass

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.print_board()
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

generate_sudoku(9, 1)

a = SudokuGenerator(9, 0)
print(SudokuGenerator.get_board(a))
print(SudokuGenerator.print_board(a))
num = 4
print(SudokuGenerator.valid_in_row(a, 2, 5))
print(SudokuGenerator.valid_in_col(a, 2, 3))
print(SudokuGenerator.valid_in_box(a, 3, 3, 5))
print(SudokuGenerator.is_valid(a, 3, 3, 3))
print(SudokuGenerator.fill_box(a, 5, 5))





#Check generate_soduku on github to make sure my functino matches what is there
#Find correct list comprehension to make list of 0s




