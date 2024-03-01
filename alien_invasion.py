""" This is the main file. Where you run to play the game. 
    The others file are imported here.
     """

import pygame
from pygame.sprite import (
    Group,
)  # This behaves like a list wit some extra functionalities

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game, settings ans screen object.
    pygame.init()

    # An instance of Settings
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )  #
    pygame.display.set_caption("Alien Invasion")

    # Making a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = (
        Group()  # It is outside of the main loop to avoiding creating many groups
    )  # To draw bullets in the screen on each pass through the main loop and to update each bullet position

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
