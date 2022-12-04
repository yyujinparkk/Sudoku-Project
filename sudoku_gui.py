import pygame, sys
import math
import random
from constants import *
from sudoku_generator import *
from sudoku_oop_gui import *

winner = 0
game_over = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
default_grid =[
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
    ]
board = generate_sudoku(9, 30)

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
                    return draw_grid() # if mouse is on easy button, return to main
            if event.type == pygame.MOUSEBUTTONDOWN:
                if medium_rectangle.collidepoint(event.pos):
                    return draw_grid()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hard_rectangle.collidepoint(event.pos):
                    return draw_grid()
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

def main():
    draw_game_start(screen)
    draw_grid()

if __name__ == '__main__':
    main()


