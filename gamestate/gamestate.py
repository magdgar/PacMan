"contains basic variables used in one gameplay"
from events.eventobserver import EventObserver
from events.eventconstans import GAME_OVER, RESPAWN
class GameState(EventObserver):

    def __init__(self, coinainer, event_handler):
        super().__init__(coinainer, event_handler)
        self.react_cases = {RESPAWN : self.pacman_die}
        self.score = 0
        self.lives_left = 3

    def pacman_die(self):
        self.lives_left -= 1
        if self.lives_left == 0:
            self.event_handler.add_event(GAME_OVER)

    def add_score(self):
        self.score += 1

