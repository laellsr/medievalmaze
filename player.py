import pygame,glob, sys
from settings import *
class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		self.images = {"UP": [pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{'cu_'}*.png")], "DOWN":[pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{'cd_'}*.png")], "LEFT": [pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{'cl_'}*.png")], "RIGHT": [pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{'cr_'}*.png")] }	
		self.direction = 'DOWN'
		self.index = 0
		self.image = self.images[self.direction][int(self.index)]
		self.image = pygame.transform.scale(self.image, (width,height))
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		# self.rect = pygame.Rect(self.x, self.y, width//2, height//2)
		self.rect = self.image.get_rect(center = (width, height))

		self.vel = 3
		self.index_vel = 0.15

	def draw(self, window):
		window.blit(self.image, (self.x, self.y))

	def move(self, tiles):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.direction = "LEFT"
			self.x -= self.vel
			if not self.collide_with_tiles(tiles, self.direction):
				self.index += self.index_vel
			else:
				self.x += self.vel
		if keys[pygame.K_RIGHT]:
			self.direction = "RIGHT"
			self.x += self.vel
			if not self.collide_with_tiles(tiles, self.direction):
				self.index += self.index_vel
			else:
				self.x -= self.vel
		if keys[pygame.K_UP]:
			self.direction = "UP"
			self.y -= self.vel
			if not self.collide_with_tiles(tiles, self.direction):
				self.index += self.index_vel
			else:
				self.y += self.vel
		if keys[pygame.K_DOWN]:
			self.direction = "DOWN"
			self.y += self.vel
			if not self.collide_with_tiles(tiles, self.direction):
				self.index += self.index_vel
			else:
				self.y -= self.vel
	
		self.update()

	def get_hits(self, tiles):
		hits = []
		for tile in tiles:
			if self.rect.colliderect(tile):
				hits.append(tile)
		return hits

	def collide_with_tiles(self, tiles, direction):
		# collisions = self.get_hits(tiles)
		temp_rect = self.rect
		temp_rect.x = self.x
		temp_rect.y = self.y
		for tile in tiles:
			if temp_rect.colliderect(tile):
				# print("collide")
				# print(self.rect, self.rect.x, self.rect.y, self.x, self.y)
				# print(tile.rect, tile.rect.x, tile.rect.y)
				return True
		return False

	def update(self):
		if self.index >= len(self.images[self.direction]):
			self.index = 0
		self.image = self.images[self.direction][int(self.index)]
		self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH,PLAYER_HEIGHT))
		self.rect.x = self.x
		self.rect.y = self.y