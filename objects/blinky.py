from pygame.rect import Rect
from game_engine.gameengine import BG_MATRIX
from objects.container import get_object
from pacfunctions.pacfunction import get_next_direction
import media
from media.dirtyrect import add_dirty_rect, PacDirtyRect
from objects.hero import Hero, RECT_MATRIX


class Blinky(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_dot = True
        self.animations = media.sprites.BlinkyAnim
        for key, animation in self.animations.items():
            animation.play()

    def move(self):
        super().move()
        add_dirty_rect(PacDirtyRect(Rect(self.x, self.y, 26, 26), self.is_dot))

    def move_hero(self, arguments): #sprawa z argumentami do przemyslenia
        self.new_direction = get_next_direction((round(self.y / 20), round(self.x / 20)),
                                                    (round(get_object(0).y / 20), round(get_object(0).x / 20)))

        if self.in_place_to_change_direction():
            self.is_dot = self.is_dot_at_field()
            self.direction = self.new_direction
        self.move()

    def is_dot_at_field(self):
        return RECT_MATRIX.is_dot_at_field(self.area_rect)
