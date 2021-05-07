import pygame
import glob

class Player():
	def __init__(self, x, y, width, height):
		self.images = {"UP": [pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{'u_'}*.png")], "DOWN":[pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{'d_'}*.png")], "LEFT": [pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{'l_'}*.png")], "RIGHT": [pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{'r_'}*.png")] }	
		self.direction = 'DOWN'
		self.index = 0
		self.image = self.images[self.direction][int(self.index)]
		self.image = pygame.transform.scale(self.image, (200,200))
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = pygame.Rect(self.x, self.y, width, height)
		self.vel = 3

	def draw(self, window):
		window.blit(self.image, (self.x, self.y))

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and self.x > -58:
			self.x -= self.vel
			self.direction = "LEFT"
			self.index += 0.15
		if keys[pygame.K_RIGHT] and self.x < 755:
			self.x += self.vel
			self.direction = "RIGHT"
			self.index += 0.15
		if keys[pygame.K_UP] and self.y > -44:
			self.y -= self.vel
			self.direction = "UP"
			self.index += 0.15
		if keys[pygame.K_DOWN] and self.y < 341:
			self.y += self.vel
			self.direction = "DOWN"
			self.index += 0.15
		self.update()

	def update(self):
		if self.index >= len(self.images[self.direction]):
			self.index = 0
		self.image = self.images[self.direction][int(self.index)]
		self.image = pygame.transform.scale(self.image, (100,100))