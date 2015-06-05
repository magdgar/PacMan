from copy import deepcopy
from pygame.locals import *
from events.eventhandler import add_event
import media.sprites
from objects.Container import get_ghosts, add_object
from objects.hero import Hero, RECT_MATRIX
from pacfunctions.pacfunction import next_point_in_direction

class PacMan(Hero):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.animations = media.sprites.PacManAnim
        self.react_cases = {"DEATH": self.die}
        self.alive = True
        self.is_dot = False
        for key, animation in self.animations.items():
            animation.play()
        add_object(self, True)

    def move(self):
        super().move()
       # add_dirty_rect(PacDirtyRect(Rect(self.x - 2, self.y - 2, 30, 30), self.is_dot))

    def move_hero(self, key):
        self.new_direction = key
        if self.in_place_to_change_direction():
            self.tunel_teleportation()
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.eat_dot()
            if not self.is_this_the_wall(self.new_direction):
                self.direction = self.new_direction

            if self.is_this_the_wall(self.direction):
                self.go_back()
        self.move()

    def eat_dot(self):
        RECT_MATRIX.eat_dot(self.map_point)

    def predicted_pac_man_point(self, steps_to_predict):
        pac_point = self.map_point
        pac_direction = deepcopy(self.direction)
        while steps_to_predict > 0:

            if not RECT_MATRIX.is_wall_at_field(next_point_in_direction(pac_point, pac_direction)):
                pac_point = next_point_in_direction(pac_point, pac_direction)
            else:
                pac_direction = RECT_MATRIX.get_proper_random_direction(pac_point, pac_direction)
                pac_point = next_point_in_direction(pac_point, pac_direction)
            steps_to_predict -= 1
        return pac_point

    def tunel_teleportation(self):
        if self.map_point in RECT_MATRIX.teleport_points:
            if self.map_point[1] == 28 and self.direction == K_RIGHT:
                self.teleport((13, 0))
            elif self.map_point[1] == 1 and self.direction == K_LEFT:
                self.teleport((13, 28))
            add_event("REPAINT")

    def die(self):
        self.direction = K_DELETE
        self.active = False

