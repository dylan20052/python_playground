import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, gs, screen, ship):
        """Make bullet at ships position"""
        super().__init__()
        self.screen = screen

        # Create bullet rect at 0,0 and then set positiong
        self.rect = pygame.Rect(0, 0, gs.bullet_width, gs.bullet_height)
        self.rect.center = ship.image_rect.center
        self.rect.left = ship.image_rect.left

        # Store bullet's pos as decimal
        self.x = float(self.rect.x)

        self.color = gs.bullet_color
        self.speed_factor = gs.bullet_speed_factor

    def update(self):
        """Move bullet on x plane"""
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)