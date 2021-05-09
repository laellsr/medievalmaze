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
                self.data.append(line)

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * TILESIZE
        self.height = self.tile_height * TILESIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)

class Wall(pygame.sprite.Sprite):
    def __init__(self, walls, x, y):
        self.groups = walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE