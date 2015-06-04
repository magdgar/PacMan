import pygame

class DynamicImages:
    lives = 'resources/live.png'

    def __init__(self, window_surface):
        self.window_surface = window_surface
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.lives), (100, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.lives), (70, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.lives), (40, 580))

    def paint(self):
       pass
