from copy import deepcopy
from pygame.constants import *
import sys

with open("pacfunctions/map.txt") as file:
    path_array = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]
    path_array_copy = deepcopy(path_array)


def shortest_way(place_from, place_to, road_value=0):
    to_path_array()
    point_neighbours = neighbours(place_from)
    while place_to not in point_neighbours:
        if road_value > 50:
            to_path_array()
            return [neighbours(place_from)[0], neighbours(neighbours(place_from)[0])[0]]
        road_value += 1
        increse(point_neighbours, road_value)
        point_neighbours = list(set([point for points in list(map(neighbours, point_neighbours)) for point in points]))

    return list(reversed(colect_way_back(place_to, road_value)))


def colect_way_back(place_to, road_value):
    road_back = [place_to]
    while road_value > 0:
        for point in road_neighbour(place_to):
            if path_array[point[0]][point[1]] == road_value:
                road_back.append(point)
                place_to = point
                road_value -= 1
                break
    return road_back


def increse(points, road_value):
    for point in points:
        path_array[point[0]][point[1]] = road_value


def road_neighbour(point):
    return [valid_point for valid_point in [(point[0], point[1] - 1), (point[0] - 1, point[1]),
                                            (point[0], point[1] + 1), (point[0] + 1, point[1])] if
            valid_coord(valid_point)]


def neighbours(point):
    return [valid_point for valid_point in [(point[0], point[1] - 1), (point[0] - 1, point[1]),
                                            (point[0], point[1] + 1), (point[0] + 1, point[1])] if valid(valid_point)]

def all_neighbours(point):
    return [valid_point for valid_point in [(point[0]-1, point[1]-1), (point[0]-1, point[1]-1), (point[0]-1, point[1]), (point[0]-1, point[1]+1),
                                            (point[0], point[1] - 1), (point[0], point[1] + 1),
                                            (point[0]+1, point[1]-1), (point[0]+1, point[1]), (point[0]+1, point[1]+1)]
            if valid(valid_point)]

def valid(point):
    return valid_coord(point) and valid_value(point)


def valid_coord(point):
    return 0 <= point[0] < len(path_array) \
           and 0 <= point[1] < len(path_array[0])


def valid_value(point):
    return path_array[point[0]][point[1]] == 0

def change_to_direction(point_from, next_point):
    if point_from[0] < next_point[0]:
        return K_DOWN
    elif point_from[1] < next_point[1]:
        return K_RIGHT
    elif point_from[0] > next_point[0]:
        return K_UP
    elif point_from[1] > next_point[1]:
        return K_LEFT

def to_path_array():
    for y in range(len(path_array)):
        for x in range(len(path_array[0])):
            if path_array_copy[y][x] != 7 and path_array_copy[y][x] != 0 and path_array_copy[y][x] != 8:
                path_array[y][x] = '*'
            else:
                path_array[y][x] = 0

def print_path_array(place_from=(0, 0), place_to=(0, 0)):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row])
      for row in path_array]))
    print(place_from)
    print(place_to)



