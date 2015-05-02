import ctypes

from gameloop.mapgameloop import *


user32 = ctypes.windll.user32
WIDTH = 1000
HEIGHT = 600
BGCOLOR = (0, 0, 0)
pygame.init()
pygame.display.set_caption('Pac Man!')

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

game_loop = GameLoop(window_surface)
mainClock = pygame.time.Clock()

while True:
    game_loop.handle_map_event(pygame.event.get())
    pygame.display.update()
    mainClock.tick(20)
