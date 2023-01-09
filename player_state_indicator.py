from drawable import DrawWithText


class PlayerStateIndicator(DrawWithText):
    def __init__(self, pos, hero):
        self.hero = hero
        self.pos = pos
        self.update()

    def update(self):
        self.text = f'HP : {self.hero.hp} SCORE : {self.hero.score}'
        super().__init__(self.pos, self.text)
