from scenes.scene import Scene
from core.settings import *

class IntroScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        # 필요한 것 초기화


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space Pressed")
                if event.key == pygame.K_RETURN:
                    print("Return pressed")

    def update(self, delta_time):
        pass

    def draw(self, screen):
        pass