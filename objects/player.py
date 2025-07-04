import pygame, os
from core.loader import load

class Player:
    def __init__(self, x, y, speed=200):
        self.x = x
        self.y = y
        self.speed = speed
        self.player = load(os.path.join('assets', 'images', 'Player.png'))

    def update(self, delta_time, keys):
        dx = dy = 0

        if keys[pygame.K_w]:
            dy -= 1
            # TODO: 다른 방향 바라보는 이미지로 변경 코드 작성
        if keys[pygame.K_s]:
            dy += 1
            # TODO: 다른 방향 바라보는 이미지로 변경 코드 작성
        if keys[pygame.K_a]:
            dx -= 1
            # TODO: 다른 방향 바라보는 이미지로 변경 코드 작성
        if keys[pygame.K_d]:
            dx += 1
            # TODO: 다른 방향 바라보는 이미지로 변경 코드 작성

        self.x += dx * self.speed * delta_time
        self.y += dy * self.speed * delta_time

    def draw(self, screen):
        screen.blit(self.player, (self.x, self.y))