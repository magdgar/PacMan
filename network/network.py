import socket
from threading import Thread

HOST = 'localhost'
PORT = 4444

def get_connection(connection_type):
    if connection_type is ServerConnection:
        return ServerConnection()
    elif connection_type is ClientConnection:
        return ClientConnection()
    else:
        raise Exception("wrong connection type")

class Connection:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = None
        self.address = None
        self.received_data = None
        self.start_connection()

    def start_connection(self):
        pass

    def receive_data(self):
        while True:
            try:
                if isinstance(self, ServerConnection):
                    self.received_data = self.connection.recv(1024).decode()
                elif isinstance(self, ClientConnection):
                    self.received_data = self.socket.recv(1024).decode()
            except:
                raise Exception("error receiving data")
                pass

    def send_data(self, args):
        try:
            if isinstance(self, ServerConnection):
                self.connection.send(str(args).encode())
            elif isinstance(self, ClientConnection):
                self.socket.send(str(args).encode())
        except:
            raise Exception("error sending data")
            pass


class ServerConnection(Connection):
    def start_connection(self):
        self.socket.bind(('', PORT))
        self.socket.listen(1)
        self.connection, address = self.socket.accept()
        print("connected from " + str(address))
        print(self.connection.__str__())
        th = Thread(target=self.receive_data)
        th.daemon = True
        th.start()


class ClientConnection(Connection):
    def start_connection(self):
        self.socket.connect((HOST, PORT))
        th = Thread(target=self.receive_data)
        th.daemon = True
        th.start()
