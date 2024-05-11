import pygame
from pygame.locals import *
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

clock = pygame.time.Clock()
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf=pygame.Surface((25,25))
        self.surf.fill((0,200,255))
        self.rect = self.surf.get_rect()
        self.x = self.rect.x

        

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
square = Square()
moving_right = False
moving_left = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(square.surf,square.rect)#arguments: source,destination
    #places the source(=surf) at destination(=rect)where rect is top left
    pygame.display.update()

                
            