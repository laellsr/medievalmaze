import pygame
from player import Player
from network import Network

clientNumber = 0

def read_position(str):
	str = str.split(",")
	return int(str[0]), int(str[1])


def make_position(tup):
	return str(tup[0]) + "," + str(tup[1])


def redrawWindow(window, player, player2):
	window.fill((255,255,255))
	player.draw(window)
	player2.draw(window)
	pygame.display.update()


def main():
	width = 500
	height = 500
	window = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Medieval Race v0.5")
	network = Network()
	start_position = read_position(network.get_position())
	player = Player(start_position[0],start_position[1],100,100)
	player2 = Player(0,0,100,100)
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(60)
		player2_position = read_position(network.send(make_position((player.x, player.y))))
		player2.x = player2_position[0]
		player2.y = player2_position[1]
		player2.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

		player.move()
		redrawWindow(window, player, player2)

main()