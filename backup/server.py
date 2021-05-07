import socket
from _thread import *
import sys

address = ("localhost", 7777) # server and port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((address))
except socket.error as error:
    str(error)

server.listen(2) # specific number to limit connection #
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]

# def threaded_client(conn):
def threaded_client(conn, player):
    # conn.send(str.encode("Connected"))
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            # data = conn.recv(2048)
            # reply = data.decode("utf-8")
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                # print("Received: ", reply)
                # print("Sending : ", reply)

            # conn.sendall(str.encode(reply))
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = server.accept() # server input waitng for client connection
    print("Connected to:", addr)

    # start_new_thread(threaded_client, (conn,))
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1