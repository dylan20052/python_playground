class GameStats:
    """Track Statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Init stats that can change during game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0