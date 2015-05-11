import painter.painter


class GameLoop:
    def __init__(self, window_surface, game_engine):
        self.game_engine = game_engine
        self.painter = painter.painter.Painter(window_surface)

    def perform_one_cycle(self, events):
        self.game_engine.simulate_world(events)
        self.painter.paint_objects()
