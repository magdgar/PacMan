from pygame.constants import *
from events.eventconstans import DEATH
from pacfunctions.pacfunction import get_next_directions
from objects.hero import Hero
CHASE = 999
SCATTER = 998
SCARED = 997
HOUSE = 996
FROZEN = 995

class Ghost(Hero):
    def __init__(self, x, y, anim, rect_martix, container, evenent_handler):
        super().__init__(x, y, rect_martix, container, evenent_handler)
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
                                                    (round(self.container.pac_man.y / 20), round(self.container.pac_man.x / 20)))
        for key, animation in self.animations.items():
            animation.play()

        self.container.add_object(self)

    def move(self):
        super().move()
        self.check_if_catched()

    def move_hero(self, arguments):
        self.move_hero_function()
        self.move()

    def chase_move(self):
        pass

    def scatter_move(self):
        if self.in_place_to_change_direction():
            self.map_point = self.rect_matrix.get_map_point(self.area_rect)
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

    def get_directions_to_closest_pacman(self):
        if self.container.enemy_pac_man is None:
            self.new_directions = get_next_directions(self.map_point, self.container.pac_man.map_point)
        else:
            directions_to_player = get_next_directions(self.map_point, self.container.pac_man.map_point)
            directions_to_enemy = get_next_directions(self.map_point, self.container.enemy_pac_man.map_point)
            self.new_directions = directions_to_player if len(directions_to_player) <= len(directions_to_enemy) else directions_to_enemy
        return self.new_directions


    def is_dot_at_field(self):
        return self.rect_matrix.is_dot_at_field(self.map_point)

    def check_if_catched(self):
        if self.area_rect.colliderect(self.container.pac_man.area_rect):
            if self.container.pac_man.alive:
                self.container.pac_man.alive = False
                self.container.pac_man.active = False
                for ghost in self.container.ghosts:
                    ghost.active = False
                self.event_handler.add_event(DEATH)


def stupidity_decorator(func):
    def stupitidy(self, *args, **kwargs):
        if self.in_place_to_change_direction():
            self.map_point = self.rect_matrix.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            if self.change_direction_counter % self.stupidity == 0:
                self.change_direction_counter = 1
                func(self, *args, **kwargs)
                self.direction = self.new_directions[0]
            else:
                if self.change_direction_counter < len(self.new_directions):
                    self.direction = self.new_directions[self.change_direction_counter]
                else:
                    self.direction = self.get_proper_random_direction()
                self.change_direction_counter += 1
    return stupitidy