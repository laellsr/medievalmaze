import pygame
# from os import path
from settings import *

class Map:
    def __init__(self):
        self.data = []
        # self.game_dir =  path.dirname(path.realpath(__file__))
        # self.map_dir = path.join(self.game_dir, "/settings/map.txt")
        with open("settings/map.txt", 'rt') as file:
            for line in file:
                self.data.append(line.strip())

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * TILESIZE
        self.height = self.tile_height * TILESIZE

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))