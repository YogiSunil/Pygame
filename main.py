import pygame
from player import PlayerSprite
from apple import AppleSprite
from strawberry import StrawberrySprite
from bomb import BombSprite
from cloud import CloudSprite
from score import Score  # Import the Score class
from constants import LANES

# Initialize pygame
pygame.init()

# Configure screen
screen = pygame.display.set_mode([500, 500])

# Groups for sprites
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()

# Create instances
all_sprites.add(CloudSprite(), CloudSprite(), CloudSprite())

apple = AppleSprite()
strawberry = StrawberrySprite()
fruit_sprites.add(apple, strawberry)

player = PlayerSprite()
bomb = BombSprite()

all_sprites.add(player, apple, strawberry, bomb)

# Create a Score instance
score = Score()

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()

    # Clear screen
    screen.fill((170, 230, 255))

    # Move and render sprites
    for entity in all_sprites:
        if hasattr(entity, 'move'):  # Check if the entity has a move() method
            entity.move()
        entity.render(screen)

    # Check for collisions with fruit
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()  # Reset fruit to its original position
        score.increment()  # Increase the score by 1

    # Check for collisions with bomb
    if pygame.sprite.collide_rect(player, bomb):
        running = False

    # Render the score
    score.render(screen)

    # Update window
    pygame.display.flip()

    # Tick the clock
    clock.tick(30)

pygame.quit()
