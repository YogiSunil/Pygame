import pygame
from constants import LANES
from game_object import GameObject

class PlayerSprite(GameObject):
    def __init__(self):
        super(PlayerSprite, self).__init__(0, 0, 'images/player.png')
        self.pos_x = 1  # Start in the middle lane
        self.pos_y = 1  # Start in the middle lane
        self.dx = LANES[self.pos_x]
        self.dy = LANES[self.pos_y]
        self.reset()

    def move_left(self):
        """Move player left, if possible."""
        if self.pos_x > 0:
            self.pos_x -= 1
        self.update_position()

    def move_right(self):
        """Move player right, if possible."""
        if self.pos_x < len(LANES) - 1:
            self.pos_x += 1
        self.update_position()

    def move_up(self):
        """Move player up, if possible."""
        if self.pos_y > 0:
            self.pos_y -= 1
        self.update_position()

    def move_down(self):
        """Move player down, if possible."""
        if self.pos_y < len(LANES) - 1:
            self.pos_y += 1
        self.update_position()

    def update_position(self):
        """Update player position based on lane choice."""
        self.dx = LANES[self.pos_x]  # Update x-coordinate based on selected lane
        self.dy = LANES[self.pos_y]  # Update y-coordinate based on selected lane
        self.x = self.dx
        self.y = self.dy

    def reset(self):
        """Reset player's position."""
        self.update_position()

    def update(self):
        """Override to handle position updates more smoothly."""
        self.x = self.dx
        self.y = self.dy
