import pygame
from random import randint

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 500

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title
pygame.display.set_caption("Fruit Movement Game")

# Load images
apple_image = pygame.image.load('apple.png')
strawberry_image = pygame.image.load('strawberry.png')

# Base GameObject class
class GameObject:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Apple class (vertical movement)
class Apple(GameObject):
    def __init__(self):
        super().__init__(randint(93, 343), 0, apple_image)
        self.dy = (randint(100, 300) / 100)  # Speed between 1.0 and 3.0

    def move(self):
        self.y += self.dy
        if self.y > screen_height:
            self.reset()

    def reset(self):
        self.x = randint(93, 343)  # Choose from specific lanes
        self.y = -64  # Start above the screen

# Strawberry class (horizontal movement)
class Strawberry(GameObject):
    def __init__(self):
        super().__init__(0, randint(50, 400), strawberry_image)
        self.dx = (randint(100, 300) / 100)  # Speed between 1.0 and 3.0

    def move(self):
        self.x += self.dx
        if self.x > screen_width:
            self.reset()

    def reset(self):
        self.x = -64  # Start off-screen to the left
        self.y = randint(50, 400)  # Random vertical position

# Main game loop
running = True
clock = pygame.time.Clock()

# Create instances of the game objects
apple = Apple()
strawberry = Strawberry()

while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Move and render the objects
    apple.move()
    apple.render(screen)

    strawberry.move()
    strawberry.render(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
