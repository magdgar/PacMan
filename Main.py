import ctypes
import os

import pygame

import objects.pacman

import gameloop.gameloop


user32 = ctypes.windll.user32
WIDTH = (int(user32.GetSystemMetrics(0) / 2))
HEIGHT = (int(user32.GetSystemMetrics(1) / 2))
pos_x = WIDTH/4
pos_y = HEIGHT/4
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (pos_x, pos_y)
BGCOLOR = (0, 0, 0)
pygame.init()
pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode(WIDTH, HEIGHT, 0, 32)

pac_man = objects.pacman.PacMan(100, 100)
game_loop = gameloop.gameloop.GameLoop(window_surface, pac_man)
mainClock = pygame.time.Clock()

while True:
    window_surface.fill(BGCOLOR)
    game_loop.move_pac_man(pygame.event.get())
    pygame.display.update()
    mainClock.tick(30)