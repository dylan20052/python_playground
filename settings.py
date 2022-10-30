class Settings:
	"""A class to store all game settings"""
	
	def __init__(self):
		"""Init game settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		
		# Ship settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 1

		# Bullet settings
		self.bullet_speed_factor = 3
		self.bullet_width = 1
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Alien settings
		self.fleet_drop_speed = 80

		# How quickly the game speeds up and score multiplies
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Init settings that change throughout game"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet direction of 1 represents right; -1 represent left
		self.fleet_direction = 1

		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.speedup_scale)