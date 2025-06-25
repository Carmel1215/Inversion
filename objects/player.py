import pygame, os
from core.loader import load

class Player:
    def __init__(self, x, y, speed=100):
        self.x = x
        self.y = y
        self.speed = speed
        self.player = load(os.path.join('assets', 'images', 'Player.png'))

    def update(self, delta_time, keys):
        dx = dy = 0

        if keys[pygame.K_w]: dy -= 1
        if keys[pygame.K_s]: dy += 1
        if keys[pygame.K_a]: dx -= 1
        if keys[pygame.K_d]: dx += 1

        self.x += dx * self.speed * delta_time
        self.y += dy * self.speed * delta_time

    def draw(self, screen):
        screen.blit(self.player, (self.x, self.y))