import pygame
from sudoku_generator import *
from board import *
from cell import *
from constants import *


def draw_game_start(screen):
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

    Board.easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 175, HEIGHT // 2 + 100))
    Board.medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    Board.hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 175, HEIGHT // 2 + 100))

    # draw button
    screen.blit(easy_surface, Board.easy_rectangle)
    screen.blit(medium_surface, Board.medium_rectangle)
    screen.blit(hard_surface, Board.hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Board.easy_rectangle.collidepoint(event.pos):
                    mode = "easy"
                    return mode
                if Board.medium_rectangle.collidepoint(event.pos):
                    mode = "medium"
                    return mode
                if Board.hard_rectangle.collidepoint(event.pos):
                    mode = "hard"
                    return mode
        pygame.display.update()


def draw_game_won(screen):
    result_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    screen.fill(BG_COLOR)

    win_surface = result_font.render('Game Won!', 0, LINE_COLOR)
    win_rect = win_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 210))
    screen.blit(win_surface, win_rect)

    exit_text = button_font.render('EXIT', 0, (255, 255, 255))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 40, exit_text.get_size()[1] + 40))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (20, 20))

    Board.exit_rect = exit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))

    # draw button
    screen.blit(exit_surface, Board.exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Board.exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def draw_game_lost(screen):
    result_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    screen.fill(BG_COLOR)

    over_surface = result_font.render('Game Over :(', 0, LINE_COLOR)
    over_rect = over_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 210))
    screen.blit(over_surface, over_rect)

    over_text = button_font.render('RESTART', 0, (255, 255, 255))

    over_surface = pygame.Surface((over_text.get_size()[0] + 40, over_text.get_size()[1] + 40))
    over_surface.fill(BUTTON_COLOR)
    over_surface.blit(over_text, (20, 20))

    Board.over_rect = over_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))

    # draw button
    screen.blit(over_surface, Board.over_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Board.over_rect.collidepoint(event.pos):
                    main()
        pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    mode = draw_game_start(screen)
    num_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)
    board = Board(WIDTH, HEIGHT, screen, mode)
    board.draw()
    pygame.display.update()

    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = x // int(SQUARE_SIZE)
                col = y // int(SQUARE_SIZE)
                if count < 1:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(row * int(SQUARE_SIZE), col * int(SQUARE_SIZE), int(SQUARE_SIZE), int(SQUARE_SIZE)), 3)
                    count += 1
                if board.reset_rectangle.collidepoint(event.pos):
                    screen.fill(BG_COLOR)
                    board = Board(WIDTH, HEIGHT, screen, mode)
                    board.draw()
                    pygame.display.update()
                if board.restart_rectangle.collidepoint(event.pos):
                    main()
                if board.exit_rectangle.collidepoint(event.pos):
                    sys.exit()
            pygame.display.update()
            if event.type == pygame.KEYDOWN:  # Should not be able to select a cell with a num already
                if event.key == pygame.K_1:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 1
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                elif event.key == pygame.K_2:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 2
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                elif event.key == pygame.K_3:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 3
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                elif event.key == pygame.K_4:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 4
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                elif event.key == pygame.K_5:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 5
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                elif event.key == pygame.K_6:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 6
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                elif event.key == pygame.K_7:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 7
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                elif event.key == pygame.K_8:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 8
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                elif event.key == pygame.K_9:
                    if board.can_place(col, row):  # Switched col and row now test
                        value = 9
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                if event.key == pygame.K_BACKSPACE:  # Switched col and row now test
                        value = 0
                        board.select_cell(col, row, value)
                        screen.fill(BG_COLOR)
                        board.draw()
                        pygame.display.update()
                count = 0
                if event.key == pygame.K_RETURN:
                    if Board.check_board(board, row, col, range(1, 10)):
                        draw_game_won(screen)
                        pygame.display.update()
                    else:
                        draw_game_lost(screen)
                        pygame.display.update()
        pygame.display.update()


if __name__ == "__main__":
    main()
