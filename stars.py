import pygame
import game_functions as gf
from pygame.sprite import Group
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    stars = Group()

    while True:
        screen.fill((250,250,250))
        gf.create_stars(screen, stars)
        stars.draw(screen)
        pygame.display.flip()

run_game()