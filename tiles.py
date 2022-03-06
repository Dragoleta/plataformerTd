import pygame
from settings import tileSize

class Tile(pygame.sprite.Sprite):
    def __init__(self, surface, pos):
        super().__init__()
        self.image = pygame.Surface((tileSize, tileSize))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, xShift):
        self.rect.x += xShift