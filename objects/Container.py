GAME_OBJECTS = []


def add_object(new_object):
    GAME_OBJECTS.append(new_object)


def get_objects():
    return GAME_OBJECTS


def get_object(i):
    return GAME_OBJECTS[i]