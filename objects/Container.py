from media.sprites import PacManAnim

GAME_OBJECTS = []
PAC_MANS = []
GHOSTS = []

def add_object(new_object):
    GAME_OBJECTS.append(new_object)
    if len(PAC_MANS) < 2:
        PAC_MANS.append(new_object)
    else:
        GHOSTS.append(new_object)

def get_objects():
    return GAME_OBJECTS


def get_object(i):
    return GAME_OBJECTS[i]

def get_ghosts():
    return GHOSTS
def get_pacmans():
    return PAC_MANS
def get_pacman(i):
    return PAC_MANS[i]
def del_objects():
    del GAME_OBJECTS[:]
    del PAC_MANS[:]
    del GHOSTS[:]



