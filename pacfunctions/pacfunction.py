from pygame.constants import *
from pacfunctions.paclogic import *


def get_next_directions(point_from, point_to):
    shortest_way_list = shortest_way(point_from, point_to)
    directions = [change_to_direction(point_from, shortest_way_list[0])]
    for n in range(len(shortest_way_list) - 1):
        directions.append(change_to_direction(shortest_way_list[n], shortest_way_list[n+1]))
    return directions


def change_to_direction(point_from, next_point):
    if point_from[0] < next_point[0]:
        return K_DOWN
    elif point_from[1] < next_point[1]:
        return K_RIGHT
    elif point_from[0] > next_point[0]:
        return K_UP
    elif point_from[1] > next_point[1]:
        return K_LEFT

