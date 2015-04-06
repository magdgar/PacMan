import media.sprites


class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animations = [media.sprites.PacManAnimTop, media.sprites.PacManAnimRight,
                           media.sprites.PacManAnimDown, media.sprites.PacManAnimLeft]
        for animation in self.animations:
            animation.play()

    def paint(self, window_surface, number):
        self.animations[number].blit(window_surface, (self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
