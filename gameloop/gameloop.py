from gamestate.gamestate import GameState
import painter.painter
from events.eventhandler import notify_observers

class GameLoop:
    def __init__(self, window_surface, game_engine, game):
        self.game = game
        self.game_engine = game_engine
        self.painter = painter.painter.Painter(window_surface)
        self.game_state = GameState()

    def perform_one_cycle(self, events):
        self.game_engine.simulate_world(events)
        self.painter.paint_objects()
        notify_observers([self.painter, self.game_state, self.game])
