import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("images/ship.bmp")
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # starting point for ship
        self.image_rect.center = self.screen_rect.center
        self.image_rect.left = self.screen_rect.left

        # movement flag
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)

    def update_ship(self):
        if self.moving_up:
            self.image_rect.centery -= 1
        if self.moving_down:
            self.image_rect.centery += 1