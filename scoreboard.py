import pygame.font

class Scoreboard:
    """A class to report scoring info"""

    def __init__(self, screen, ai_settings, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48, True)

        # prepare init score image
        self.prep_score()

    def prep_score(self):
        """Render score"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, False, self.text_color, self.ai_settings.bg_color)

        # Display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = self.screen_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)