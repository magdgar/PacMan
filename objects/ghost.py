from pygame.constants import *
from pygame.rect import Rect
from events.eventconstans import DEATH, POWER_UP, BACK_TO_CHASE, ENEMY_DEATH
from pacfunctions.pacfunction import get_next_directions
from objects.hero import Hero
import media.sprites
CHASE = 999
SCATTER = 998
SCARED = 997
HOUSE = 996
FROZEN = 995
HOUSE_RETURN = 1000
class Ghost(Hero):
    def __init__(self, x, y, anim, rect_martix, container, evenent_handler):
        super().__init__(x, y, rect_martix, container, evenent_handler)
        self.standard_anim = anim
        self.current_anim = anim
        self.corner_changer = 0
        self.house_time = 1
        self.scatter_time = 1000
        self.corner_points = []
        self.is_dot = True
        self.is_scared = False
        self.change_direction_counter = 1
        self.stupidity = 3
        self.react_cases = {POWER_UP: self.run_away, BACK_TO_CHASE: self.back_to_chase}
        self.move_functions = {CHASE: self.chase_move, SCATTER: self.scatter_move,
                               SCARED: self.scared_move, HOUSE: self.house_move,
                                   FROZEN: self.stand_still, HOUSE_RETURN: self.house_return_move}
        self.move_hero_function = self.house_move
        self.new_directions = get_next_directions((round(self.y / 20), round(self.x / 20)),
                                                    (round(self.container.pac_man.y / 20), round(self.container.pac_man.x / 20)))
        self.last_predicted_rect = []
        self.new_directions_painted = False
        for key, animation in self.standard_anim.items():
            animation.play()

        self.container.add_object(self)

    def move(self):
        super().move()
        self.check_if_catched()
        self.check_if_enemy_catched()

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
        if self.in_place_to_change_direction():
            self.map_point = self.rect_matrix.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            self.direction = get_next_directions(self.map_point, self.container.pac_man.predicted_pac_man_point(20))[0]

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

    def house_return_move(self):
        if self.in_place_to_change_direction():
            self.map_point = self.rect_matrix.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            self.new_directions = get_next_directions(self.map_point, (13, 14))
            if len(self.new_directions) == 1:
                self.is_scared = False
                self.reload_movements()
                self.current_anim = self.standard_anim
                self.change_move_hero_function(CHASE)
            else:
                self.direction = self.new_directions[0]

    def run_away(self):
        if not self.is_scared:
            self.change_move_hero_function(SCARED)
            self.speed = 1
            self.reload_movements()
            self.current_anim = media.sprites.FrightenAnim
            for key, anim in self.current_anim.items():
                anim.play()
            self.is_scared = True

    def back_to_chase(self):
        if self.in_place_to_change_direction() and not self.move_hero_function == self.house_return_move:
            self.is_scared = False
            self.speed = 2
            self.reload_movements()
            self.current_anim = self.standard_anim
            self.change_move_hero_function(CHASE)

    def get_directions_to_closest_pacman(self):
        if self.container.enemy_pac_man is None:
            self.new_directions = get_next_directions(self.map_point, self.container.pac_man.map_point)
        else:
            if self.container.pac_man.active:
                directions_to_player = get_next_directions(self.map_point, self.container.pac_man.map_point)
            else:
                directions_to_player = [self.get_proper_random_direction()]
            if self.container.enemy_pac_man.active:
                directions_to_enemy = get_next_directions(self.map_point, self.container.enemy_pac_man.map_point)
            else:
                directions_to_enemy = [self.get_proper_random_direction()]
            if len(directions_to_enemy) == 0 and len(directions_to_player) == 0:
                return [self.get_proper_random_direction()]
            self.new_directions = directions_to_player if len(directions_to_player) <= len(directions_to_enemy) else directions_to_enemy
        return self.new_directions

    def get_predicted_rect(self):
        predicted_rect = []
        current_rect = self.area_rect
        for direction in self.new_directions:
            current_rect = Rect(current_rect.left + (self.movements[direction][0] * 20 / self.speed),
                                current_rect.top + (self.movements[direction][1] * 20 / self.speed),
                                20, 20)
            predicted_rect.append(current_rect)
        self.last_predicted_rect = predicted_rect
        return predicted_rect

    def is_dot_at_field(self):
        return self.rect_matrix.is_dot_at_field(self.map_point)

    def check_if_catched(self):
        if self.area_rect.colliderect(self.container.pac_man.area_rect):
            if not self.is_scared:
                if self.container.pac_man.alive:
                    self.container.pac_man.alive = False
                    self.container.pac_man.active = False
                    if self.container.enemy_pac_man is  None:
                        for ghost in self.container.ghosts:
                            ghost.active = False
                    self.event_handler.add_event(DEATH)
            elif self.in_place_to_change_direction():
                self.change_move_hero_function(HOUSE_RETURN)
                self.current_anim = media.sprites.EyesAnim
                for key, anim in self.current_anim.items():
                    anim.play()
                self.speed = 2
                self.reload_movements()

    def check_if_enemy_catched(self):#TODO temp!
        if self.container.enemy_pac_man is not None:
            if self.area_rect.colliderect(self.container.enemy_pac_man.area_rect):
                if not self.is_scared:
                    if self.container.enemy_pac_man.alive:
                        self.container.enemy_pac_man.alive = False
                        self.container.enemy_pac_man.active = False
                        self.event_handler.add_event(ENEMY_DEATH)
                elif self.in_place_to_change_direction():
                    self.change_move_hero_function(HOUSE_RETURN)
                    self.current_anim = media.sprites.EyesAnim
                    for key, anim in self.current_anim.items():
                        anim.play()
                    self.speed = 2
                    self.reload_movements()




def stupidity_decorator(func):
    def stupitidy(self, *args, **kwargs):
        if self.in_place_to_change_direction():
            self.map_point = self.rect_matrix.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            if self.change_direction_counter % self.stupidity == 0:
                self.change_direction_counter = 1
                func(self, *args, **kwargs)
                self.new_directions_painted = False
                self.direction = self.new_directions[0]
            else:
                if self.change_direction_counter < len(self.new_directions):
                    self.direction = self.new_directions[self.change_direction_counter]
                else:
                    self.direction = self.get_proper_random_direction()
                self.change_direction_counter += 1
    return stupitidy