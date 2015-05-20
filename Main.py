import ctypes

import pygame
from pygame.rect import Rect

from objects.pacman import PacMan
from objects.blinky import Blinky
import gameloop.gameloop
import background.background
import game_engine.gameengine
import painter.painter

user32 = ctypes.windll.user32
WIDTH = 1000
HEIGHT = 600
pygame.init()
pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pac_man = PacMan(37, 17)
blinky = Blinky(417, 397)
painter = painter.painter.Painter(window_surface)
game_engine = game_engine.gameengine.GameEngine(window_surface)
game_loop = gameloop.gameloop.GameLoop(window_surface, game_engine)
mainClock = pygame.time.Clock()
background.background.paint_whole_background(window_surface)
pygame.display.update()
# pygame.image.save(window_surface, "resources/screenshot_dot.jpeg")
print([item for sublist in [[1], [1, 2, 3]] for item in sublist])
print(Rect(100, 100, 20, 20).contains(105, 105, 10, 10))
while True:
    game_loop.perform_one_cycle(pygame.event.get())
    mainClock.tick(60)
