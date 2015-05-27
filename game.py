import pygame
from background import background
from background.background import paint_whole_background
from events.eventobserver import EventObserver
from game_engine.gameengine import GameEngine
from gameloop.gameloop import GameLoop
from gamestate.gamestate import GameState
from objects.blinky import Blinky
from objects.clyde import Clyde
from objects.Container import del_objects
from objects.pacman import PacMan
from objects.pinky import Pinky
from painter.painter import Painter
with open("resources/map.txt") as file:
    array2d = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]

class Game(EventObserver):
    def __init__(self, window_surface):
        super().__init__()
        self.react_cases = {"RESPAWN" : self.respawn}
        self.window_surface = window_surface
        reset_objects()
        self.paused = False
        self.game_state = GameState()
        self.game_loop = GameLoop(window_surface, GameEngine(window_surface), self)
        self.mainClock = pygame.time.Clock()
        self.start_game()

    def start_game(self):
        while not self.game_state.lives_left == 0:
           self.game_loop.perform_one_cycle(pygame.event.get())
           self.mainClock.tick(60)

    def respawn(self):
        reset_objects()

def reset_objects():
    del_objects()
    PacMan(1, 1)
    Blinky(11, 13)
    Pinky(13, 13)
    Clyde(16, 13)

