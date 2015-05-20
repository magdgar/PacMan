from objects.container import *

with open("resources/map.txt") as file:
    BG_MATRIX = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]



class GameEngine:
    def __init__(self, window_surface):
        self.window_surface = window_surface

    @staticmethod
    def simulate_world(events):
        for hero in get_objects():
            hero.move_hero([events])

