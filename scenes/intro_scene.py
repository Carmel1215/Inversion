import pygame
from objects.player import Player
from scenes.scene import Scene
from core.settings import *

class IntroScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player(400, 500)

    def handle_events(self, events):
        for event in events:
            pass

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.player.update(delta_time, keys)

    def draw(self, screen):
        screen.fill(BLACK)
        self.player.draw(screen)