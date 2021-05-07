import pygame
from player import Player
from network import Network

clientNumber = 0

def read_pos(str):
	str = str.split(",")
	return int(str[0]), int(str[1])


def make_pos(tup):
	return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win,player, player2):
	win.fill((255,255,255))
	player.draw(win)
	player2.draw(win)
	pygame.display.update()


def main():
	width = 500
	height = 500
	win = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Medieval Race v0.5")
	n = Network()
	startPos = read_pos(n.getPos())
	player = Player(startPos[0],startPos[1],100,100,(0,255,0))
	p2 = Player(0,0,100,100,(255,0,0))
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(60)
		p2Pos = read_pos(n.send(make_pos((player.x, player.y))))
		p2.x = p2Pos[0]
		p2.y = p2Pos[1]
		p2.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

		player.move()
		redrawWindow(win, player, p2)

main()