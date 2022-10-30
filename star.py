import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """STARRRRR"""
    def __init__(self, screen):
        super().__init__()

        """init star image"""
        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Start at top left and then adjust later
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)