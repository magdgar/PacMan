import media.sprites
from objects.hero import Hero


class PacMan(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.animations = media.sprites.PacManAnim
        for key, animation in self.animations.items():
            animation.play()

    def move(self, d_move):
        super().move()
        self.x += d_move[0]
        self.y += d_move[1]
