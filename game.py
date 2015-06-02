import pygame
import sys
from background import background
from background.background import paint_whole_background
from events.eventhandler import add_event
from events.eventobserver import EventObserver
from game_engine.gameengine import GameEngine
from gameloop.gameloop import GameLoop
from gamestate.gamestate import GameState
from objects.blinky import Blinky
from objects.clyde import Clyde
from objects.Container import del_objects
from objects.pacman import PacMan
from objects.pinky import Pinky
from objects.inky import Inky

class Game(EventObserver):
    def __init__(self, window_surface):
        super().__init__()
        self.react_cases = {"RESPAWN" : self.respawn, "GAMEOVER" : self.delete_ghost, "EXIT" : self.exit}
        self.game_on = True
        self.window_surface = window_surface
        self.paused = False
        self.game_state = GameState()
        self.game_loop = GameLoop(window_surface, GameEngine(window_surface), self)
        self.mainClock = pygame.time.Clock()

        reset_objects()
        self.start_game()

    def start_game(self):
        while self.game_on:
           self.game_loop.perform_one_cycle(pygame.event.get())
           self.mainClock.tick(60)

    def respawn(self):
        if self.game_state.lives_left != 0:
            reset_objects()
            add_event("REPAINT")

    def delete_ghost(self):
        del_objects()

    def exit(self):
        self.game_on = False

def reset_objects():
    del_objects()
    PacMan(2, 1)
    Blinky(13, 11)
    Pinky(11, 13)
    Inky(13, 13)
    Clyde(15, 13)

