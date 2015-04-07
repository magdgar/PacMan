import media.sprites


class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.animations = media.sprites.PacManAnim
        for key, animation in self.animations.items():
            animation.play()

    def paint(self, window_surface, direction):
        self.animations[direction].blit(window_surface, (self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
