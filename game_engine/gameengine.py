from objects.container import *
with open("C:/Users/Maciek/PacMan/resources/lvl2.txt") as file:
    BG_MATRIX = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]



class GameEngine:
    def __init__(self, window_surface):
        self.window_surface = window_surface


    def simulate_world(self, events):
        for hero in get_objects():
            hero.move_hero([events])

