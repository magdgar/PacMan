"""handles event appearing and notifying observers"""
from events.eventconstans import *
#dictionary with all possible events as keys and length in frames
GAME_EVENTS = {DEATH: 60, GAME_OVER: 200, RESPAWN: 1, REPAINT: 1, EXIT: 1, WON: 300, EAT_DOT: 1}


class EventHandler:
    def __init__(self, container):
        self.container = container
        self.active_events = []

    def add_event(self, event):
        """function called when events occurs"""
        self.active_events.append([event, GAME_EVENTS[event]])


    def add_observer(self, new_observer):
        self.container.event_observers.append(new_observer)
        

    def notify_observers(self):
        """for each active event calls react on all observers"""
        for event in self.active_events:
            for event_observer in self.container.event_observers:
                event_observer.react(event[0])
            event[1] -= 1
            if event[1] == 0:
                if event[0] == DEATH:
                    self.add_event(RESPAWN)
                if event[0] == GAME_OVER:
                    self.add_event(EXIT)
                if event[0] == WON:
                    self.add_event(EXIT)
                #when event time is zero remove event from list
                self.active_events.remove(event)

