class SceneManager:
    def __init__(self):
        self.current_scene = None

    def go_to(self, scene):
        '''현재 실행할 씬을 선택하는 메소드'''
        self.current_scene = scene

    def handle_events(self, events):
        self.current_scene.handle_events(events)

    def update(self, delta_time):
        self.current_scene.update(delta_time)

    def draw(self, screen):
        self.current_scene.draw(screen)