from events.eventobserver import EventObserver
from objects.ghost import Ghost
from objects.pacman import PacMan


class Container:
    def __init__(self):
        self.game_objects = []
        self.event_observers = []
        self.ghosts = []
        self.pac_man = None
        self.enemy_pac_man = None

    def add_object(self, new_object):
        self.game_objects.append(new_object)
        if isinstance(new_object, EventObserver):
            self.event_observers.append(new_object)
        if isinstance(new_object, Ghost):
            self.ghosts.append(new_object)
        if isinstance(new_object, PacMan):
            if self.pac_man is None:
                self.pac_man = new_object
            else:
                self.enemy_pac_man = new_object

    def del_objects(self):
        del self.game_objects[:]
        del self.ghosts[:]
        self.pac_man = None
        self.enemy_pac_man = None



