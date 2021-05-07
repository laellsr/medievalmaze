import pygame
import glob
 
SIZE = WIDTH, HEIGHT = 900, 900 #the width and height of our screen
FPS = 60 #Frames per second
 
def fps():
    fr = "V. 2 Fps: " + str(int(clock.get_fps()))
    frt = font.render(fr, 1, pygame.Color("coral"))
    return frt

class Warrior(pygame.sprite.Sprite):
    def __init__(self, action, x, y):
        super(Warrior, self).__init__()
        self.images = [pygame.image.load(img) for img in glob.glob(f"assets/warrior1/{action}*.png")]
        self.index = 0
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 50, 50)

    def update(self, x, y):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]
        self.image = pygame.transform.scale(self.image, (200,200))
        self.index += 0.15
        self.x += x
        self.y += y
        self.rect = (self.x, self.y, 50, 50)

def create_sprites():
    down = pygame.sprite.Group(Warrior("d_", 5, 5))
    left = pygame.sprite.Group(Warrior("l_", 5, 5))
    right = pygame.sprite.Group(Warrior("r_", 5, 5))
    up = pygame.sprite.Group(Warrior("u_", 5, 5))
    return down, left, right, up

def main():
    global clock
    global font

    pygame.init()
    font = pygame.font.SysFont("Arial", 60)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Game v.2")
    down, left, right, up  = create_sprites()
    my_group = down
    clock = pygame.time.Clock()
    loop = True
    while loop:
        x=0
        y=0
        for event in pygame.event.get():
            x=0
            y=0
            if event.type == pygame.QUIT:
                loop: False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    my_group = left
                    x=-3               
                if event.key == pygame.K_UP:
                    my_group = up
                    x=3
                if event.key == pygame.K_RIGHT:
                    my_group = right
                    y=3
                if event.key == pygame.K_DOWN:
                    my_group = down
                    y=-3
            my_group.update(x, y)
            
        screen.fill((0,0,0))
        my_group.draw(screen)
        screen.blit(fps(), (10, 0))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
 
if __name__ == '__main__':
    main()