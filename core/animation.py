class Animation:
    def __init__(self, frames, speed=0.15, loop=True):
        self.frames = frames
        self.speed = speed
        self.loop = loop

        self.frame_index = 0
        self.timer = 0
        self.finished = False

    def update(self, delta_time):
        if self.finished:
            return

        self.timer += delta_time
        if self.timer >= self.speed:
            self.timer = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                if self.loop:
                    self.frame_index = 0
                else:
                    self.frame_index = len(self.frames) - 1
                    self.finished = True

    def get_image(self):
        return self.frames[self.frame_index]

    def reset(self):
        self.frame_index = 0
        self.timer = 0
        self.finished = False