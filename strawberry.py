import pygame
from random import randint, choice
from constants import LANES
from game_object import GameObject

class StrawberrySprite(GameObject):
    def __init__(self):
        super().__init__(0, 0, 'images/strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64
        self.y = choice(LANES)
