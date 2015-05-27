from objects.Container import get_objects
GAME_EVENTS = {"DEATH": 60, "GAME_OVER": 10, "RESPAWN" : 1}
EVENTS = []


def add_event(event):
    EVENTS.append([event, GAME_EVENTS[event]])

def notify_observers(event_observers):
    for event in EVENTS:
        for game_object in get_objects():
            game_object.react(event[0])
        for event_observer in event_observers:
            event_observer.react(event[0])
        event[1] -= 1
        if event[1] == 0:
            if(event[0] == "DEATH"):
                add_event("RESPAWN")
            EVENTS.remove(event)
