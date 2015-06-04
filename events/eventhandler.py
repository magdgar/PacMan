"""handles event appearing and notifying observers"""

from objects.Container import get_objects
#dictionary with all possible events as keys and length in frames
GAME_EVENTS = {"DEATH": 60, "GAME_OVER": 200, "RESPAWN": 1, "REPAINT": 1, "EXIT": 1}
#acvtie events
EVENTS = []

def add_event(event):
    """function called when events occurs"""
    EVENTS.append([event, GAME_EVENTS[event]])

def notify_observers(event_observers):
    """for each active event calls react on all observers"""
    for event in EVENTS:
        for game_object in get_objects():
            game_object.react(event[0])
        for event_observer in event_observers:
            event_observer.react(event[0])
        event[1] -= 1
        if event[1] == 0:
            if(event[0] == "DEATH"):
                add_event("RESPAWN")
            if(event[0] == "GAME_OVER"):
                add_event("EXIT")
            #when event time is zero remove event from list
            EVENTS.remove(event)

