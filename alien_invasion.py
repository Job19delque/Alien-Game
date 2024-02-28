import pygame

def main():
    """ Set up the game and rum the main loop"""

    pygame.init() # Prepare the pygame module for use
    surface_sz = 480 # Describe physical surface in pixels

    # Create surface of width, height and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and it color
    small_rect = (300, 200, 150, 90)
    some_color = (250, 0, 0)

    while True:
        ev = pygame.event.poll() # Look for any event
        if ev.type == pygame.QUIT: # Window close button clicked?
            break # Leave game loop
        

pygame.quit()