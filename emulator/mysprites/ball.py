"""
# Author: Acxel Orozco
# Date: 10/09/2022
"""
import pygame
import random


class Ball(pygame.sprite.Sprite):

    """
    Ball class
    """

    def __init__(
        self,
        screen,
        name: str,
        img_url: str,
        radius: float,
        k_hooke: float,
        quiet: bool,
        mass: float,
        **kargs
    ):
        pygame.sprite.Sprite.__init__(self)
        # Initial values
        self.movex = 0
        self.movey = 0
        self.frames = 0
        # Screen dimensions
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.screen = screen
        pygame.time.Clock().tick(0)
        # Color dict
        self.colors = {
            "blue": (0, 0, 180),
            "black": (0, 0, 0),
            "green": (0, 255, 0),
            "red": (255, 0, 0),
            "white": (255, 255, 255)
        }
        # Object info dict
        self.props = {
            'id': random.randrange(1, round(10**23), 1),
            'name': 'ball',
            'radius': 0.1,
            'k_hooke': 0.0,
            'quiet': False,
            'mass': 0.0,
            'acceleration_i': 0.0,
            'acceleration_f': 0.0,
            'width': 0,
            'height': 0,
            'x': 0,
            'y': 0,
            'screen_color': '',
            'speed_i': [],
            'speed_f': [],
            'speed_dir': [1, 1],
            'clock_time': 0
        }
        self.props_metric = {
            'id': 'int',
            'radius': 'm',
            'k_hooke': 'N/m',
            'quiet': 'bool',
            'mass': 'kg',
            'acceleration_i': 'm/(s**2)',
            'acceleration_f': 'm/(s**2)',
            'width': 'm',
            'height': 'm',
            'x': 'm',
            'y': 'm',
            'screen_color': '',
            'speed_i': '[m/s, m/s]',
            'speed_f': '[m/s, m/s]',
            'speed_dir': [
                '1: left toward right' or '0: right toward left'
                '1: down toward up' or '0: up toward down'
            ],
            'clock_time': 'FPS'
        }
        self.props['name'] = name
        self.props['radius'] = radius
        self.props['k_hooke'] = k_hooke
        self.props['quiet'] = quiet
        self.props['mass'] = mass

        if kargs is not None:
            for key, value in kargs.items():
                if key == 'x':
                    self.props['x'] = value
                if key == 'y':
                    self.props['y'] = value

        # Image source
        self.image = pygame.transform.scale(
            pygame.image.load(img_url).convert_alpha(),
            (self.props["radius"],
                self.props["radius"])
        )
        self.rect = self.image.get_rect()

        # set dim
        self.props["width"] = self.rect.width
        self.props["height"] = self.rect.height

        # set initial position
        self.control(self.props['x'], self.props['y'])

    def control(self, x: int, y: int):
        """
        control ball movement
        """
        self.movex += x
        self.movey += y

    def update(self) -> list:
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.screen.blit(self.image, self.rect)
        self.props['x'] = self.rect.x
        self.props['y'] = self.rect.y
        pygame.display.flip()
        return [self.rect.x, self.rect.y]

    def motion(
        self, screen_color: str,
        speed: list,
        clock_time: int
    ):
        """
        Motion
        """
        self.props["screen_color"] = screen_color
        self.props["speed_i"] = speed
        self.props["speed_f"] = speed
        self.props["clock_time"] = clock_time

        pygame.time.Clock().tick(clock_time)
        if speed == [0.0, 0.0]:
            print(self.props['id'], "Quiet")
            self.control(self.props['x'], self.props['y'])
            self.props['quiet'] = True
            self.quiet()
        else:
            self.screen.fill(self.colors[screen_color])
            self.props['quiet'] = False
            print(self.props['id'], "Run")
            self.rect = self.rect.move(speed)
            if self.rect.left <= 0 or self.rect.right >= self.width:
                speed[0] = -speed[0]
            if self.rect.top <= 0 or self.rect.bottom >= self.height:
                speed[1] = -speed[1]
            self.props["speed_f"] = speed
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()

    def quiet(self):
        '''
        Stay static but present in screen update
        '''
        pygame.time.Clock().tick(self.props["clock_time"])
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

    def collision(self):
        """
        Collision
        """
        self.update()
        print(f"propiedades: {self.props}")
        print()
