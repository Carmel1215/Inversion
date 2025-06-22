from scenes.scene import Scene
from core.settings import *

class IntroScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        # 필요한 것 초기화
        self.x = SCREEN_WIDTH / 2
        self.y = 700
        self.to_x = 50
        self.to_y = 50
        self.speed = 10
        self.arrived = False
        self.image = pygame.image.load('assets/images/IntroScene.png')


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space Pressed")

    def update(self):
        if not self.arrived:
            self.y -= self.speed
            if self.y <= self.to_y:
                self.y = self.to_y
                self.arrived = True

        if not self.arrived:
            self.x -= self.speed
            if self.x <= self.to_x:
                self.x = self.to_x
                self.arrived = True


    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.image, (self.x, self.y))
