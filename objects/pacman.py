from copy import deepcopy
from pygame.locals import *
from events.eventconstans import DEATH, REPAINT, EAT_DOT, WON, POWER_UP, ENEMY_DEATH, ENEMY_EAT_DOT

import media.sprites
from objects.hero import Hero
from pacfunctions.pacfunction import next_point_in_direction
AI_KEY = -1
class PacMan(Hero):
    def __init__(self, x, y, rect_martix, container, evenent_handler):
        super().__init__(x, y, rect_martix, container, evenent_handler)
        self.current_anim = media.sprites.PacManAnim
        self.react_cases = {DEATH: self.die}
        self.score = 0
        self.alive = True
        self.is_dot = False
        for key, animation in self.current_anim.items():
            animation.play()
        self.container.add_object(self)

    def move_hero(self, key):
        self.new_direction = key
        if self.in_place_to_change_direction():
            self.tunel_teleportation()
            self.map_point = self.rect_matrix.get_map_point(self.area_rect)
            self.eat_dot()
            if not self.is_this_the_wall(self.new_direction):
                self.direction = self.new_direction

            if self.is_this_the_wall(self.direction):
                self.go_back()
        self.move()

    def eat_dot(self):
        if self.rect_matrix.eat_dot(self.map_point):
            self.score += 1
            self.event_handler.add_event(EAT_DOT)
            if self.rect_matrix.count_dots() == 0:
                self.event_handler.add_event(WON)
        elif self.rect_matrix.eat_power_dot(self.map_point):
            self.event_handler.add_event(POWER_UP)

    def predicted_pac_man_point(self, steps_to_predict):
        pac_point = self.map_point
        pac_direction = deepcopy(self.direction)
        while steps_to_predict > 0:

            if not self.rect_matrix.is_wall_at_field(next_point_in_direction(pac_point, pac_direction)):
                pac_point = next_point_in_direction(pac_point, pac_direction)
            else:
                pac_direction = self.rect_matrix.get_proper_random_direction(pac_point, pac_direction)
                pac_point = next_point_in_direction(pac_point, pac_direction)
            steps_to_predict -= 1
        return pac_point

    def tunel_teleportation(self):
        if self.map_point in self.rect_matrix.teleport_points:
            if self.map_point[1] == 28 and self.direction == K_RIGHT:
                self.teleport((13, 0))
            elif self.map_point[1] == 1 and self.direction == K_LEFT:
                self.teleport((13, 28))
            self.event_handler.add_event(REPAINT)

    def die(self):
        self.direction = K_DELETE
        self.active = False

class EnemyPacMan(PacMan):
    def __init__(self, x, y, rect_martix, container, evenent_handler):
        super().__init__(x, y, rect_martix, container, evenent_handler)
        self.react_cases = {ENEMY_DEATH: self.die}

    def move_hero(self, key):
        if key == AI_KEY:
            if self.in_place_to_change_direction():
                self.map_point = self.rect_matrix.get_map_point(self.area_rect)
                if self.is_this_the_wall(self.direction):
                    self.direction = self.get_proper_random_direction()
                self.eat_dot()
        else:
            super().move_hero(key)
        self.move()

    def eat_dot(self):
        if self.rect_matrix.eat_dot(self.map_point):
            self.score += 1
            self.event_handler.add_event(ENEMY_EAT_DOT)
            if self.rect_matrix.count_dots() == 0:
                self.event_handler.add_event(WON)
        elif self.rect_matrix.eat_power_dot(self.map_point):
            self.event_handler.add_event(POWER_UP)



