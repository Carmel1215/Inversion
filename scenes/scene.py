import pygame

class Scene:
    def __init__(self, game):
        self.game = game

    def handle_events(self, events):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def draw(self, screen):
        raise NotImplementedError