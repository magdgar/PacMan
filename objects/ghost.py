from pygame.constants import *
from pygame.rect import Rect
from events.eventhandler import add_event
from objects.container import get_object
from pacfunctions.pacfunction import get_next_directions
from media.dirtyrect import add_dirty_rect, PacDirtyRect
from objects.hero import Hero, RECT_MATRIX


class Ghost(Hero):
    def __init__(self, x, y, anim):
        super().__init__(x, y)
        self.is_dot = True
        self.animations = anim
        self.change_direction_counter = 1
        self.stupidity = 6
        self.new_directions = get_next_directions((round(self.y / 20), round(self.x / 20)),
                                                    (round(get_object(0).y / 20), round(get_object(0).x / 20)))
        for key, animation in self.animations.items():
            animation.play()

    def move(self):
        super().move()
        self.check_if_catched()
        add_dirty_rect(PacDirtyRect(Rect(self.x, self.y, 26, 26), self.is_dot))

    def is_dot_at_field(self):
        return RECT_MATRIX.is_dot_at_field(self.map_point)

    def check_if_catched(self):
        if self.area_rect.colliderect(get_object(0).area_rect):
            if get_object(0).alive:
                get_object(0).alive = False
                add_event("DEATH")
