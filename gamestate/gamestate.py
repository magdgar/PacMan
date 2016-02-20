"contains basic variables used in one gameplay"
from events.eventconstans import EAT_DOT, ENEMY_EAT_DOT, RESPAWN, ENEMY_RESPAWN
from events.eventobserver import EventObserver


class GameState(EventObserver):
    def __init__(self, coinainer, event_handler):
        EventObserver.__init__(self, coinainer, event_handler)
        self.react_cases = {EAT_DOT: self.add_score, ENEMY_EAT_DOT: self.add_enemy_score,
                            RESPAWN: self.kill_player, ENEMY_RESPAWN: self.kill_enemy}
        self.score = 0
        self.enemy_score = 0
        self.lives_left = 3
        self.enemy_lives_left = 3

    def add_score(self):
        self.score += 1

    def add_enemy_score(self):
        self.enemy_score += 1

    def kill_player(self):
        self.lives_left -= 1

    def kill_enemy(self):
        self.enemy_lives_left -= 1

