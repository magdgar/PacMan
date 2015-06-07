"""handles everything that should be performed in one frame"""
from game_engine.gameengine import GameEngine

from gamestate.gamestate import GameState
import painter.painter

class GameLoop:
    def __init__(self, window_surface, cointainer, game):
        self.game = game
        self.painter = painter.painter.Painter(window_surface, game.container, game.event_handler, game.rect_matrix)
        self.game_engine = GameEngine(window_surface, cointainer, self.painter)
        self.game.event_handler.add_observer(self.game)
        self.game.event_handler.add_observer(self.painter)
        self.game.event_handler.add_observer(self.game.game_state)

    def perform_one_cycle(self, key_events):
        """calls main modules"""
        self.game_engine.simulate_world(key_events)
        self.painter.paint_objects()
        self.game.event_handler.notify_observers()
