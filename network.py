import socket, pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 7777
        self.addr = (self.server, self.port)
        self.position = self.connect()

    def get_position(self):
        return self.position

    def connect(self):
        try:
            self.client.connect(self.addr)
            initial_position = pickle.loads(self.client.recv(2048))
            return initial_position
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)