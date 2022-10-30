import pygame

from game_settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    gs = Settings()

    pygame.init()
    screen = pygame.display.set_mode(gs.resolution)
    pygame.display.set_caption(gs.caption)

    ship = Ship(screen)
    bullets = Group()

    while True:
        gf.check_events(gs, screen, ship, bullets)
        ship.update_ship()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.left > 1200:
                bullets.remove(bullet)

        gf.update_screen(gs, screen, ship, bullets)
run_game()
