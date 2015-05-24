from events.eventhandler import add_event
from events.eventobserver import EventObserver


class GameState(EventObserver):

    def __init__(self):
        super().__init__()
        self.react_cases = {"DEATH" : self.pacman_die}
        self.score = 0
        self.lives_left = 3

    def pacman_die(self):
        # print("JESTEM TUTAJ")
        self.lives_left -= 1
        if self.lives_left == 0:
            add_event("GAME_OVER")
        else:
            add_event("RESPAWN")

    def add_score(self):
        self.score += 1
