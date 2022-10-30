import pygame
from pygame.sprite import Group

from button import Button
from settings import Settings
from game_stats import GameStats
from ship import Ship
from scoreboard import Scoreboard
from alien import Alien
import game_functions as gf


def run_game():
	# Init pygame, settings, screen obj
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make the play button
	play_button = Button(ai_settings, screen, "Play")

	# Create an instance to store game stats
	stats = GameStats(ai_settings)

	# Make scoreboard
	sb = Scoreboard(screen, ai_settings, stats)

	# Make a ship, bullet group, and aliens
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	# Create alien fleet
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Start main loop for game
	while True:
		gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens)
		if stats.game_active == True:
			ship.update()

			gf.update_bullets(ai_settings, screen, ship, stats, sb, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		else:
			print("GAME OVER")

		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
