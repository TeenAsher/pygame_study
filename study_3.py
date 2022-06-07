# --------------------------------------
# Third file with random pygame practice
# TeenAsher
# --------------------------------------
import pygame
from pygame.locals import *
import sys
import random

pygame.init()

screen = pygame.display.set_mode((1920, 1080), FULLSCREEN, 32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        screen.fill((10, 10, 45))
        pygame.draw.circle(screen, (255, 250, 50), (1200, 200), 100)
        pygame.draw.circle(screen, (10, 10, 45), (1150, 200), 90)

        for i in range(200):
            x = random.randint(0, 2047)
            y = random.randint(0, 1079)
            z = random.randrange(1, 8)
            pygame.draw.circle(screen, (255, 250, 100), (x, y), z)

        pygame.mouse.set_visible(False)

        pygame.display.update()