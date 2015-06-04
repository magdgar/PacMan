"""responsible for game logic"""


from pygame.rect import Rect
from media.dirtyrect import add_dirty_rect, PacDirtyRect
from objects.Container import *
from media.constans import ACTUAL_LVL

with open(ACTUAL_LVL) as file:
    BG_MATRIX = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]

class GameEngine:
    """class responsible for invoking low-level logic"""
    def __init__(self, window_surface):
        self.window_surface = window_surface

    @staticmethod
    def simulate_world(key_events):
        """responsible for invoking logic each frame"""
        get_pacman(0).move_hero(key_events[0])
        add_dirty_rect(PacDirtyRect(Rect(get_pacman(0).x - 2, get_pacman(0).y - 2, 30, 30), get_pacman(0).is_dot))
        if len(get_pacmans()) > 1:
            get_pacman(1).move_hero(key_events[1])
            add_dirty_rect(PacDirtyRect(Rect(get_pacman(1).x - 2, get_pacman(1).y - 2, 30, 30), get_pacman(1).is_dot))
        for ghost in get_ghosts():
            if ghost.active:
                ghost.move_hero(key_events)
            add_dirty_rect(PacDirtyRect(Rect(ghost.x - 2, ghost.y - 2, 30, 30), ghost.is_dot))

