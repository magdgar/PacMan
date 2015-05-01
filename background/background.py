import pygame

horizontal_wall = pygame.image.load('media/1.png')
vertical_wall = pygame.image.load('media/2.png')
up_right_wall = pygame.image.load('media/3.png')
right_down_corner = pygame.image.load('media/4.png')
left_down_corner = pygame.image.load('media/5.png')
up_left_corner = pygame.image.load('media/6.png')
dot = pygame.image.load('media/dot.png')
background_image = pygame.image.load('media/screenshot.jpeg')

walls_dict = {1: horizontal_wall, 2: vertical_wall, 3: up_right_wall,
              4: right_down_corner, 5: left_down_corner, 6: up_left_corner, 7: dot}


def proper_digit(number):
    if number != '\n':
        return int(number)
    else:
        return 0


with open("background/lvl2.txt") as file:
    array2d = [[proper_digit(digit) for digit in list(line)] for line in file]


def paint_whole_background(window_surface):
    for x in range(len(array2d[0])):
        for y in range(len(array2d) - 1):
            if array2d[y][x] > 0:
                window_surface.blit(walls_dict[array2d[y][x]], (x * 20, y * 20))


def paint_background(window_surface, rect):
    window_surface.blit(background_image, rect, rect)
