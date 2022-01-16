import pygame
import os
from MedievalMaze.settings import *

class Map:
    def __init__(self, maze):

        self.data = []

        limit_line = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        walk_line = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        for i in range(0, 10):
            self.data.append(limit_line)

        # for maze in mazes:
        #     for line in maze:
        #         self.data.append(line)

        for line in maze:
            self.data.append(line)

        self.data.append(limit_line)

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

class Limit(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

class Stone(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH_TO_ASSETS, 'objects/Brick_01.png'))
        self.image = pygame.transform.scale(self.image, (27,27))
        self.image.set_alpha(255)

class Final(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.set_alpha(255)

class Greenery(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH_TO_ASSETS, 'objects/greenery_2.png'))
        self.image = pygame.transform.scale(self.image, (28,44))
        self.image.set_alpha(255)

class Plaque(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH_TO_ASSETS, 'objects/Sign_01.png'))
        self.image = pygame.transform.scale(self.image, (33,33))
        self.image.set_alpha(255)

class Barrel(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH_TO_ASSETS, 'objects/decor_17.png'))
        self.image = pygame.transform.scale(self.image, (22,24))
        self.image.set_alpha(255)

class Statue(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH_TO_ASSETS, 'objects/Decor_Statue.png'))
        self.image = pygame.transform.scale(self.image, (60,60))
        self.image.set_alpha(255)

class Goblin(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH_TO_ASSETS, 'goblin/goblin_11.png'))
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (160,160))
        self.image.set_alpha(255)