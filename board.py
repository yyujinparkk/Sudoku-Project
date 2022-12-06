from constants import *
from cell import Cell
from sudoku_generator import *
import pygame
import sys


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.removed = 0
        self.reset_rectangle = None
        self.restart_rectangle = None
        self.exit_rectangle = None
        self.cells = []
        match difficulty:
            case "easy":
                self.removed = 30
            case "medium":
                self.removed = 40
            case "hard":
                self.removed = 50

        self.sudoku = SudokuGenerator(9, self.removed)
        self.sudoku.fill_values()
        self.sudoku.remove_cells()
        self.board = self.sudoku.get_board()

        for row in range(9):
            self.cells.append([])# need to be able to make list of cell objects
            for col in range(9):
                self.cells[row].append(Cell(self.board[row][col], row, col, screen))

    def draw(self):
        self.screen.fill(BG_COLOR)
        num_font = pygame.font.Font(None, 40)
        for line in range(0, BOARD_ROWS + 1):
            if line % 3 == 0:
                thick = 6
            else:
                thick = 1.5

            pygame.draw.line(self.screen, LINE_COLOR, (0, line * SQUARE_SIZE), (WIDTH, line * SQUARE_SIZE), int(thick))

        for line in range(0, BOARD_COLS + 1):
            if line % 3 == 0:
                thick = 6
            else:
                thick = 1.5

            pygame.draw.line(self.screen, LINE_COLOR, (line * SQUARE_SIZE, 0), (line * SQUARE_SIZE, HEIGHT - 79), int(thick))

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                cell = Cell(self.board[row][col], row, col, self.screen)
                cell.draw(self.screen)

        reset_text = num_font.render('RESET', 0, (255, 255, 255))
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 30, reset_text.get_size()[1] + 30))
        reset_surface.fill(BUTTON_COLOR)
        reset_surface.blit(reset_text, (15, 15))
        self.reset_rectangle = reset_surface.get_rect(
            center=(WIDTH // 2 - 175, HEIGHT // 2 + 350.1))
        self.screen.blit(reset_surface, self.reset_rectangle)

        restart_text = num_font.render('RESTART', 0, (255, 255, 255))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 30, restart_text.get_size()[1] + 30))
        restart_surface.fill(BUTTON_COLOR)
        restart_surface.blit(restart_text, (15, 15))
        self.restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 350.1))

        self.screen.blit(restart_surface, self.restart_rectangle)

        exit_text = num_font.render('EXIT', 0, (255, 255, 255))

        exit_surface = pygame.Surface((exit_text.get_size()[0] + 30, exit_text.get_size()[1] + 30))
        exit_surface.fill(BUTTON_COLOR)
        exit_surface.blit(exit_text, (15, 15))

        self.exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2 + 175, HEIGHT // 2 + 350.1))

        self.screen.blit(exit_surface, self.exit_rectangle)

    def select_cell(self, row, col, value):  # Outlines
        self.board[row][col] = value
        self.update_cells()
        cell = self.cells[row][col]
        cell.selected = True

    def get_value(self, row, col):
        cell = self.cells[row][col]
        a = Cell.get_value(cell)
        return a

    def update_cells(self):
        self.cells = [
            [Cell(self.board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)
        ]

    def check_board(self, row, col, num):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    if SudokuGenerator.is_valid(self.board, row, col, num):
                        return True
                    else:
                        return False
                else:
                    return

    def is_full(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j])
                if self.board[i][j] == 0:
                    return False
                else:
                    return True


if __name__ == "__main__":
    pygame.init()  # Initializes pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Screen variable dimensions (how big is window)
    num_font = pygame.font.Font(None, 40)  # Font for numbers
    pygame.display.set_caption("Sudoku")  # Title of window
    board = Board(WIDTH, HEIGHT, screen, "hard")  # Initializes a board at the moment
    board.draw()  # draws board

    board.select_cell(5, 5, 5)
    board.check_board(4, 4, 5)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.reset_rectangle.collidepoint(event.pos):
                    screen.fill(BG_COLOR)
                    board = Board(WIDTH, HEIGHT, screen, "easy")
                    board.draw()
                    pygame.display.update()
                if board.restart_rectangle.collidepoint(event.pos):
                    pass
                if board.exit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

