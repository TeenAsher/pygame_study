# --------------------------------------
# Fourth file with random pygame practice
# TeenAsher
# --------------------------------------
import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()

screen = pygame.display.set_mode((1920, 1080), FULLSCREEN, 32)
screen.fill((35, 10, 10))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                for i in range(1000):
                    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
                    rand_pos = (randint(0, 1919), randint(0, 1079))
                    screen.set_at(rand_pos, rand_col)

        if event.type == KEYUP:
            if event.key == K_a:
                screen.fill((35, 10, 10))

        pygame.display.update()