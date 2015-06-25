import pygame
import sys
from events.eventconstans import *
from pygame.constants import KEYDOWN, K_RIGHT, K_LEFT, K_s, K_w, QUIT, K_y, K_u, K_UP, K_DOWN, K_a, K_d
from events.eventobserver import EventObserver
from gameloop.gameloop import GameLoop
from gamestate.gamestate import GameState
from media.constans import ACTUAL_LVL
from media.matrix import RectMatrix
from network import network
from objects.blinky import Blinky
from objects.clyde import Clyde
from objects.pacman import PacMan, EnemyPacMan
from objects.pinky import Pinky
from objects.inky import Inky

PLAYER_ONE_KEYS = [K_LEFT, K_UP, K_RIGHT, K_DOWN]
PLAYER_TWO_KEYS = [K_a, K_w, K_d, K_s]

class Game(EventObserver):
    def __init__(self, window_surface, container, event_handler):
        super().__init__(container, event_handler)
        self.react_cases = {RESPAWN: self.respawn, GAME_OVER: self.delete_ghost, EXIT: self.exit, WON: self.game_won}
        self.rect_matrix = RectMatrix(ACTUAL_LVL)
        self.fps = 60
        self.current_key = K_LEFT
        self.current_enemy_key = K_RIGHT
        self.game_on = True
        self.window_surface = window_surface
        self.paused = False
        self.game_state = GameState(container, event_handler)
        self.reset_objects()
        self.game_loop = GameLoop(window_surface, container, self)

    def start_game(self):
        main_clock = pygame.time.Clock()
        while self.game_on:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key in PLAYER_ONE_KEYS + [K_s, K_w]:
                    if event.key == K_s:
                        self.fps -= 5
                    elif event.key == K_w:
                        self.fps += 5
                    else:
                        self.current_key = event.key
                elif event.type == QUIT:
                    sys.exit(0)

            self.game_loop.perform_one_cycle([self.current_key])
            main_clock.tick(self.fps)

    def game_won(self):
        self.container.pac_man.active = False
        del self.container.ghosts[:]

    def respawn(self):
        if self.game_state.lives_left != 0:
            self.reset_objects()
            self.event_handler.add_event(REPAINT)
        else:
            self.game_on = False

    def delete_ghost(self):
        self.container.del_objects()

    def exit(self):
        self.game_on = False

    def reset_objects(self):
        self.container.del_objects()
        PacMan(2, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.score)
        self.reset_ghosts()

    def reset_ghosts(self):
        Blinky(13, 11, self.rect_matrix, self.container, self.event_handler)
        Pinky(11, 13, self.rect_matrix, self.container, self.event_handler)
        Inky(13, 13, self.rect_matrix, self.container, self.event_handler)
        Clyde(15, 13, self.rect_matrix, self.container, self.event_handler)

class EnemyGame(Game):
    def __init__(self, window_surface, container, event_handler):
        super().__init__(window_surface, container, event_handler)
        self.react_cases = {RESPAWN: self.respawn, ENEMY_RESPAWN: self.enemy_respawn,
                            GAME_OVER: self.delete_ghost, EXIT: self.exit, WON: self.game_won}

    def respawn(self):
        self.container.del_object(self.container.pac_man)
        if self.game_state.lives_left > 0:
            PacMan(2, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.score)
        else:
            self.game_on = False
        for ghost in self.container.ghosts:
            ghost.active = True
        self.event_handler.add_event(REPAINT)

    def enemy_respawn(self):
        self.container.del_object(self.container.enemy_pac_man)
        if self.game_state.enemy_lives_left > 0:
            EnemyPacMan(27, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.enemy_score)
        else:
            self.game_on = False
        self.event_handler.add_event(REPAINT)

    def reset_objects(self):
        self.container.del_objects()
        PacMan(2, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.score)
        EnemyPacMan(27, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.enemy_score)
        self.reset_ghosts()

class HumanGame(EnemyGame):
    def __init__(self, window_surface, container, event_handler):
        super().__init__(window_surface, container, event_handler)
        self.react_cases = {RESPAWN: self.respawn, ENEMY_RESPAWN: self.enemy_respawn,
                            GAME_OVER: self.delete_ghost, EXIT: self.exit, WON: self.game_won}

    def start_game(self):
        main_clock = pygame.time.Clock()
        while self.game_on:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        self.fps -= 5
                    elif event.key == K_u:
                        self.fps += 5
                    else:
                        if event.key in PLAYER_ONE_KEYS:
                            self.current_enemy_key = event.key
                        elif event.key in PLAYER_TWO_KEYS:
                            self.current_key = event.key

                elif event.type == QUIT:
                    sys.exit(0)

            self.game_loop.perform_one_cycle([self.current_key, self.current_enemy_key])
            main_clock.tick(self.fps)
        self.game_on = False

class ServerGame(EnemyGame):
    def __init__(self, window_surface, cointainer, event_handler):
        super().__init__(window_surface, cointainer, event_handler)
        self.current_key = K_RIGHT
        self.enemy_key = K_LEFT
        self.connection = network.get_connection(network.ServerConnection)
        self.connection.received_data = K_LEFT
        self.start_game()

    def start_game(self):
        main_clock = pygame.time.Clock()
        while self.game_on:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key in PLAYER_ONE_KEYS:
                    self.current_key = event.key
                elif event.type == QUIT:
                    sys.exit(0)

            self.game_loop.perform_one_cycle([self.current_key, self.enemy_key])
            self.connection.send_data((str(self.enemy_key) + str(self.current_key)))
            self.enemy_key = int(self.connection.received_data)
            main_clock.tick(45)

    def reset_objects(self):
        self.container.del_objects()
        PacMan(2, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.score)
        EnemyPacMan(27, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.score)
        self.reset_ghosts()

class ClientGame(EnemyGame):
    def __init__(self, window_surface, cointainer, event_handler):
        super().__init__(window_surface, cointainer, event_handler)
        self.current_key = K_LEFT
        self.enemy_key = K_RIGHT
        self.connection = network.get_connection(network.ClientConnection)
        self.connection.received_data = str(K_LEFT) + str(K_RIGHT)

    def start_game(self):
        main_clock = pygame.time.Clock()
        while self.game_on:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key in PLAYER_ONE_KEYS:
                    self.connection.send_data(str(event.key))
                elif event.type == QUIT:
                    sys.exit(0)

            self.current_key, self.enemy_key = parse_to_keys(self.connection.received_data)
            self.game_loop.perform_one_cycle([self.current_key, self.enemy_key])
            main_clock.tick(45)

    def reset_objects(self):
        self.container.del_objects()
        PacMan(27, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.score)
        EnemyPacMan(2, 1, self.rect_matrix, self.container, self.event_handler, self.game_state.score)
        self.reset_ghosts()

def parse_to_keys(server_response):
    return int(server_response[:3]), int(server_response[-3:])

