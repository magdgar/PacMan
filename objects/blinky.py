import media
from objects.ghost import Ghost


class Blinky(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, media.sprites.BlinkyAnim)

    def move_hero(self, arguments): #sprawa z argumentami do przemyslenia
        super().move_hero(arguments)
