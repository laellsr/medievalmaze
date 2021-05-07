import pygame
import glob
 
SIZE = WIDTH, HEIGHT = 600, 600 #the width and height of our screen
FPS = 60 #Frames per second
 
def fps():
    fr = "V. 2 Fps: " + str(int(clock.get_fps()))
    frt = font.render(fr, 1, pygame.Color("coral"))
    return frt

class MySprite(pygame.sprite.Sprite):
    def __init__(self, action):
        super(MySprite, self).__init__()
        im = glob.glob(f"png\\{action}*.png")
        lenim = len(im[0])
        self.images = [pygame.image.load(img) for img in glob.glob(f"png\\{action}*.png") if len(img) == lenim]
        self.images2 = [pygame.image.load(img) for img in glob.glob(f"png\\{action}*.png") if len(img) > lenim]
        self.images.extend(self.images2)
        self.index = 0
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1

def create_sprites():
    idle = pygame.sprite.Group(MySprite("idle"))
    walk = pygame.sprite.Group(MySprite("walk"))
    run = pygame.sprite.Group(MySprite("run"))
    jump = pygame.sprite.Group(MySprite("jump"))
    dead = pygame.sprite.Group(MySprite("dead"))
    return idle, walk, run, jump, dead

def main():
    global clock
    global font

    pygame.init()
    font = pygame.font.SysFont("Arial", 60)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Game v.2")
    idle, walk, run, jump, dead = create_sprites()
    my_group = idle
    clock = pygame.time.Clock()
    loop = 1
    while loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: my_group = walk
                if event.key == pygame.K_d: my_group = dead                
                if event.key == pygame.K_UP: my_group = jump
                if event.key == pygame.K_SPACE: my_group = idle
                if event.key == pygame.K_RIGHT: my_group = run
                if event.key == pygame.K_DOWN: my_group = dead

 
        my_group.update()
        screen.fill((0,0,0))
        my_group.draw(screen)
        screen.blit(fps(), (10, 0))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
 
if __name__ == '__main__':
    main()