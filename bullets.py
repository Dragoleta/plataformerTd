import pygame

class Bullets(pygame.sprite.Sprite):
    def __init__(self, pos, pos1):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = (pos,pos1))

    def update(self):
        self.rect.x += 5