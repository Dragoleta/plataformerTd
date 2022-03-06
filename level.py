import pygame
from settings import *
from player import Player
from enemy import Enemy
from tiles import Tile
from bullets import Bullets


class Level:
    def __init__(self, surface, levelMap):
        self.displaySurface = surface
        self.setupLevel(levelMap)
        self.worldShift = 0
        self.currentX = 0

    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.GroupSingle()
        self.bullets = pygame.sprite.Group()

        for colIndex, col in enumerate(layout):
            for rowIndex, cel in enumerate(col):
                x = rowIndex * tileSize
                y = colIndex * tileSize
                if cel == "X":
                    tile = Tile(self.displaySurface, (x, y))
                    self.tiles.add(tile)
                
        enemySprite = Enemy((10, 10))
        self.enemy.add(enemySprite)

        playerSprite = Player((10, 10))
        self.player.add(playerSprite)

    def horizontalMovementColision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.playerSpeed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.onLeft = True
                    self.currentX = player.rect.left

                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.onRight = True
                    self.currentX = player.rect.right

        if player.onLeft and (player.rect.left < self.currentX or player.direction.x >= 0):
            player.onLeft = False
        if player.onRight and (player.rect.right > self.currentX or player.direction.x <= 0):
            player.onRight = False

    def verticalMovementColision(self):
        player = self.player.sprite
        player.applyGravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.onGround = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.onCeiling = True

        if player.onGround and player.direction.y < 0 or player.direction.y > 1:
            player.onGround = False
        if player.onCeiling and player.direction.y > 0:
            player.onCeiling = False

    def verticalEnemyColision(self):
        enemy = self.enemy.sprite
        enemy.applyGravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(enemy.rect):
                if enemy.direction.y > 0:
                    enemy.rect.bottom = sprite.rect.top
                    enemy.direction.y = 0
                elif enemy.direction.y < 0:
                    enemy.rect.top = sprite.rect.bottom
                    enemy.direction.y = 0
   
    def scrollX(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        directionX = player.direction.x

        if playerX < winWidth//2 and directionX < 0:
            self.worldShift = 3
            player.playerSpeed = 0
        elif playerX > winWidth//2 and directionX > 0:
            self.worldShift = -3
            player.playerSpeed = 0
        else:
            self.worldShift = 0
            player.playerSpeed = 3

    def createBullet(self):
        player = self.player.sprite
        return Bullets(player.rect.x, player.rect.y)

    def shoot(self):
        self.bullets.add(self.createBullet())

    def run(self):
        # tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        self.scrollX()

        # colisions
        self.horizontalMovementColision()
        self.verticalMovementColision()
        self.verticalEnemyColision()
        

        # player
        self.player.update()
        self.player.draw(self.displaySurface)

        # enemy
        self.enemy.update()
        self.enemy.draw(self.displaySurface)

        self.bullets.draw(self.displaySurface)
        self.bullets.update()
