import media.sprites


class PacMan:
    def __init__(self, x, y):
        self.x = x              # x position in the matrix
        self.y = y              # y position in the matrix
        self.speed = 4/9
        self.animations = media.sprites.PacManAnim
        for key, animation in self.animations.items():
            animation.play()

    def paint(self, window_surface, direction):
        self.animations[direction].blit(window_surface, (int(self.x) * 20, int(self.y) * 20))  # each background png is 20x20

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
