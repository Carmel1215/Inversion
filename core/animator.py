class Animator:
    def __init__(self, animations):
        self.animations = animations
        self.current = None

    def set(self, name):
        if name not in self.animations:
            raise NameError("Animation not found")

        if self.current != self.animations[name]:
            self.current = self.animations[name]
            self.current.reset()

    def update(self, delta_time):
        if self.current:
            self.current.update(delta_time)
    def get_image(self):
        if self.current:
            return self.current.get_image()
        return None