import pygame, os
from objects.player import Player
from scenes.scene import Scene
from core.settings import *

class IntroScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player(400, 500)

        self.font = pygame.font.Font(FONT_PATH, 256)

        self.title_text = self.font.render('Inversion', True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            pass

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.player.update(delta_time, keys)

    def draw(self, screen):
        text_rect = self.title_text.get_rect(centerx=screen.get_width() / 2, centery=screen.get_height() / 6)

        # BackGround
        screen.fill(BLACK)

        # UI
        screen.blit(self.title_text, text_rect)

        # Player
        self.player.draw(screen)