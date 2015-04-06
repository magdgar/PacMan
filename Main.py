import sys

import pygame
from pygame.locals import *

import objects.pacman


pygame.init()

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Pac Man!')
pac_man = objects.pacman.PacMan(100, 100)
mainClock = pygame.time.Clock()
BGCOLOR = (0, 0, 0)

right = False
buttons = 0
while True:

    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            buttons += 1
            if event.key == K_UP:
                direction = UP
            elif event.key == K_RIGHT:
                direction = RIGHT
            elif event.key == K_DOWN:
                direction = DOWN
            elif event.key == K_LEFT:
                direction = LEFT
        elif event.type == KEYUP:
            buttons -= 1

    if buttons > 0:
        if direction == UP:
            pac_man.move(0, -5)
            pac_man.paint(windowSurface, 0)
        elif direction == RIGHT:
            pac_man.move(5, 0)
            pac_man.paint(windowSurface, 1)
        elif direction == DOWN:
            pac_man.move(0, 5)
            pac_man.paint(windowSurface, 2)
        elif direction == LEFT:
            pac_man.move(-5, 0)
            pac_man.paint(windowSurface, 3)
    else:
        pac_man.paint(windowSurface, 1)

    pygame.display.update()
    mainClock.tick(30)