import ctypes
import pygame
from events.eventhandler import EventHandler
from game import Game, ServerGame, ClientGame, EnemyGame
from game_start import GameStart
from objects.Container import Container

WIDTH = 600
HEIGHT = 650

pygame.display.set_caption('Pac Man!')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

if __name__ == "__main__":
    container = Container()
    event_handler = EventHandler(container)
    GameStart(window_surface, container, event_handler).display_start_screen()
