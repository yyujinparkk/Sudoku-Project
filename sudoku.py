import pygame
from constants import *
from sudoku_generator import *

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
num_font = pygame.font.Font(None, 40)  # Need an effective font size
game_over_font = pygame.font.Font(None, 40
                                  )
board = generate_sudoku(9, 50)  # Need to be variable implemented somehow for different difficulties


#  Vid one for draw_grid and draw_nums

def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * int(SQUARE_SIZE)),
            (WIDTH, i * int(SQUARE_SIZE)),
            int(LINE_WIDTH)
        )

    for j in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (j * int(SQUARE_SIZE), 0),
            (j * int(SQUARE_SIZE), HEIGHT),
            int(LINE_WIDTH)
        )  #


def draw_nums():
    num_1_surf = num_font.render("1", 0, CROSS_COLOR)  # Surf is surface to draw, rect is location
    num_2_surf = num_font.render("2", 0, CROSS_COLOR)  # Deleted all rect and make below may cause issue not sure
    num_3_surf = num_font.render("3", 0, CROSS_COLOR)
    num_4_surf = num_font.render("4", 0, CROSS_COLOR)
    num_5_surf = num_font.render("5", 0, CROSS_COLOR)
    num_6_surf = num_font.render("6", 0, CROSS_COLOR)
    num_7_surf = num_font.render("7", 0, CROSS_COLOR)
    num_8_surf = num_font.render("8", 0, CROSS_COLOR)
    num_9_surf = num_font.render("9", 0, CROSS_COLOR)

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                num_1_rect = num_1_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_1_surf, num_1_rect)
            elif board[row][col] == 2:
                num_2_rect = num_2_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_2_surf, num_2_rect)
            elif board[row][col] == 3:
                num_3_rect = num_3_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_3_surf, num_3_rect)
            elif board[row][col] == 4:
                num_4_rect = num_4_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_4_surf, num_4_rect)
            elif board[row][col] == 5:
                num_5_rect = num_5_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_5_surf, num_5_rect)
            elif board[row][col] == 6:
                num_6_rect = num_6_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_6_surf, num_6_rect)
            elif board[row][col] == 7:
                num_7_rect = num_7_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_7_surf, num_7_rect)
            elif board[row][col] == 8:
                num_8_rect = num_8_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_8_surf, num_8_rect)
            elif board[row][col] == 9:
                num_9_rect = num_9_surf.get_rect(center=(int(SQUARE_SIZE) * col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * row + SQUARE_SIZE // 2))
                screen.blit(num_9_surf, num_9_rect)


def draw_game_over():
    screen.fill(BG_COLOR)
    if board == board:
        end_text = f"Game Won!"
    else:
        end_text = f"Game Over :("
    end_surf = game_over_font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_surf, end_rect)
    #  Implement button creation and make restart game in event loop (vid 3)

screen.fill(BG_COLOR)
draw_grid()
draw_nums()

game_over = False  # Used when checking if solution matches filled board by player if True will display game over screen
while True:
    for event in pygame.event.get(): # Event loop for the different pygame events like key presses
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # Possibly something like game_over will equal True or False is the solution matches the board once they fill it out
            x, y = event.pos
            row = y // int(SQUARE_SIZE)
            col = x // int(SQUARE_SIZE)
            if board[row][col] == 0:  # Believe this sections will be redone for each num 1-9
                if event.type == pygame.KEYDOWN:  # Belive using cell or board class will be able to draw the num in specific cell
                    if event.key == pygame.K_1:
                        board[row][col] = 1
                        draw_nums()
                        #  Draw nums will have to go here as well because the board needs to be updated (vid 2 for this stuff)

    if game_over:
        pygame.display.update()
        pygame.time.delay(1000)  # Maybe extend length of time
        draw_game_over()
    pygame.display.update()
