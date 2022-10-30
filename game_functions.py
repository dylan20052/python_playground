import sys
import pygame
from ball import Ball
from random import randrange


def check_keydown_events(event, character):
    if event.key == pygame.K_RIGHT:
        character.moving_right = True
    elif event.key == pygame.K_LEFT:
        character.moving_left = True

def check_keyup_events(event, character):
    if event.key == pygame.K_RIGHT:
        character.moving_right = False
    elif event.key == pygame.K_LEFT:
        character.moving_left = False

def check_events(character):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, character)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)

def check_collision(character, ball):
    if character.rect.colliderect(ball.rect):
        # return if collision
        character.score += 1
        print(character.score)
        return True
    if  ball.rect.top >= ball.screen_rect.height:
        return True

def update_ball_collision(character, ball):
    if check_collision(character, ball):
        ball.randompos()


def update_screen(character, ball, screen):
    update_ball_collision(character, ball)
    screen.fill((250, 250, 250))
    character.blitme()
    ball.blitme()
    pygame.display.flip()

