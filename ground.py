from drawable import DrawWithSprite


class Ground(DrawWithSprite):
    def __init__(self, pos, size, image):
        super().__init__(pos, size, image)

    def update(self, shift_x):
        self.rect.x += shift_x
