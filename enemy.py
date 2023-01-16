from constants import *
from objects import Object


class Enemy(Object):
    def __init__(self, X, Y, state):
        self.speed = int(random.choice(["2", "3", "4"])) * int(random.choice(["1", "-1"]))
        self.delta = 0
        super().__init__(X, Y)
        self.image = pygame.image.load(pig_img)
        self.rect = self.image.get_rect()
        self.state = state
        self.rect.x = X
        self.rect.y = Y

    def update(self, game):
        self.rect.x += self.speed
        self.delta += self.speed
        if abs(self.delta) > 40:
            self.speed *= -1

    def incollision(self, game):
        self.state = "hit"
        game.objects.remove(self)
        game.enemies.remove(self)
        game.enemies_list = pygame.sprite.Group.sprites(game.enemies)


