import pygame


class Character:

    def __init__(self, screen):
        """init image and screen"""
        self.image = pygame.image.load('images/character1.bmp')
        self.rect = self.image.get_rect()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # init starting pos for image
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # moving markers
        self.moving_right = False
        self.moving_left = False

        # score
        self.score = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.center += 1.5
        elif self.moving_left:
            self.center -= 3

        self.rect.centerx = self.center
