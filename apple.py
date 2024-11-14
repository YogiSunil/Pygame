import pygame
from random import choice, randint
from constants import LANES
from game_object import GameObject


class AppleSprite(GameObject):
    def __init__(self):
        super().__init__(0, 0, 'images/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = choice(LANES)
        self.y = -64
