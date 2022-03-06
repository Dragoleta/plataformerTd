import pygame, sys
from level import Level
from settings import *

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((winWidth, winHeight))
level = Level(win, levelMap)

def main(): 
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    level.shoot()
        win.fill('black')
        level.run()
        pygame.display.update()


if __name__ == "__main__":
    main()
