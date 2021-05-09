import pygame, sys
from scenery import Map, Camera, Wall
from player import Player
from network import Network
from settings import *

def redrawWindow(window, background, player, player2, player3, player4):
    window.blit(background, (0,0))
    player.draw(window)
    player2.draw(window)
    player3.draw(window)
    player4.draw(window)
    pygame.display.update()


def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    game_map = Map()
    camera = Camera(game_map.width, game_map.height)
    background = pygame.image.load("assets/background/background_1.png")
    background = pygame.transform.scale(background, (3840//4,2160//4))
    pygame.display.set_caption(TITLE)
    network = Network()
    start_position = network.get_position()
    player = Player(start_position[0],start_position[1],PLAYER_WIDTH,PLAYER_HEIGHT)
    player2 = Player(100,0,PLAYER_WIDTH,PLAYER_HEIGHT)
    player3 = Player(200,0,PLAYER_WIDTH,PLAYER_HEIGHT)
    player4 = Player(300,0,PLAYER_WIDTH,PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    walls = pygame.sprite.Group()
    for row, tiles in enumerate(game_map.data):
        for col, tile in enumerate(tiles):
            if tile == '1':
                Wall(walls, col, row)

    run = True
    while run:
        clock.tick(FPS)
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
        camera.update(player)
        redrawWindow(window, background, player, player2, player3, player4)
    pygame.quit()
main()