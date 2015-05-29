"""logic and graphics required to handle background paining"""

import pygame
from media.constans import ACTUAL_SCREENSCHOT, ACTUAL_DOT_SCREENSCHOT, ACTUAL_LVL

# images needed to build map
BLANK_PIECE = pygame.image.load('resources/0.png')
HORIZONTAL_WALL = pygame.image.load('resources/1.png')
VERTICAL_WALL = pygame.image.load('resources/2.png')
UP_RIGHT_WALL = pygame.image.load('resources/3.png')
RIGHT_DOWN_CORNER = pygame.image.load('resources/4.png')
LEFT_DOWN_CORNER = pygame.image.load('resources/5.png')
UP_LEFT_CORNER = pygame.image.load('resources/6.png')
DOT = pygame.image.load('resources/DOT.png')
BACKGROUND_IMAGE = pygame.image.load(ACTUAL_SCREENSCHOT)
BACKGROUND_IMAGE_DOT = pygame.image.load(ACTUAL_DOT_SCREENSCHOT)

# dictionary used for painting
WALLS_DICT = {1: HORIZONTAL_WALL, 2: VERTICAL_WALL, 3: UP_RIGHT_WALL,
              4: RIGHT_DOWN_CORNER, 5: LEFT_DOWN_CORNER, 6: UP_LEFT_CORNER,
              7: DOT, 0: BLANK_PIECE}

with open(ACTUAL_LVL) as file:
    ARRAY_2D = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]


def paint_whole_background(window_surface, map_array=ARRAY_2D):
    """with given array paints background on whole window"""

    for y in range(len(map_array)):
        for x in range(len(map_array[0])):
            if 8 > map_array[y][x] >= 0:
                window_surface.fill((0, 0, 0), (x * 20, y * 20, 20, 20))
                window_surface.blit(WALLS_DICT[map_array[y][x]], (x * 20, y * 20))


def repaint_fragment_of_background(window_surface, rect, is_dot):
    """
    repaints given background area of screen if
    chooses background with dots if is_dot == True
    """
    if is_dot:
        window_surface.blit(BACKGROUND_IMAGE_DOT, rect, rect)
    else:
        window_surface.blit(BACKGROUND_IMAGE, rect, rect)
