DIRTY_RECT = []


def add_dirty_rect(dirty_rect):
    DIRTY_RECT.append(dirty_rect)


def clear_dirty_rect():
    del DIRTY_RECT[:]