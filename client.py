import pygame, sys
from player import Player
from network import Network


def redrawWindow(window, player, player2, player3, player4):
    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    player3.draw(window)
    player4.draw(window)
    pygame.display.update()


def main():
    width = 500
    height = 500
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Medieval Race v0.5")
    network = Network()
    start_position = network.get_position()
    player = Player(start_position[0],start_position[1],100,100)
    player2 = Player(100,0,100,100)
    player3 = Player(200,0,100,100)
    player4 = Player(300,0,100,100)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(60)
        players_data = network.send((player.x, player.y))
        player2.x , player2.y = players_data[0]
        player2.update()
        player3.x , player3.y = players_data[1]
        player3.update()
        player4.x , player4.y = players_data[2]
        player4.update()
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		run = False
        		pygame.quit()
        player.move()
        redrawWindow(window, player, player2, player3, player4)
    pygame.quit()
main()