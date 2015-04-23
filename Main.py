import ctypes
import os

import pygame

import objects.pacman
import objects.dot
import gameloop.gameloop
import background.background


user32 = ctypes.windll.user32
#WIDTH = (int(user32.GetSystemMetrics(0) / 2))
#HEIGHT = (int(user32.GetSystemMetrics(1) / 2))
WIDTH = 1000
HEIGHT = 600
pos_x = WIDTH/2
pos_y = HEIGHT/2
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (pos_x, pos_y)
BGCOLOR = (0, 0, 0)
pygame.init()
pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pac_man = objects.pacman.PacMan(100, 100)
#dot = objects.dot.Dot(150, 150)
game_loop = gameloop.gameloop.GameLoop(window_surface, pac_man)
mainClock = pygame.time.Clock()

while True:
    window_surface.fill(BGCOLOR)
    background.background.paint_background(window_surface)
    #pygame.draw.circle(window_surface, (255, 224, 149), (150, 150), 4)
    #dot.paint(window_surface)
    game_loop.move_pac_man(pygame.event.get())
    pygame.display.update()
    mainClock.tick(30)
