import pygame
from pygame.constants import MOUSEBUTTONDOWN
from game import Game, ClientGame, ServerGame


class GameStart:
    def __init__(self, window_surface, container, event_handler):
        self.window_surface = window_surface
        self.container = container
        self.event_handler = event_handler

    def display_start_screen(self):
        black = (0, 0, 0)
        is_true = True
        self.window_surface.fill(black)
        pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start.png",), (0, 100))
        pygame.display.flip()
        while is_true:
            for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start.png",), (0, 100))
                        wsp = pygame.mouse.get_pos()
                        if wsp[1] < 400:
                            Game(self.window_surface, self.container, self.event_handler).start_game()
                        else:
                            pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start_dual.png",), (0, 100))
                            pygame.display.flip()
                            while True:
                                for event1 in pygame.event.get():
                                    if event1.type == MOUSEBUTTONDOWN:
                                        wsp = pygame.mouse.get_pos()
                                        if wsp[0] < 310:
                                            ClientGame(self.window_surface, self.container, self.event_handler).start_game()
                                        else:
                                            ServerGame(self.window_surface, self.container, self.event_handler).start_game()
                        is_true = False


