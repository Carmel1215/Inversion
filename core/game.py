import pygame
import core.settings as settings
from core.settings import *
from core.assets import load_assets
from core.scene_manager import SceneManager
from scenes.intro_scene import IntroScene

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(settings.TITLE)
        # pygame.display.set_icon(settings.icon)
        self.clock = pygame.time.Clock()
        self.running = True

        load_assets()

        self.scene_manager = SceneManager()
        self.scene_manager.go_to(IntroScene(self))

    def run(self):
        '''메인 루프'''

        fps_font = pygame.font.SysFont("Arial", 16) # 디버깅용 FPS 출력 폰트
        while self.running:
            delta_time = self.clock.tick(settings.FPS) / 1000 # deltatime
            events = pygame.event.get()
            self.handle_quit(events)
            self.scene_manager.handle_events(events)
            self.scene_manager.update(delta_time)
            self.scene_manager.draw(self.screen)

            # 디버깅용 FPS 출력
            fps = self.clock.get_fps()
            fps_text = fps_font.render(f"FPS: {fps:.1f}", True, (0, 255, 0))
            self.screen.blit(fps_text, (10, 10))

            pygame.display.update()

    def handle_quit(self, events):
        '''모든 씬에 적용되는 프로그램 종료 함수'''
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False