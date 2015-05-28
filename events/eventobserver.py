"""class extended by all objects interested in reacting to game events"""


class EventObserver:
    def __init__(self):
        # dict should be overwritten with event names as keys and functions as values
        self.react_cases = {}

    def react(self, event):
        """with event as key extract right function and call it"""
        if self.react_cases.__contains__(event):
            self.react_cases[event]()
