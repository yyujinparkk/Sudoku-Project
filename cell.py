from constants import *
import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def draw(self, screen):
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
        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.col * int(SQUARE_SIZE), self.row * int(SQUARE_SIZE), int(SQUARE_SIZE), int(SQUARE_SIZE)), 3)
            self.selected = False
        if self.value == 1:
            num_1_rect = num_1_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_1_surf, num_1_rect)
        elif self.value == 2:
            num_2_rect = num_2_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_2_surf, num_2_rect)
        elif self.value == 3:
            num_3_rect = num_3_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_3_surf, num_3_rect)
        elif self.value == 4:
            num_4_rect = num_4_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_4_surf, num_4_rect)
        elif self.value == 5:
            num_5_rect = num_5_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_5_surf, num_5_rect)
        elif self.value == 6:
            num_6_rect = num_6_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_6_surf, num_6_rect)
        elif self.value == 7:
            num_7_rect = num_7_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_7_surf, num_7_rect)
        elif self.value == 8:
            num_8_rect = num_8_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_8_surf, num_8_rect)
        elif self.value == 9:
            num_9_rect = num_9_surf.get_rect(center=(int(SQUARE_SIZE) * self.col + SQUARE_SIZE // 2, int(SQUARE_SIZE) * self.row + SQUARE_SIZE // 2))
            screen.blit(num_9_surf, num_9_rect)
