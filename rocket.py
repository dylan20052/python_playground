import pygame

from game_settings import GameSettings
from rocketship import Rocketship
import game_func as gf


def run_game():
    # Init Objects
    gs = GameSettings()

    # Init
    pygame.init()
    screen = pygame.display.set_mode(gs.resolution)
    pygame.display.set_caption(gs.caption)

    rocket = Rocketship(screen)

    # Display
    while True:
        gf.check_events(rocket)
        screen.fill(gs.bg_color)
        rocket.update(gs.rocket_speed)
        rocket.blitme()
        pygame.display.flip()

run_game()