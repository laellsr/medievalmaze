import pygame
import glob

SIZE = WIDTH, HEIGHT = 900, 500
FPS = 60

def fps():
	fr = "V. 2 Fps: " + str(int(clock.get_fps()))
	frt = font.render(fr, 1, pygame.Color("coral"))
	return frt

class Warrior():
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

	def update(self):

		if self.index >= len(self.images[self.direction]):
			self.index = 0
		
		self.image = self.images[self.direction][int(self.index)]
		self.image = pygame.transform.scale(self.image, (200,200))
		

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
		

def main():
	global clock
	global font

	pygame.init()
	font = pygame.font.SysFont("Arial", 24)
	screen = pygame.display.set_mode(SIZE)
	pygame.display.set_caption("Game v.2")
	clock = pygame.time.Clock()
	
	warrior = Warrior(5, 5)
	loop = True
	
	
	while loop:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
				break
		warrior.move()
		screen.fill((0,0,0))
		screen.blit(fps(), (10, 0)) # fps na tela
		screen.blit(warrior.image, (warrior.x, warrior.y))
		screen.blit(font.render('X: '+str(warrior.x)+"\n"+'Y: '+str(warrior.y), 1, (255,255,255)),(0,200))
		# pygame.draw.rect(screen, (0,0,0), warrior.rect)
		pygame.display.update()
		
	pygame.quit()
 
if __name__ == '__main__':
	main()