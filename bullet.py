import pygame

# The use of Sprite is when you want to group related elements in a game and act on all elements at once
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(
            Bullet, self
        ).__init__()  # super() is need to inherit properly from Sprite
        self.screen = screen

        # Create a bullet rect (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = (
            ship.rect.centerx
        )  # Here the bullet be in the same position as the ship
        self.rect.top = ship.rect.top  # The bullets are fired from the top of the ship

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    # It manages the bullet's position
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
