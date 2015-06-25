import pygame
from pygame.constants import MOUSEBUTTONDOWN, QUIT
import sys
from events.eventhandler import EventHandler
from game import Game, ClientGame, ServerGame, EnemyGame, HumanGame
from objects.Container import Container

BLACK = (0, 0, 0)

class GameStart:
    def __init__(self, window_surface, container, event_handler):
        self.window_surface = window_surface
        self.container = container
        self.event_handler = event_handler
        self.game_on = True

    def display_start_screen(self):
        self.window_surface.fill(BLACK)
        self.selection_of_the_number_of_players()

    def selection_of_the_number_of_players(self):
        pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start.png",), (0, 100))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:

                        wsp = pygame.mouse.get_pos()
                        if wsp[1] < 400:
                            self.selection_of_the_game_mode()
                        else:
                            self.selection_of_the_server_mode()
                        self.game_on = True
                        self.window_surface.fill(BLACK)
                        pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start.png",), (0, 100))
                        pygame.display.update()
                    elif event.type == QUIT:
                        sys.exit(0)

    def selection_of_the_server_mode(self):
        pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start_dual.png",), (0, 100))
        pygame.display.flip()
        while self.game_on:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    wsp = pygame.mouse.get_pos()
                    if wsp[1] > 450:
                        HumanGame(self.window_surface, self.container, self.event_handler).start_game()
                    else:
                        if wsp[0] < 310:
                            ClientGame(self.window_surface, self.container, self.event_handler).start_game()
                        else:
                            ServerGame(self.window_surface, self.container, self.event_handler).start_game()
                    self.game_on = False
                    self.container = Container()
                    self.event_handler = EventHandler(self.container)
                    self.window_surface.fill(BLACK)
                    pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start.png",), (0, 100))
                    pygame.display.update()
                elif event.type == QUIT:
                        sys.exit(0)

    def selection_of_the_game_mode(self):
        pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start_single.png",), (0, 100))
        pygame.display.flip()
        while self.game_on:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    wsp = pygame.mouse.get_pos()
                    if wsp[0] < 310:
                        Game(self.window_surface, self.container, self.event_handler).start_game()
                    else:
                        EnemyGame(self.window_surface, self.container, self.event_handler).start_game()
                    self.game_on = False
                    self.container = Container()
                    self.event_handler = EventHandler(self.container)
                    self.window_surface.fill(BLACK)
                    pygame.Surface.blit(self.window_surface, pygame.image.load("resources/start.png",), (0, 100))
                    pygame.display.update()
                elif event.type == QUIT:
                        sys.exit(0)

