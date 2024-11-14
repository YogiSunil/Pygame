import pygame
from random import randint
from game_object import GameObject


class CloudSprite(GameObject):
    def __init__(self):
        super().__init__(0, 0, 'images/cloud-1.png')
        self.dx = 0
        self.reset()

    def move(self):
        self.x += self.dx
        if self.x > 500:
            self.reset()

    def get_cloud_image(self):
        return f"images/cloud-{randint(1, 3)}.png"

    def reset(self):
        self.x = -64
        self.y = randint(0, 500 - 64)
        self.dx = (randint(0, 200) / 100)
        self.surf = pygame.image.load(self.get_cloud_image())
