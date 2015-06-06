import ctypes
import pygame
from game import Game, ServerGame, ClientGame

user32 = ctypes.windll.user32
WIDTH = 600
HEIGHT = 650

pygame.display.set_caption('Pac Man!')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

if __name__ == "__main__":
    GAME = Game(window_surface).start_game()

