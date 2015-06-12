from objects.ghost import Ghost
from objects.ghost import stupidity_decorator
import media


class Blinky(Ghost):
    def __init__(self, x, y, rect_martix, container, evenent_handler):
        super().__init__(x, y, media.sprites.BlinkyAnim, rect_martix, container, evenent_handler)
        self.corner_points = [(1, 26), (5, 26)]
        self.house_time = 10
        self.color = (250, 0, 0, 128)

    @stupidity_decorator
    def chase_move(self):
        self.new_directions = self.get_directions_to_closest_pacman()


