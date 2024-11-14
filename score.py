import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)  # Font for displaying the score

    def increment(self):
        """Increase the score by 1."""
        self.score += 1

    def render(self, screen):
        """Render the score on the screen at the top-left corner."""
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))  # Black text
        screen.blit(score_text, (10, 10))  # Draw the score at position (10, 10)
