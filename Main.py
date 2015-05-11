import ctypes

import pygame

import objects.pacman
import gameloop.gameloop
import background.background
import game_engine.game_engine
import painter.painter
from objects.Container import *

user32 = ctypes.windll.user32
WIDTH = 1000
HEIGHT = 600

pygame.init()
pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pac_man = objects.pacman.PacMan(16, 16)
add_object(pac_man)
painter = painter.painter.Painter(window_surface)
game_engine = game_engine.game_engine.GameEngine(window_surface)
game_loop = gameloop.gameloop.GameLoop(window_surface, game_engine)
mainClock = pygame.time.Clock()
background.background.paint_whole_background(window_surface)
pygame.display.update()
pygame.image.save(window_surface, "media/screenshot.jpeg")

while True:
    game_loop.perform_one_cycle(pygame.event.get())
    mainClock.tick(30)
