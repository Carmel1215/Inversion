import pygame, os
from objects.player import Player
from scenes.scene import Scene
import core.settings as settings

class IntroScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player(400, 500)

        self.font = pygame.font.Font(settings.FONT_PATH, 256)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.toggle_inversion()

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.player.update(delta_time, keys)

    def draw(self, screen):
        black = settings.WHITE if settings.IS_INVERSION else settings.BLACK
        white = settings.BLACK if settings.IS_INVERSION else settings.WHITE
        self.title_text = self.font.render('Inversion', True, white)
        text_rect = self.title_text.get_rect(centerx=screen.get_width() / 2, centery=screen.get_height() / 6)

        # BackGround
        screen.fill(black)

        # UI
        screen.blit(self.title_text, text_rect)

        # Player
        self.player.draw(screen)