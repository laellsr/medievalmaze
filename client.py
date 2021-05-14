import pygame, sys
from scenery import *
from player import Player
from network import Network
from settings import *

def fps(font, clock):
	fr = "FPS: " + str(int(clock.get_fps()))
	fr += " | You: Knight, P2: Green Knight, P3: Red Knight, P4: Blue Knight"
	frt = font.render(fr, 1, pygame.Color("yellow"))
	return frt

def set_color_mask(player, color):
	color_image = pygame.Surface(player.image.get_size())
	color_image.fill(color)
	masked_image = player.image.convert_alpha()
	masked_image.set_colorkey((0,0,0))
	masked_image.blit(color_image, (0,0), None, pygame.BLEND_RGBA_MULT)
	player.image.blit(masked_image,(0,0), None)

def redrawWindow(window, background, map_tiles, font, clock, player, player2, player3, player4):
	window.blit(background, (0,0))
	for tile in map_tiles:
		tile.draw(window)
	set_color_mask(player4, BLUE)
	player4.draw(window)
	set_color_mask(player3, RED)
	player3.draw(window)
	set_color_mask(player2, GREEN)
	player2.draw(window)
	player.draw(window)
	pygame.draw.rect(window, (255,255,255), player.rect, 1)
	window.blit(fps(font,clock), (5, 527))
	pygame.display.update()

def main():
	pygame.init()
	font = pygame.font.SysFont(None, 16, True)
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	game_map = Map()
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
	map_tiles = pygame.sprite.Group()
	for row, tiles in enumerate(game_map.data):
		for col, tile in enumerate(tiles):
			if tile == '0':
				map_tiles.add(Limit(col, row))
			elif tile == '1':
				map_tiles.add(Stone(col, row))

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
		player.move(map_tiles)
		redrawWindow(window, background, map_tiles, font, clock, player, player2, player3, player4)
		# player.move(map_tiles)
		# window.blit(background, (0,0))
		# player.draw(window)
		# pygame.draw.rect(window, (255,255,255), player.rect, 1)
		# for tile in map_tiles:
		# 	tile.draw(window)
		# pygame.display.update()

	pygame.quit()
main()