import ctypes

import pygame
from pygame.rect import Rect
from objects.inky import Inky

from objects.pacman import PacMan
from objects.blinky import Blinky
from objects.clyde import Clyde
import gameloop.gameloop
import background.background
import game_engine.gameengine
from objects.pinky import Pinky
import painter.painter

user32 = ctypes.windll.user32
WIDTH = 560
HEIGHT = 580
pygame.init()
pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pac_man = PacMan(13, 21)
blinky = Blinky(13, 11)
pinky = Pinky(15, 14)
inky = Inky(21, 20)
clyde = Clyde(2, 1)
painter = painter.painter.Painter(window_surface)
game_engine = game_engine.gameengine.GameEngine(window_surface)
game_loop = gameloop.gameloop.GameLoop(window_surface, game_engine)
mainClock = pygame.time.Clock()
background.background.paint_whole_background(window_surface)
pygame.display.update()
# pygame.image.save(window_surface, "resources/screenshot_dot.jpeg")


while True:
    game_loop.perform_one_cycle(pygame.event.get())
    mainClock.tick(60)
