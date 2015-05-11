import painter.painter
from media.dirtyrect import *
from game_engine.game_engine import *


class GameLoop:
    def __init__(self, window_surface, game_engine):
        self.game_engine = game_engine
        self.painter = painter.painter.Painter(window_surface)

    def perform_one_cycle(self, events):
        add_dirty_rect(Rect(0, 0, 40, 40))
        self.painter.paint_objects()
        self.game_engine.simulate_world(events)