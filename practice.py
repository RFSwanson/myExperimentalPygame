import pygame
from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square,self).__init__()

        self.surf = pygame.Surface((25,25))
        self.surf.fill((0,200,255))
        self.rect = self.surf.get_rect()
    def update(self,pressed_keys):
        if pressed_keys[K_RIGHT] and self.rect.right < 800:
            self.rect.move_ip(1,0)
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-1,0)

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
    pressed_keys = pygame.key.get_pressed()
    square.update(pressed_keys)
    screen.fill((255,255,255))
    screen.blit(square.surf,square.rect)
    pygame.display.flip()