import pygame

horizontal_wall = pygame.image.load('media/1.png')
vertical_wall = pygame.image.load('media/2.png')
up_right_wall = pygame.image.load('media/3.png')
right_down_corner = pygame.image.load('media/4.png')
left_down_corner = pygame.image.load('media/5.png')
up_left_corner = pygame.image.load('media/6.png')

with open("background/level1.txt") as f:
    lines = f.readlines()

walls_dict = {1: horizontal_wall, 2: vertical_wall, 3: up_right_wall,
              4: right_down_corner, 5: left_down_corner, 6: up_left_corner}


def paint_background(window_surface):
    y = 0
    for line in lines:
        x = 0
        for char in line:
            dict_walue = ord(char) - 48
            if 0 < dict_walue < 7:
                window_surface.blit(walls_dict[dict_walue], (x, y))
            x += 20
        y += 20
