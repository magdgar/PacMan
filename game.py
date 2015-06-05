import socket
import pygame
from pygame.constants import KEYDOWN, K_RIGHT, K_LEFT
from pygame.threads import Thread
from events.eventhandler import add_event
from events.eventobserver import EventObserver
from game_engine.gameengine import GameEngine
from gameloop.gameloop import GameLoop
from gamestate.gamestate import GameState
from objects.blinky import Blinky
from objects.clyde import Clyde
from objects.Container import del_objects
from objects.pacman import PacMan
from objects.pinky import Pinky
from objects.inky import Inky

class Game(EventObserver):
    def __init__(self, window_surface):
        super().__init__()
        self.score = 0
        self.current_key = K_LEFT
        self.current_enemy_key = K_RIGHT
        self.react_cases = {"RESPAWN": self.respawn, "GAMEOVER": self.delete_ghost, "EXIT": self.exit}
        self.game_on = True
        self.window_surface = window_surface
        self.paused = False
        self.game_state = GameState()
        self.game_loop = GameLoop(window_surface, GameEngine(window_surface), self)
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

    def respawn(self):
        if self.game_state.lives_left != 0:
            self.reset_objects()
            add_event("REPAINT")

    def delete_ghost(self):
        del_objects()

    def exit(self):
        self.game_on = False

    def reset_objects(self):
        del_objects()
        PacMan(2, 1)
        Blinky(13, 11)
        Pinky(11, 13)
        Inky(13, 13)
        Clyde(15, 13)

class ServerGame(Game):
    def __init__(self, window_surface):
        super().__init__(window_surface)
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.current_key = K_RIGHT
        self.enemy_key  = K_LEFT
        self.connection = None
        self.start_server()

    def start_server(self):
        self.serversocket.bind(('', 4444))
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
        del_objects()
        PacMan(2, 1)
        PacMan(27, 1)
        Blinky(13, 11)
        Pinky(11, 13)
        Inky(13, 13)
        Clyde(15, 13)

class ClientGame(Game):
    def __init__(self, window_surface):
        super().__init__(window_surface)
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.current_key = K_LEFT
        self.enemy_key  = K_RIGHT
        self.start_client()

    def start_client(self):
        self.clientsocket.connect(('25.122.171.23', 4444))
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
        del_objects()
        PacMan(27, 1)
        PacMan(2, 1)
        Blinky(13, 11)
        Pinky(11, 13)
        Inky(13, 13)
        Clyde(15, 13)



def parse_to_keys(server_response):
    return int(server_response[:3]), int(server_response[-3:])

