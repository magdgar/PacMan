from pygame.rect import Rect

from game_engine.gameengine import BG_MATRIX
from objects.container import get_object
from pacfunctions.pacfunction import get_next_direction
import media
from media.dirtyrect import add_dirty_rect, PacDirtyRect
from objects.hero import Hero


class Blinky(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 4
        self.animations = media.sprites.BlinkyAnim
        for key, animation in self.animations.items():
            animation.play()

    def move(self):
        super().move()
        add_dirty_rect(PacDirtyRect(Rect(self.x - self.speed, self.y - self.speed, 30, 31), self.is_dot_at_field()))

    def move_hero(self, arguments): #sprawa z argumentami do przemyslenia
        self.new_direction = get_next_direction((round(self.y / 20), round(self.x / 20)),
                                            (round(get_object(0).y / 20), round(get_object(0).x / 20)))
        if self.in_place_to_change_direction(self):
            self.direction = self.new_direction
        self.move()

    def is_dot_at_field(self):
        return BG_MATRIX[round(self.y / 20)][round(self.x / 20)] == 7