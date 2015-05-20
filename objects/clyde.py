from pygame.rect import Rect
from objects.container import get_object
from pacfunctions.pacfunction import get_next_directions
import media
from media.dirtyrect import add_dirty_rect, PacDirtyRect
from objects.hero import Hero, RECT_MATRIX


class Clyde(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_dot = True
        self.animations = media.sprites.ClydeAnim
        self.change_direction_counter = 1
        self.stupidity = 6
        self.new_directions = self.get_directions()
        for key, animation in self.animations.items():
            animation.play()

    def move(self):
        super().move()
        add_dirty_rect(PacDirtyRect(Rect(self.x, self.y, 26, 26), self.is_dot))

    def get_directions(self):
        directions_to_pacman = get_next_directions((round(self.y / 20), round(self.x / 20)),
                                                    (round(get_object(0).y / 20), round(get_object(0).x / 20)))
        directions_to_left_corner = get_next_directions((round(self.y / 20), round(self.x / 20)), (27, 1))
        if len(directions_to_pacman) <= 8:
            self.stupidity = len(directions_to_left_corner)
            return directions_to_left_corner
        else:
            self.stupidity = 6
            return directions_to_pacman

    def move_hero(self, arguments): #sprawa z argumentami do przemyslenia

        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            if self.change_direction_counter % self.stupidity == 0:
                self.change_direction_counter = 1
                self.new_directions = self.get_directions()
                self.direction = self.new_directions[0]
            else:
                if self.change_direction_counter < len(self.new_directions):
                    self.direction = self.new_directions[self.change_direction_counter]
                else:
                    self.direction = self.get_proper_random_direction()
                self.change_direction_counter += 1

        self.move()

    def is_dot_at_field(self):
        return RECT_MATRIX.is_dot_at_field(self.map_point)
