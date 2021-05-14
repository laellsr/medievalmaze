import pygame
from settings import *

class Map:
    def __init__(self):
        self.data = []
        with open("settings/map.txt", 'rt') as file:
            for line in file:
                self.data.append(line.strip())

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * TILESIZE
        self.height = self.tile_height * TILESIZE

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.set_alpha(0) # 0-255
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Stone(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('assets/objects/stones_1.png')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.image.set_alpha(255)

class Limit(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)