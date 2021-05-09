import socket, pickle
from _thread import *

address = ("localhost", 7777)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((address))
except socket.error as error:
    str(error)

server.listen(4)
print("Welcome to Medieval Maze Server!")
print("Waiting for a connection...")

position = [(0,0),(100,0),(200,0),(300,0)]

def threaded_client(conn, player):
    conn.send(pickle.dumps(position[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            position[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = [position[0], position[2], position[3]]
                elif player == 2:
                    reply = [position[0], position[1], position[3]]
                elif player == 3:
                    reply = [position[0], position[1], position[2]]
                elif player == 0:
                    reply = [position[1], position[2], position[3]]
            
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

current_player = 0
while True:
    conn, addr = server.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1