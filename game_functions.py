import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep



def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Responds to keypresses"""
	if event.key == pygame.K_RIGHT:
		# Move ship to right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# Move ship to left
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(event, ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()


def fire_bullet(event, ai_settings, screen, ship, bullets):
	"""Fire bullet if limit is not reached"""
	# Create bullet and add it to bullet group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# Move ship to right
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		# Move ship to left
		ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens):
	"""Respond to keypress and mouse events"""
	# Watch for keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship)


def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship):
	"""Start new game when player hits play"""
	if play_button.rect.collidepoint(mouse_x, mouse_y) and stats.game_active == False:
		ai_settings.initialize_dynamic_settings()
		# Reset game stats
		stats.reset_stats()
		stats.game_active = True

		# Empty list of aliens and bullets
		aliens.empty()
		bullets.empty()

		# Create new fleet and center ship
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		pygame.mouse.set_visible(False)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
	"""Update images on screen and flip to new screen"""
	# Redraw screen during each pass through loop
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen)
	sb.show_score()

	# Draw play button if game is inactive
	if not stats.game_active:
		pygame.mouse.set_visible(True)
		play_button.draw_button()

	# Make most recently drawn screen visible
	pygame.display.flip()


def update_bullets(ai_settings, screen, ship, stats, sb, aliens, bullets):
	"""Update bullet position and get rid of excess bullets"""
	# Update bullet position
	bullets.update()

	# Get rid of bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collision(ai_settings, screen, ship, stats, sb, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, ship, stats, sb, aliens, bullets):
	# Check for any bullets that have hit aliens
	# If so, get rid of bullet and alien
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			stats.score += (ai_settings.alien_points * len(aliens))
			sb.prep_score()

	if len(aliens) == 0:
		# Destroy existing bulelts and create new fleet
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - (alien_width * 2)
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
	"""Determine number of rows alien can fit on screen"""
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
	"""Create full alien fleet"""
	# Create alien and find number of aliens in row
	# Spacing between each alien is equal to one alien width
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	# Create first row of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
	"""Respond appropiately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break


def change_fleet_direction(ai_settings, aliens):
	"""Drop entire fleet and change fleet's direction"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	"""Ship response after being hit by alien."""
	if stats.ships_left > 0:
		# Decrement ships left
		stats.ships_left -= 1
		# Empty the list of aliens and bullets
		aliens.empty()
		bullets.empty()
		# Create new fleet and center ship
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		print("Lives: " + str(stats.ships_left))

		# Pause
		sleep(0.5)

	else:
		stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	"""Check if any aliens have reached bottom of screen."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Treat this the same if the ship got hit
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
			break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	"""Update pos of all aliens"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	# Look for alien-ship collisions
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

	# Look for aliens hitting bottom of screen
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
