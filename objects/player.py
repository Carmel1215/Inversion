import pygame, os
from core.animator import Animator
from core.animation import Animation
import core.settings as settings
import core.assets as assets


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=250):
        super().__init__()
        self.speed = speed
        self.direction = 'Front' # 'Front' 또는 'Back' 또는 'Left' 또는 'Right'
        self.state = 'Idle' # 'Idle' 또는 'Walk'

        self.animator = Animator({
            # Black Idle
            "BlackIdleFront" : Animation(assets.BLACK_PLAYER_IDLE_FRONT, 0.5),
            "BlackIdleBack" : Animation(assets.BLACK_PLAYER_IDLE_BACK, 0.5),
            "BlackIdleLeft" : Animation(assets.BLACK_PLAYER_IDLE_LEFT, 1),
            "BlackIdleRight" : Animation(assets.BLACK_PLAYER_IDLE_RIGHT, 1),

            # Black Walk
            "BlackWalkFront" : Animation(assets.BLACK_PLAYER_WALK_FRONT, 0.25),
            "BlackWalkBack" : Animation(assets.BLACK_PLAYER_WALK_BACK, 0.25),
            "BlackWalkLeft" : Animation(assets.BLACK_PLAYER_WALK_LEFT),
            "BlackWalkRight" : Animation(assets.BLACK_PLAYER_WALK_RIGHT),

            # White Idle
            "WhiteIdleFront" : Animation(assets.WHITE_PLAYER_IDLE_FRONT, 0.5),
            "WhiteIdleBack" : Animation(assets.WHITE_PLAYER_IDLE_BACK, 0.5),
            "WhiteIdleLeft" : Animation(assets.WHITE_PLAYER_IDLE_LEFT, 1),
            "WhiteIdleRight" : Animation(assets.WHITE_PLAYER_IDLE_RIGHT, 1),

            # White Walk
            "WhiteWalkFront" : Animation(assets.WHITE_PLAYER_WALK_FRONT, 0.25),
            "WhiteWalkBack" : Animation(assets.WHITE_PLAYER_WALK_BACK, 0.25),
            "WhiteWalkLeft" : Animation(assets.WHITE_PLAYER_WALK_LEFT),
            "WhiteWalkRight" : Animation(assets.WHITE_PLAYER_WALK_RIGHT),
        })
        self.animator.set("BlackIdleFront")

        self.image = self.animator.get_image()
        self.rect = self.image.get_rect(topleft=(x, y))

    def toggle_inversion(self):
        settings.IS_INVERSION = not settings.IS_INVERSION

    def update(self, delta_time, keys):
        dx = dy = 0
        is_moving = False
        if keys[pygame.K_w]:
            dy -= 1
            self.direction = 'Back'
            is_moving = True
        if keys[pygame.K_s]:
            dy += 1
            self.direction = 'Front'
            is_moving = True
        if keys[pygame.K_a]:
            dx -= 1
            self.direction = 'Left'
            is_moving = True
        if keys[pygame.K_d]:
            dx += 1
            self.direction = 'Right'
            is_moving = True

        self.state = 'Walk' if is_moving else 'Idle'

        self.rect.x += dx * round(self.speed * delta_time) # round 처리한 이유: 좌표는 무조건 정수이기 때문에 소수값을 집어넣으면 무조건 버림을 하고 따라서 속도에 차이가 나기 때문
        self.rect.y += dy * round(self.speed * delta_time) # round 처리한 이유: 좌표는 무조건 정수이기 때문에 소수값을 집어넣으면 무조건 버림을 하고 따라서 속도에 차이가 나기 때문

        animation_name = f"White{self.state}{self.direction}" if settings.IS_INVERSION else f"Black{self.state}{self.direction}"
        self.animator.set(animation_name)
        self.animator.update(delta_time)

        self.image = self.animator.get_image()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))