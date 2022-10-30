import pygame

class Character():
	
	def __init__(self, screen):
		self.screen = screen
		
		# init character
		self.image = pygame.image.load('images/character1.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		# init starting character point
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		"""Draws ship"""
		self.screen.blit(self.image, self.rect)
