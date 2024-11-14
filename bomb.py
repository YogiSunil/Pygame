import pygame
from random import randint, choice
from constants import LANES
from game_object import GameObject


class BombSprite(GameObject):
    def __init__(self):
        super().__init__(0, 0, 'images/bomb.png')
        self.dx = 0
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
            self.reset()

    def reset(self):
        direction = randint(1, 4)
        if direction == 1:  # left
            self.x = -64
            self.y = choice(LANES)
            self.dx = (randint(0, 200) / 100) + 1
            self.dy = 0
        elif direction == 2:  # right
            self.x = 500
            self.y = choice(LANES)
            self.dx = ((randint(0, 200) / 100) + 1) * -1
            self.dy = 0
        elif direction == 3:  # down
            self.x = choice(LANES)
            self.y = -64
            self.dx = 0
            self.dy = (randint(0, 200) / 100) + 1
        else:  # up
            self.x = choice(LANES)
            self.y = 500
            self.dx = 0
            self.dy = ((randint(0, 200) / 100) + 1) * -1
