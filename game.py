# Import and initialize pygame
import pygame

# Initialize Pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Drawing Objects and Images")

# Define the GameObject class
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

# Create instances of GameObject for apples and strawberries
objects = [
     GameObject(100, 100, 'apple.png'),    # Top left apple
    GameObject(200, 100, 'strawberry.png'), # Top middle strawberry
    GameObject(300, 100, 'apple.png'),    # Top right apple
    
    GameObject(100, 200, 'strawberry.png'), # Middle left strawberry
    GameObject(200, 200, 'apple.png'),    # Middle center apple
    GameObject(300, 200, 'strawberry.png'), # Middle right strawberry
    
    GameObject(100, 300, 'apple.png'),    # Bottom left apple
    GameObject(200, 300, 'strawberry.png'), # Bottom middle strawberry
    GameObject(300, 300, 'apple.png')     # Bottom right apple
]

# Create the game loop
running = True
while running:
    # Check for events and handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen to white
    screen.fill((255, 255, 255))

    # Render each game object
    for obj in objects:
        obj.render(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
