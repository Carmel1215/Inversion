import pygame
import core.settings as settings
from core.scene_manager import SceneManager
from scenes.intro_scene import IntroScene

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        # pygame.display.set_icon(settings.icon)
        self.clock = pygame.time.Clock()
        self.running = True

        self.scene_manager = SceneManager()
        self.scene_manager.go_to(IntroScene(self))

    def run(self):
        '''메인 루프'''
        while self.running:
            delta_time = self.clock.tick(settings.FPS) / 1000 # deltatime

            events = pygame.event.get()
            self.handle_quit(events)
            self.scene_manager.handle_events(events)
            self.scene_manager.update(delta_time)
            self.scene_manager.draw(self.screen)
            pygame.display.flip()

    def handle_quit(self, events):
        '''모든 씬에 적용되는 프로그램 종료 함수'''
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False