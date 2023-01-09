from drawable import DrawWithSprite


class WinObject(DrawWithSprite):
    def __init__(self, pos, size, image):
        super().__init__(pos, size, image)

    def update(self, shift):
        self.rect.x += shift
