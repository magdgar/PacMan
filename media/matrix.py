from pygame.constants import *
from pygame.rect import Rect
from pacfunctions.pacfunction import add_points, negative_direction, as_a_grid
from pacfunctions.paclogic import valid


class RectMatrix:
    def __init__(self, path):
        with open(path) as file:
            map_array = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]
        self.matrix = [[[Rect(x * 20, y * 20, 20, 20), map_array[y][x]]
                        for x in range(len(map_array[0]))] for y in range(len(map_array))]
        self.map_array = [[map_array[y][x] for x in range(len(map_array[0]))] for y in range(len(map_array))]
        self.remain_dots = self.count_dots()
        self.teleport_points = self.find_teleport_points()
        print(self.teleport_points)

    def count_dots(self):
        dot_counter = 0
        for (y, x) in as_a_grid(self.matrix):
            if self.matrix[y][x][1] == 7:
                dot_counter += 1
        return dot_counter

    def is_at_direction_change_place(self, rect):
        for (y, x) in as_a_grid(self.matrix):
            if self.matrix[y][x][0].contains(rect):
                return True
        return False

    def is_dot_at_field(self, map_point):
        return self.matrix[map_point[0]][map_point[1]][1] == 7

    def is_wall_at_field(self, map_point):
        if valid(map_point):
            return 0 < self.matrix[map_point[0]][map_point[1]][1] < 7 or self.matrix[map_point[0]][map_point[1]][1] == 8
        return True

    def get_map_point(self, rect):
        for (y, x) in as_a_grid(self.matrix):
            if self.matrix[y][x][0].contains(rect):
                return y, x

    def eat_dot(self, map_point):
        self.map_array[map_point[0]][map_point[1]] = 0
        if self.matrix[map_point[0]][map_point[1]][1] == 7:
            self.remain_dots -= 1
            self.matrix[map_point[0]][map_point[1]][1] = 0
            return True
        return False

    def eat_power_dot(self, map_point):
        self.map_array[map_point[0]][map_point[1]] = 0
        if self.matrix[map_point[0]][map_point[1]][1] == 8:
            self.matrix[map_point[0]][map_point[1]][1] = 0
            return True
        return False

    def is_game_won(self):
        return self.remain_dots == 0

    def is_this_the_wall(self, rect, alter):
        for (y, x) in as_a_grid(self.matrix):
            if self.matrix[y][x][0].contains(rect):
                return 0 < self.matrix[y + alter[1]][x + alter[0]][1] < 7

    def get_rect(self, rect):
        for (y, x) in as_a_grid(self.matrix):
            if self.matrix[y][x][0].contains(rect):
                return self.matrix[y][x][0]

    def get_proper_random_direction(self, point, direction):
        if not self.is_wall_at_field(add_points(point, (-1, 0))) and K_UP != negative_direction(direction):
            return K_UP
        elif not self.is_wall_at_field(add_points(point, (0, 1))) and K_RIGHT != negative_direction(direction):
            return K_RIGHT
        elif not self.is_wall_at_field(add_points(point, (1, 0))) and K_DOWN != negative_direction(direction):
            return K_DOWN
        elif not self.is_wall_at_field(add_points(point, (0, -1))) and K_LEFT != negative_direction(direction):
            return K_LEFT
        return negative_direction(direction)

    def find_teleport_points(self):
        teleport_points = []
        for (y, x) in as_a_grid(self.matrix):
            if self.matrix[y][x][1] == 9:
                teleport_points.append((y, x))

        return teleport_points



