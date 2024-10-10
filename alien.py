import pygame
 
from pygame.sprite import Sprite
 
class Alien(Sprite):
 
    def __init__(self,ia_game):
        super().__init__()
        self.screen = ia_game.screen
        self.settings=ia_game.settings
 
        self.image = pygame.image.load('imagens/alien.bmp')
        self.rect = self.image.get_rect()
 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        self.x+=self.settings.velocidade_alien
        self.rect.x=self.x
 