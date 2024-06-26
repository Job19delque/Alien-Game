""" This is the main file. Where you run to play the game. 
    The others file are imported here.
     """

import pygame
from pygame.sprite import (
    Group,
)  # This behaves like a list with some extra functionalities

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Making a Ship
    ship = Ship(ai_settings, screen)

    # Making an Alien
    # alien = Alien(ai_settings, screen) --> Used before the fleet of aliens.

    # Make a group to store bullets in.
    bullets = (
        Group()  # It is outside of the main loop to avoiding creating many groups
    )  # To draw bullets in the screen on each pass through the main loop and to update each bullet position

    # Making Aliens
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(
            ai_settings, screen, stats, sb, play_button, ship, aliens, bullets
        )

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens, bullets, play_button
        )


run_game()
