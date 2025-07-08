class Scene:
    '''모든 씬이 상속하는 부모 클래스'''
    def __init__(self, game):
        self.game = game

    def handle_events(self, events):
        raise NotImplementedError

    def update(self, delta_time):
        raise NotImplementedError

    def draw(self, screen):
        raise NotImplementedError