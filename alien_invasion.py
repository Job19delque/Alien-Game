""" This is the main file. Where you run to play the game. 
    The others file are imported here.
     """
import pygame

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

    # Set the background color
    # This is specified only once, so define it before the main while loop.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
