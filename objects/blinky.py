from pygame.rect import Rect
from game_engine.gameengine import BG_MATRIX
from objects.container import get_object
from pacfunctions.pacfunction import get_next_directions
import media
from media.dirtyrect import add_dirty_rect, PacDirtyRect
from objects.hero import Hero, RECT_MATRIX


class Blinky(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_dot = True
        self.animations = media.sprites.BlinkyAnim
        self.change_direction_counter = 1
        self.stupidity = 6
        self.new_directions = get_next_directions((round(self.y / 20), round(self.x / 20)),
                                                    (round(get_object(0).y / 20), round(get_object(0).x / 20)))
        for key, animation in self.animations.items():
            animation.play()

    def move(self):
        super().move()
        add_dirty_rect(PacDirtyRect(Rect(self.x, self.y, 26, 26), self.is_dot))

    def move_hero(self, arguments): #sprawa z argumentami do przemyslenia

        if self.in_place_to_change_direction():
            self.is_dot = self.is_dot_at_field()
            if self.change_direction_counter % self.stupidity == 0:
                self.change_direction_counter = 1
                self.new_directions = get_next_directions((round(self.y / 20), round(self.x / 20)),
                                                    (round(get_object(0).y / 20), round(get_object(0).x / 20)))
                self.direction = self.new_directions[0]
            else:
                if self.change_direction_counter < len(self.new_directions):
                    self.direction = self.new_directions[self.change_direction_counter]
                else:
                    self.direction = self.get_proper_random_direction()
                self.change_direction_counter += 1

        self.move()

    def is_dot_at_field(self):
        return RECT_MATRIX.is_dot_at_field(self.area_rect)
