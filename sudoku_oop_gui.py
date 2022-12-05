from sudoku_gui import *
from constants import *
from sudoku_generator import *
import pygame


class Cell:
    # val is 1 - 9
    def __init__(self, value, row, col, width, height, screen):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.screen = screen

    def set_cell_value(self, val):
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

class Board:
    def __init__(self, rows, cols, width, height, screen):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height= height
        self.board = self.get_board()
        self.cells = [
            [Cell(self.board[i][j], i, j, SQUARE_SIZE, SQUARE_SIZE) for j in range(cols)] for i in range(rows)]
        self.screen = screen

    def draw_grid(self):
        screen.fill(BG_COLOR)
        opt_font = pygame.font.Font(None, 20)

        for line in range(0, BOARD_ROWS + 1):
            if line % 3 == 0:
                thick = 6
            else:
                thick = 1.5

            pygame.draw.line(screen, LINE_COLOR, (0, line * SQUARE_SIZE), (WIDTH, line * SQUARE_SIZE), int(thick))

        for line in range(0, BOARD_COLS + 1):
            if line % 3 == 0:
                thick = 6
            else:
                thick = 1.5

            pygame.draw.line(screen, LINE_COLOR, (line * SQUARE_SIZE, 0), (line * SQUARE_SIZE, HEIGHT - 79), int(thick))

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)

        reset_text = opt_font.render('RESET', 0, (255, 255, 255))
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 30, reset_text.get_size()[1] + 30))
        reset_surface.fill(BUTTON_COLOR)
        reset_surface.blit(reset_text, (15, 15))
        reset_rectangle = reset_surface.get_rect(
            center=(WIDTH // 2 - 175, HEIGHT // 2 + 350.1))
        screen.blit(reset_surface, reset_rectangle)

        restart_text = opt_font.render('RESTART', 0, (255, 255, 255))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 30, restart_text.get_size()[1] + 30))
        restart_surface.fill(BUTTON_COLOR)
        restart_surface.blit(restart_text, (15, 15))
        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 350.1))

        screen.blit(restart_surface, restart_rectangle)

        exit_text = opt_font.render('EXIT', 0, (255, 255, 255))

        exit_surface = pygame.Surface((exit_text.get_size()[0] + 30, exit_text.get_size()[1] + 30))
        exit_surface.fill(BUTTON_COLOR)
        exit_surface.blit(exit_text, (15, 15))

        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2 + 175, HEIGHT // 2 + 350.1))

        screen.blit(exit_surface, exit_rectangle)

        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_rectangle.collidepoint(event.pos):
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rectangle.collidepoint(event.pos):
                        return draw_game_start(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_rectangle.collidepoint(event.pos):
                        return draw_grid()
            pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)
    board = generate_sudoku(9, 30)
    num = Cell('9', 2, 2, SQUARE_SIZE, SQUARE_SIZE, draw_grid())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()