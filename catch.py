import pygame
import game_functions as gf

from character import Character
from ball import Ball

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    # init classes
    character = Character(screen)
    ball = Ball(screen)


    while True:
        gf.check_events(character)
        character.update()
        ball.update()
        gf.update_screen(character, ball, screen)

run_game()