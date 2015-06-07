"""responsible for game logic"""


from pygame.rect import Rect
from media.dirtyrect import  PacDirtyRect
from objects.Container import *
from media.constans import ACTUAL_LVL

with open(ACTUAL_LVL) as file:
    BG_MATRIX = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]

class GameEngine:
    """class responsible for invoking low-level logic"""
    def __init__(self, window_surface, coinainer, painter):
        self.window_surface = window_surface
        self.cointainer = coinainer
        self.painter = painter

    def simulate_world(self, key_events):
        """responsible for invoking logic each frame"""
        if self.cointainer.pac_man is not None:
            self.cointainer.pac_man.move_hero(key_events[0])
            self.painter.add_dirty_rect(PacDirtyRect(Rect(self.cointainer.pac_man.x - 2, self.cointainer.pac_man.y - 2, 30, 30), self.cointainer.pac_man.is_dot))
        if  self.cointainer.enemy_pac_man is not None:
            self.cointainer.enemy_pac_man.move_hero(key_events[1])
            self.painter.add_dirty_rect(PacDirtyRect(Rect(self.cointainer.enemy_pac_man.x - 2, self.cointainer.enemy_pac_man.y - 2, 30, 30), self.cointainer.enemy_pac_man.is_dot))

        for ghost in self.cointainer.ghosts:
            if ghost.active:
                ghost.move_hero(key_events)
            self.painter.add_dirty_rect(PacDirtyRect(Rect(ghost.x - 2, ghost.y - 2, 30, 30), ghost.is_dot))



