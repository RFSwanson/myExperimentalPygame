import pygame
from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square,self).__init__()

        self.surf = pygame.Surface((25,25))
        self.surf.fill((0,200,255))
        self.rect = self.surf.get_rect()
pygame.init()
screen = pygame.display.set_mode((800,600))
square = Square()
gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = False
    screen.blit(square.surf,square.rect)
    pygame.display.flip()
