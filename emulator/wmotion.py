"""
# Author: Acxel Orozco
# Date: 10/09/2022
# Description: Ball elastic collision excersice
# Using pygame
"""
import pygame
from pygame.locals import *
import random
import sys

from mysprites.ball import Ball


def main():

    # Start pygame
    pygame.init()

    # Surface
    screen = pygame.display.set_mode((640, 480))
    width = screen.get_width()
    height = screen.get_height()
    status = True
    # Title
    pygame.display.set_caption('Ball collision')

    ball1 = Ball(screen, "assets/sprites/pydroball.png")
    ball2 = Ball(screen, "assets/sprites/pydroball.png")
    ball2.control(width / 2, height / 2)
    ball2.update()
    speed = [4, 7]
    speed2 = [7, 1]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # Space key
                if event.key == K_SPACE:
                    ball1.motion("white", speed, 15)
                    ball2.motion("white", speed2, 15 / 2)
                # Supr key
                if event.key == K_DELETE:
                    status = False
        if status:
            ball1.motion("white", speed, 15)
            ball2.motion("white", speed2, 15)
            if pygame.sprite.collide_rect(ball1, ball2):
                ball1.update()
                ball2.update()
                ball1.collision()
                ball2.collision()
                # status = False


if __name__ == '__main__':
    main()
