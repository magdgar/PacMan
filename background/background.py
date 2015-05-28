import pygame
from media.constans import ACTUAL_LVL, ACTUAL_SCREENSCHOT, ACTUAL_DOT_SCREENSCHOT

blank_piece = pygame.image.load('resources/0.png')
horizontal_wall = pygame.image.load('resources/1.png')
vertical_wall = pygame.image.load('resources/2.png')
up_right_wall = pygame.image.load('resources/3.png')
right_down_corner = pygame.image.load('resources/4.png')
left_down_corner = pygame.image.load('resources/5.png')
up_left_corner = pygame.image.load('resources/6.png')
dot = pygame.image.load('resources/dot.png')
background_image = pygame.image.load(ACTUAL_SCREENSCHOT)
background_image_dot = pygame.image.load(ACTUAL_DOT_SCREENSCHOT)

walls_dict = {1: horizontal_wall, 2: vertical_wall, 3: up_right_wall,
              4: right_down_corner, 5: left_down_corner, 6: up_left_corner,
              7: dot, 0: blank_piece}

with open(ACTUAL_LVL) as file:
    array2d = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]


def paint_whole_background(window_surface, map_array=array2d):
    for y in range(len(map_array)):
        for x in range(len(map_array[0])):
            if 8 > map_array[y][x] >= 0:
                window_surface.fill((0, 0, 0), (x * 20, y * 20, 20, 20))
                window_surface.blit(walls_dict[map_array[y][x]], (x * 20, y * 20))


def repaint_fragment_of_background(window_surface, rect, is_dot):
    if is_dot:
        window_surface.blit(background_image_dot, rect, rect)
    else:
        window_surface.blit(background_image, rect, rect)
