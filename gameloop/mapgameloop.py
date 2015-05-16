import sys

from pygame.locals import *

from background.background import *


POSSIBLE_MAP_KEYS = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7]
MAP_DICT = {K_0: 0, K_1: 1, K_2: 2, K_3: 3, K_4: 4, K_5: 5, K_6: 6, K_7: 7}


class GameLoop:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.current_paint_item = MAP_DICT[K_1]
        self.map_array = []
        # self.reload_map()

    def handle_map_event(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.change_map_field(pos)
                paint_whole_background(self.window_surface, self.map_array)
            elif event.type == KEYDOWN:
                if event.key == K_s:
                    self.save_map_to_file()
                elif event.key == K_l:
                    self.reload_map()
                elif event.key in POSSIBLE_MAP_KEYS:
                    self.current_paint_item = MAP_DICT[event.key]
            elif event.type == QUIT:
                self.save_map_to_file()
                pygame.quit()
                sys.exit()

    def change_map_field(self, pos):
        x = int(pos[0] / 20)
        y = int(pos[1] / 20)
        self.map_array[y][x] = self.current_paint_item
        print(self.map_array[y][x])


    def save_map_to_file(self):
        string = ""
        for y in range(len(self.map_array)):
            for x in range(len(self.map_array[0]) - 1):
                string += str(self.map_array[y][x])
            string += '\n'
        with open("resources/map.txt", "w") as file:
            file.write(string)

            # def reload_map(self):
            # with open("resources/lvl2.txt") as file:
            #       array2d = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]
            #  paint_whole_background(self.window_surface, self.map_array)