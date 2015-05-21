from pygame.rect import Rect


class RectMatrix:
    def __init__(self, map_array):
        self.matrix = [[[Rect(x * 20, y * 20, 20, 20), map_array[y][x]]
                        for x in range(len(map_array[0]))] for y in range(len(map_array))]

    def is_at_direction_change_place(self, rect):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if self.matrix[y][x][0].contains(rect):
                    return True
        return False

    def is_dot_at_field(self, map_point):
        return self.matrix[map_point[0]][map_point[1]][1] == 7

    def is_wall_at_field(self, map_point):
        return 0 < self.matrix[map_point[0]][map_point[1]][1] < 7

    def get_map_point(self, rect):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if self.matrix[y][x][0].contains(rect):
                    return y, x

    def eat_dot(self, map_point):
        self.matrix[map_point[0]][map_point[1]][1] = 0

    def is_this_the_wall(self, rect, alter):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if self.matrix[y][x][0].contains(rect):
                    return 0 < self.matrix[y + alter[1]][x + alter[0]][1] < 7

    def get_rect(self, rect):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if self.matrix[y][x][0].contains(rect):
                    return self.matrix[y][x][0]

