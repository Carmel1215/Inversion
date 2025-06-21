from scenes.scene import Scene
import pygame

class IntroScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        # 필요한 것 초기화

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space Pressed")

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))