import sys
import pygame

from character import Character

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1000, 800))
	
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		c1 = Character(screen)
		
		screen.fill((230, 230, 230))
		c1.blitme()
		pygame.display.flip()
		
run_game()
