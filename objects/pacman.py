import media.sprites


class PacMan:
    def __init__(self, x, y):
        self.x = x              # x position in the matrix
        self.y = y              # y position in the matrix
        self.speed = 4
        self.animations = media.sprites.PacManAnim
        for key, animation in self.animations.items():
            animation.play()

    def paint(self, window_surface, direction):
        self.animations[direction].blit(window_surface, (self.x, self.y))  # each background png is 20x20

    def move(self, dMove):
        self.x += dMove[0]
        self.y += dMove[1]
