from events.eventhandler import add_event
from events.eventobserver import EventObserver
from objects.Container import get_objects, get_object


class GameState(EventObserver):

    def __init__(self):
        super().__init__()
        self.react_cases = {"RESPAWN" : self.pacman_die}
        self.score = 0
        self.lives_left = 3

    def pacman_die(self):
        self.lives_left -= 1
        if self.lives_left == 0:
            add_event("GAME_OVER")

    def add_score(self):
        self.score += 1

