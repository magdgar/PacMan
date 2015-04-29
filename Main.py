import ctypes
import os

import pygame

import objects.pacman
import objects.dot
import gameloop.gameloop
import background.background
from media.dirtyrect import *


user32 = ctypes.windll.user32
WIDTH = 1000
HEIGHT = 600
pos_x = WIDTH/2
pos_y = HEIGHT/2
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (pos_x, pos_y)
BGCOLOR = (0, 0, 0)
pygame.init()
pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

#pac_man = objects.pacman.PacMan(100, 100)
pac_man = objects.pacman.PacMan(4, 4)
game_loop = gameloop.gameloop.GameLoop(window_surface, pac_man)
mainClock = pygame.time.Clock()
background.background.paint_whole_background(window_surface)
pygame.display.update()
pygame.image.save(window_surface, "media/screenshot.jpeg")
while True:
    window_surface.fill(BGCOLOR)
    game_loop.move_pac_man(pygame.event.get())
    pygame.display.update(DIRTY_RECT)
    clear_dirty_rect()
    mainClock.tick(30)
