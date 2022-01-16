"""
Medieval Maze v1
dev by Lael Santa Rosa
llsr@ic.ufal.br
"""

import pygame
from scenery import *
from player import Player
from network import Network
from settings import *

from GeneticAlgorithm import run

def get_levels(quantity: int = 2, step: int = 2):
   max_gen = quantity * step
   return run(100, 10, max_gen, 0.1, shape=(12, 48), quantity=quantity)

def fps(font, clock, level):
	txt = "FPS: " + str(int(clock.get_fps()))
	txt += " | You: Knight | Level " + str(level)
	txt_render = font.render(txt, 1, pygame.Color("black"))
	return txt_render

def set_color_mask(player, color):
	color_image = pygame.Surface(player.image.get_size())
	color_image.fill(color)
	masked_image = player.image.convert_alpha()
	masked_image.set_colorkey((0,0,0))
	masked_image.blit(color_image, (0,0), None, pygame.BLEND_RGBA_MULT)
	player.image.blit(masked_image,(0,0), None)

def redrawWindow(window, background, map_tiles, font, clock, player, level):
	window.blit(background, (0,0))
	for tile in map_tiles:
		tile.draw(window)
	player.draw(window)
	window.blit(fps(font,clock,level), (5, 527))
	pygame.display.update()

def mapTiles(gameMap):
	map_tiles = pygame.sprite.Group()
	final_tiles = pygame.sprite.Group()
	line_size = len(gameMap.data[0])
	for row, tiles in enumerate(gameMap.data):
		for col, tile in enumerate(tiles):
			if (tile == 1) or (col == 0 and tile != 3) or (col == line_size-1 and tile != -1 and tile != 3):
				map_tiles.add(Stone(col, row))
			elif tile == 3:
				map_tiles.add(Limit(col, row))
			elif tile == -1:
				final_tiles.add(Final(col, row))
	return map_tiles, final_tiles

def main():
	pygame.init()
	font = pygame.font.SysFont(None, 16, True)
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	background = pygame.image.load("assets/background/background_1.png")
	background = pygame.transform.scale(background, (3840//4,2160//4))
	pygame.display.set_caption(TITLE)

	player = Player(X_INITIAL,Y_INITIAL,PLAYER_WIDTH,PLAYER_HEIGHT)
	clock = pygame.time.Clock()

	game_level = 0
	mazes = get_levels(MAX_MAPS)
	gameMap = Map(mazes[game_level])
	map_tiles, final_tiles = mapTiles(gameMap)
	
	run = True
	while run:
		clock.tick(FPS)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
		player.move(map_tiles)
		
		for tile in final_tiles:
			if player.rect.colliderect(tile):
				game_level += 1
				if game_level == MAX_MAPS:
					win_or_lose = pygame.font.SysFont(None, 60, True)
					game_over_message = "Congratulations, you win!"
					while True:
						window.blit(background, (0,0))
						window.blit(win_or_lose.render(game_over_message, 1, pygame.Color("white")), (160, 250))
						pygame.display.update()
				gameMap = Map(mazes[game_level])
				map_tiles, final_tiles = mapTiles(gameMap)
				player.x, player.y = X_INITIAL, Y_INITIAL
		
		redrawWindow(window, background, map_tiles, font, clock, player, game_level+1)
	pygame.quit()
main()