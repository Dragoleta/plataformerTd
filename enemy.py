import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((16,32))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0,0)
    
        self.walkRight = False
        self.walkLeft = False

        self.gravity = 0.3
        self.velocity = 0
        self.walkCount = 0
    
    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def update(self):
        self.applyGravity()
