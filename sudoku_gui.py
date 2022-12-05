import pygame, sys
import math
import random
from constants import *
from sudoku_generator import *
from sudoku_oop_gui import *

winner = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

board = generate_sudoku(9, 50)

def draw_game_start(screen):
    global difficulty
    # initialize title font
    welcome_font = pygame.font.Font(None, 70)
    select_font = pygame.font.Font(None, 55)
    button_font = pygame.font.Font(None, 35)
    screen.fill(BG_COLOR)

    title_surface = welcome_font.render('Welcome to Sudoku', 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 230))
    screen.blit(title_surface, title_rectangle)

    level_surface = select_font.render('Select Game Mode:', 0, LINE_COLOR)
    level_rectangle = level_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(level_surface, level_rectangle)

    easy_text = button_font.render('Easy', 0, (255, 255, 255))
    medium_text = button_font.render('Medium', 0, (255, 255, 255))
    hard_text = button_font.render('Hard', 0, (255, 255, 255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 30, easy_text.get_size()[1] + 30))
    easy_surface.fill(BUTTON_COLOR)
    easy_surface.blit(easy_text, (15, 15))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 30, medium_text.get_size()[1] + 30))
    medium_surface.fill(BUTTON_COLOR)
    medium_surface.blit(medium_text, (15, 15))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 30, hard_text.get_size()[1] + 30))
    hard_surface.fill(BUTTON_COLOR)
    hard_surface.blit(hard_text, (15, 15))

    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 175, HEIGHT // 2 + 100))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 175, HEIGHT // 2 + 100))

    # draw button
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                # Checks if mouse is on easy button
                    return draw_grid(), draw_nums() # if mouse is on easy button, return to main
            if event.type == pygame.MOUSEBUTTONDOWN:
                if medium_rectangle.collidepoint(event.pos):
                    return draw_grid(), draw_nums()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hard_rectangle.collidepoint(event.pos):
                    return draw_grid(), draw_nums()
        pygame.display.update()


def draw_grid():
    # draw horizontal line
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

def draw_nums():
    num_font = pygame.font.Font(None, 40)
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


def main():
    screen.fill(BG_COLOR)
    draw_game_start(screen)
    draw_grid()
    draw_nums()
    game_over = False  # Used when checking if solution matches filled board by player if True will display game over screen
    while True:
        for event in pygame.event.get():  # Event loop for the different pygame events like key presses
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
            pygame.display.update()

if __name__ == '__main__':
    main()


