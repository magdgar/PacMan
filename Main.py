import ctypes
import pygame
from pygame.constants import K_UP
from game import Game

from objects.pacman import PacMan
from objects.blinky import Blinky
from objects.clyde import Clyde
import gameloop.gameloop
import background.background
import game_engine.gameengine
from objects.pinky import Pinky
from pacfunctions.pacfunction import negative_direction
import painter.painter

user32 = ctypes.windll.user32
WIDTH = 560
HEIGHT = 580

pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

# pygame.image.save(window_surface, "resources/screenshot_dot.jpeg")
negative_direction(K_UP)
Game(window_surface)
