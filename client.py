import pygame, sys
from player import Player
from network import Network


def redrawWindow(window, background, player, player2, player3, player4):
    window.blit(background, (0,0))
    player.draw(window)
    player2.draw(window)
    player3.draw(window)
    player4.draw(window)
    pygame.display.update()


def main():
    width = 800
    height = 500
    sprite_width = 50
    sprite_height = 50
    window = pygame.display.set_mode((width, height))
    background = pygame.image.load("assets/background/background_1.png")
    background = pygame.transform.scale(background, (3840//4,2160//4))
    pygame.display.set_caption(" Medieval Maze v1 ")
    network = Network()
    start_position = network.get_position()
    player = Player(start_position[0],start_position[1],sprite_width,sprite_height)
    player2 = Player(100,0,sprite_width,sprite_height)
    player3 = Player(200,0,sprite_width,sprite_height)
    player4 = Player(300,0,sprite_width,sprite_height)
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
        redrawWindow(window, background, player, player2, player3, player4)
    pygame.quit()
main()