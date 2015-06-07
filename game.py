import socket
import pygame
from events.eventconstans import *
from pygame.constants import KEYDOWN, K_RIGHT, K_LEFT
from pygame.threads import Thread
from events.eventobserver import EventObserver
from game_engine.gameengine import GameEngine
from gameloop.gameloop import GameLoop
from gamestate.gamestate import GameState
from media.constans import LEVEL_MAP, ACTUAL_LVL
from media.matrix import RectMatrix
from objects.blinky import Blinky
from objects.clyde import Clyde
from objects.pacman import PacMan
from objects.pinky import Pinky
from objects.inky import Inky
HOST = ''
PORT = 4444

class Game(EventObserver):
    def __init__(self, window_surface, container, event_handler):
        super().__init__(container, event_handler)
        self.rect_matrix = RectMatrix(ACTUAL_LVL)
        self.score = 0
        self.current_key = K_LEFT
        self.current_enemy_key = K_RIGHT
        self.react_cases = {RESPAWN: self.respawn, GAME_OVER: self.delete_ghost, EXIT: self.exit, WON: self.game_won}
        self.game_on = True
        self.window_surface = window_surface
        self.paused = False
        self.game_state = GameState(container, event_handler)
        self.game_loop = GameLoop(window_surface, container, self)
        self.mainClock = pygame.time.Clock()
        self.reset_objects()

    def start_game(self):
        while self.game_on:
            for event in pygame.event.get():
               if event.type == KEYDOWN:
                   self.current_key = event.key
            self.game_loop.perform_one_cycle([self.current_key])
            self.mainClock.tick(60)

    def add_points(self, number):
        self.score += number

    def game_won(self):
        self.container.pac_man.active = False
        for object in self.container.ghosts:
            for key, animation in object.animations.items():
                animation.pause()

    def respawn(self):
        if self.game_state.lives_left != 0:
            self.reset_objects()
            self.event_handler.add_event(REPAINT)

    def delete_ghost(self):
        self.container.del_objects()

    def exit(self):
        self.game_on = False

    def reset_objects(self):
        self.container.del_objects()
        PacMan(2, 1, self.rect_matrix, self.container, self.event_handler)
        Blinky(13, 11, self.rect_matrix, self.container, self.event_handler)
        Pinky(11, 13, self.rect_matrix, self.container, self.event_handler)
        Inky(13, 13, self.rect_matrix, self.container, self.event_handler)
        Clyde(15, 13, self.rect_matrix, self.container, self.event_handler)

class ServerGame(Game):
    def __init__(self, window_surface, cointainer, event_handler):
        super().__init__(window_surface, cointainer, event_handler)
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.current_key = K_RIGHT
        self.enemy_key  = K_LEFT
        self.connection = None
        self.start_server()

    def start_server(self):
        self.serversocket.bind(('', PORT))
        self.serversocket.listen(1)
        self.connection, address = self.serversocket.accept()
        print("connected from " + str(address))
        th = Thread(target=self.recive_data)
        th.daemon = True
        th.start()

    def start_game(self):
        while self.game_on:
            for event in pygame.event.get():
               if event.type == KEYDOWN:
                   self.current_key = event.key
            self.game_loop.perform_one_cycle([self.current_key, self.enemy_key])
            self.send_data()
            self.mainClock.tick(50)

    def send_data(self):
        try:
            self.connection.send((str(self.enemy_key) + str(self.current_key)).encode())
        except:
            print("ERR")
            pass

    def recive_data(self):
        while True:
            try:
                self.enemy_key = int(self.connection.recv(1024).decode())
            except:
                print("ERR")
                pass

    def reset_objects(self):
        self.container.del_objects()
        PacMan(2, 1, self.rect_matrix, self.container, self.event_handler)
        PacMan(27, 1, self.rect_matrix, self.container, self.event_handler)
        Blinky(13, 11, self.rect_matrix, self.container, self.event_handler)
        Pinky(11, 13, self.rect_matrix, self.container, self.event_handler)
        Inky(13, 13, self.rect_matrix, self.container, self.event_handler)
        Clyde(15, 13, self.rect_matrix, self.container, self.event_handler)

class ClientGame(Game):
    def __init__(self, window_surface, cointainer, event_handler):
        super().__init__(window_surface, cointainer, event_handler)
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.current_key = K_LEFT
        self.enemy_key  = K_RIGHT
        self.start_client()

    def start_client(self):
        self.clientsocket.connect((HOST, PORT))
        th = Thread(target=self.recive_data)
        th.daemon = True
        th.start()

    def send_data(self):
        try:
            self.clientsocket.send(str(self.current_key).encode())
        except:
            print("ERR")
            pass

    def recive_data(self):
        while True:
            try:
                self.current_key, self.enemy_key = parse_to_keys(self.clientsocket.recv(1024).decode())
            except:
                print("ERR")
                pass

    def start_game(self):
        while self.game_on:
            for event in pygame.event.get():
               if event.type == KEYDOWN:
                   self.clientsocket.send(str(event.key).encode())
            self.game_loop.perform_one_cycle([self.current_key, self.enemy_key])
            self.mainClock.tick(50)

    def reset_objects(self):
        self.container.del_objects()
        PacMan(27, 1, self.rect_matrix, self.container, self.event_handler)
        PacMan(2, 1, self.rect_matrix, self.container, self.event_handler)
        Blinky(13, 11, self.rect_matrix, self.container, self.event_handler)
        Pinky(11, 13, self.rect_matrix, self.container, self.event_handler)
        Inky(13, 13, self.rect_matrix, self.container, self.event_handler)
        Clyde(15, 13, self.rect_matrix, self.container, self.event_handler)

def parse_to_keys(server_response):
    return int(server_response[:3]), int(server_response[-3:])

