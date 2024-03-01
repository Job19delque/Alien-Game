"""Here we control the game's appearance as well as the ship's speed"""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3  # 3 Pixels
        self.bullet_height = 15  # 15 pixels
        self.bullet_color = 60, 60, 60  # Dark grey bullet
        self.bullets_allowed = 3  # To limit the number of bullets a player can have on the screen at once. To be precise with the firing
