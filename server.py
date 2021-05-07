import socket
from _thread import *
import sys

address = ("localhost", 7777)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	server.bind((address))
except socket.error as error:
	str(error)

server.listen(3)
print("Waiting for a connection, Server Started")

def read_position(str):
	str = str.split(",")
	return int(str[0]), int(str[1])


def make_position(tup):
	return str(tup[0]) + "," + str(tup[1])

position = [(0,0),(100,100),(200,200)]


def threaded_client(conn, player):
	conn.send(str.encode(make_position(position[player])))
	reply = ""
	while True:
		try:
			data = read_position(conn.recv(2048).decode())
			position[player] = data

			if not data:
				print("Disconnected")
				break
			else:
				if player == 1:
					reply = position[0]
				else:
					reply = position[1]

			conn.sendall(str.encode(make_position(reply)))
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