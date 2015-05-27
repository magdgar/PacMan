

GAME_OBJECTS = []
PAC_MAN = None
GHOSTS = []

def add_object(new_object):
    GAME_OBJECTS.append(new_object)
    if len(GAME_OBJECTS) > 0:
        GHOSTS.append(new_object)

def get_objects():
    return GAME_OBJECTS


def get_object(i):
    return GAME_OBJECTS[i]

def get_ghosts():
    return GHOSTS


def del_objects():
    del GAME_OBJECTS[:]
    del GHOSTS[:]



