import types


class EventObserver:
    def __init__(self):
        self.react_cases = {}


    def react(self, event):
        if self.react_cases.__contains__(event):
            self.react_cases[event]()