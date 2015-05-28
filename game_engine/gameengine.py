from pygame.rect import Rect
from media.dirtyrect import add_dirty_rect, PacDirtyRect
from objects.Container import *
from media.constans import ACTUAL_LVL

with open(ACTUAL_LVL) as file:
    BG_MATRIX = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]

class GameEngine:
    def __init__(self, window_surface):
        self.window_surface = window_surface

    @staticmethod
    def simulate_world(events):
        for hero in get_objects():
            if hero.active:
                hero.move_hero([events])
            add_dirty_rect(PacDirtyRect(Rect(hero.x - 2, hero.y - 2, 30, 30), hero.is_dot))

