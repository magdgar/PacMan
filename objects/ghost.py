from pygame.constants import *
from pygame.rect import Rect
from events.eventhandler import add_event
from objects.Container import get_object, get_ghosts
from pacfunctions.pacfunction import get_next_directions
from media.dirtyrect import add_dirty_rect, PacDirtyRect
from objects.hero import Hero, RECT_MATRIX
CHASE = 999
SCATTER = 998
SCARED = 997
HOUSE = 996
FROZEN = 995

class Ghost(Hero):
    def __init__(self, x, y, anim):
        super().__init__(x, y)
        self.corner_changer = 0
        self.house_time = 1
        self.scatter_time = 1000
        self.corner_points = []
        self.is_dot = True
        self.animations = anim
        self.change_direction_counter = 1
        self.stupidity = 6
        self.move_functions = {CHASE: self.chase_move, SCATTER : self.scatter_move,
                               SCARED : self.scared_move, HOUSE : self.house_move,
                               FROZEN : self.stand_still}
        self.move_hero_function = self.house_move
        self.new_directions = get_next_directions((round(self.y / 20), round(self.x / 20)),
                                                    (round(get_object(0).y / 20), round(get_object(0).x / 20)))
        for key, animation in self.animations.items():
            animation.play()

    def move(self):
        super().move()
        self.check_if_catched()

    def move_hero(self, arguments):
        self.move_hero_function()
        super().move()

    def chase_move(self):
        pass

    def scatter_move(self):
        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            self.new_directions = get_next_directions(self.map_point, self.corner_points[self.corner_changer])
            if len(self.new_directions) < 2:
                self.corner_changer += 1
                if self.corner_changer == len(self.corner_points):
                    self.corner_changer = 0
        self.direction = self.new_directions[0]

        # TODO change_move_hero_function should not be called from any ghost class!!!
        self.scatter_time -= 1
        if self.scatter_time == 0:
            self.change_move_hero_function(CHASE)

    def scared_move(self):
        pass

    def stand_still(self):
        self.direction = K_DELETE

    def change_move_hero_function(self, replacement_function_key):
        self.move_hero_function = self.move_functions[replacement_function_key]

    def house_move(self):
        if self.is_this_the_wall(self.direction):
            self.direction = self.get_proper_random_direction()

        # TODO change_move_hero_function Should not be called from any ghost class!!!
        self.house_time -= 1
        if self.house_time == 0:
            self.change_move_hero_function(SCATTER)


    def is_dot_at_field(self):
        return RECT_MATRIX.is_dot_at_field(self.map_point)

    def check_if_catched(self):
        if self.area_rect.colliderect(get_object(0).area_rect):
            if get_object(0).alive:
                get_object(0).alive = False
                get_object(0).active = False
                for ghost in get_ghosts():
                    ghost.active = False
                add_event("DEATH")
