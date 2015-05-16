DIRTY_RECT = []


def add_dirty_rect(pac_dirty_rect):
    DIRTY_RECT.append(pac_dirty_rect)


def clear_dirty_rect():
    del DIRTY_RECT[:]


class PacDirtyRect:
    def __init__(self, dirty_rect, dot):
        self.dirty_rect = dirty_rect
        self.dot = dot