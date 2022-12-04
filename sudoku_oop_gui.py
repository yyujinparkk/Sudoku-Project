from sudoku_gui import *
from constants import *
from sudoku_generator import *
import pygame


class Cell:
    # val is 1 - 9
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def set_value(self, val):
        self.value = val

    # draws text
    def draw(self, screen):
        grid_font = pygame.font.Font(None, 30)
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                number = board[row][col]
                grid_text = grid_font.render(str(number), 1, (0, 0, 0))
                grid_surface = pygame.Surface((grid_text.get_size()[0] + 10, grid_text.get_size()[1] + 10))
                grid_surface.fill((255, 255, 255))
                grid_surface.blit(grid_text, (5, 5))
                if number != 0:
                    grid_rect = grid_surface.get_rect(center=(SQUARE_SIZE * self.col +
                                                              SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                    screen.blit(grid_surface, grid_rect)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)
    board = generate_sudoku(9, 30)
    value = 8
    num = Cell('9', 3, 2, SQUARE_SIZE, SQUARE_SIZE)

    num.draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()