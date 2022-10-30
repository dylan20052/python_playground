import pygame

class Rocketship():

    def __init__(self, screen):
        self.screen = screen

        # init image and screen rect
        self.image = pygame.image.load("images/rocket-ship.bmp")
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # movement flags//speed
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


        # draw rocket in middle of screen
        self.image_rect.center = self.screen_rect.center

    def update(self, speed):
        """Update position of rocket"""
        if self.moving_right:
            self.image_rect.centerx += speed
        elif self.moving_left:
            self.image_rect.centerx -= speed
        elif self.moving_up:
            self.image_rect.centery -= speed
        elif self.moving_down:
            self.image_rect.centery += speed

    def blitme(self):
        """Draw in rocket"""
        self.screen.blit(self.image, self.image_rect)