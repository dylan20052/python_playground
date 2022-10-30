import pygame
from random import randrange

class Ball:

    def __init__(self, screen):
        """init ball and starting pos"""
        self.image = pygame.image.load("images/ball.bmp")
        self.rect = self.image.get_rect()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # init ball starting at top center
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top

        self.centery = float(self.rect.centery)
        self.centerx = float(self.rect.centerx)

    def update(self):
        """Make ball fall"""
        self.centery += .5
        self.rect.centery = self.centery

    def randompos(self):
        # set y to top
        self.centery = self.screen_rect.top
        self.rect.centery = self.centery

        # set random x
        self.centerx = randrange(100, self.screen_rect.width - 100)
        self.rect.centerx = self.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)
