"contains basic variables used in one gameplay"
from events.eventobserver import EventObserver
class GameState(EventObserver):

    def __init__(self, coinainer, event_handler):
        super().__init__(coinainer, event_handler)
        self.score = 0
        self.enemy_score = 0
        self.lives_left = 3
        self.enemy_lives_left = 3

    def add_score(self):
        self.score += 1

    def add_enemy_score(self):
        self.enemy_score += 1

