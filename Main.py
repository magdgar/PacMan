import ctypes

import pygame

import objects.pacman
import objects.dot
import gameloop.gameloop
import background.background
from media.dirtyrect import *
import game_engine.game_engine

user32 = ctypes.windll.user32
WIDTH = 1000
HEIGHT = 600
BGCOLOR = (0, 0, 0)

pygame.init()
pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pac_man = objects.pacman.PacMan(16, 16)
game_engine = game_engine.game_engine.GameEngine(window_surface, pac_man)
game_loop = gameloop.gameloop.GameLoop(window_surface, game_engine)
mainClock = pygame.time.Clock()
background.background.paint_whole_background(window_surface)
pygame.display.update()
pygame.image.save(window_surface, "media/screenshot.jpeg")

while True:
    game_loop.perform_one_cycle(pygame.event.get())
    mainClock.tick(30)
