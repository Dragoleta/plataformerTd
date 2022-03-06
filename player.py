import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((16, 32))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

        # player movements
        self.direction = pygame.math.Vector2(0, 0)
        self.jumpHeight = -5
        self.playerSpeed = 3
        self.gravity = 0.2

        # player state machine
        self.onGround = False
        self.onCeiling = False
        self.onRight = False
        self.onLeft = False

    def jump(self):
        self.direction.y = self.jumpHeight

    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def getInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.onGround:
            self.jump()

    def update(self):
        self.getInput()
