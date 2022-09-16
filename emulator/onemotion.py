"""
# Author: Acxel Orozco
# Date: 10/09/2022
# Description: Ball elastic collision excersice
# Using pygame
"""
import pygame
from pygame.locals import *
import sys

from emulator.mysprites.ball import Ball
from emulator.mysprites.metrical import Metrical


class OneMotion:

    def __init__(self, width: int, height: int):
        # Start pygame
        pygame.init()

        # Surface
        # screen = pygame.display.set_mode((640, 480))
        screen = pygame.display.set_mode((width, height))
        width = screen.get_width()
        height = screen.get_height()
        # Title
        pygame.display.set_caption('Ball collision')
        self.messure = Metrical()
        self.ball1 = Ball(
            screen,
            'Ball1',
            "emulator/assets/sprites/pydroball.png",
            40,
            0.0,
            False,
            1.0,
            x=0,
            y=height / 2
        )

        # Define initial position using karg
        self.ball2 = Ball(
            screen,
            'Ball2',
            "emulator/assets/sprites/pydroball.png",
            40,
            1.0,
            True,
            1.0,
            x=width / 2,
            y=height / 2
        )

    def main(self):
        status = True
        # ball2.control(width / 2, height / 2)
        self.ball1.update()
        self.ball2.update()
        # speed1 = [4, 7]
        speed1 = [10, 0]

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    # Space key
                    if event.key == K_SPACE:
                        status = True
                    # Supr key
                    if event.key == K_DELETE:
                        status = False
            if status:
                self.ball1.motion("white", speed1, 15)
                self.ball2.quiet()
            if pygame.sprite.collide_rect(self.ball1, self.ball2):
                velocity = self.messure.elastic_collision(
                    self.ball1.props,
                    self.ball2.props
                )
                print("velocity result:", velocity)
                print(velocity['v1'])
                print(velocity['v2'])
                self.AfterColl(velocity)
                status = False

    def AfterColl(self, velocity: dict):

        status = True
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    # Space key
                    if event.key == K_SPACE:
                        status = True
                    # Supr key
                    if event.key == K_DELETE:
                        status = False
            if status:
                self.ball2.motion("white", velocity['v2'], 15)
                self.ball1.motion("white", velocity['v1'], 15)
            if pygame.sprite.collide_rect(self.ball1, self.ball2):
                velocity = self.messure.elastic_collision(
                    self.ball1.props,
                    self.ball2.props
                )
                print("velocity result:", velocity)
                print(velocity['v1'])
                print(velocity['v2'])
                self.AfterColl(velocity)
                status = False
