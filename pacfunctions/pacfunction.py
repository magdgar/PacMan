from pacfunctions.paclogic import *


def get_next_directions(point_from, point_to):
    shortest_way_list = shortest_way(point_from, point_to)
    directions = [change_to_direction(point_from, shortest_way_list[0])]
    for n in range(len(shortest_way_list) - 1):
        directions.append(change_to_direction(shortest_way_list[n], shortest_way_list[n+1]))
    return directions


def add_points(point, second_point):
    return point[0] + second_point[0], point[1] + second_point[1]


def next_point_in_direction(point, direction):
    if direction == K_UP or direction == K_w:
        return add_points(point, (-1, 0))
    elif direction == K_RIGHT or direction == K_d:
        return add_points(point, (0, 1))
    elif direction == K_DOWN or direction == K_s:
        return add_points(point, (1, 0))
    elif direction == K_LEFT or direction == K_a:
        return add_points(point, (0, -1))


def negative_direction(direction):
    if direction == K_UP:
        return K_DOWN
    elif direction == K_RIGHT:
        return K_LEFT
    elif direction == K_DOWN:
        return K_UP
    elif direction == K_LEFT:
        return K_RIGHT
    elif direction == K_d:
        return K_a
    elif direction == K_s:
        return K_w
    elif direction == K_w:
        return K_s
    elif direction == K_a:
        return K_d


def as_a_grid(alist):
    for i in range(len(alist)):
        for j in range(len(alist[i])):
            yield(i, j)