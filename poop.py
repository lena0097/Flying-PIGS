from constants import *
from objects import Object


class Poop(Object):
    def __init__(self, X, Y):
        self.speed = int(random.choice(["2", "3", "4"])) * (-1)
        super().__init__(X, Y)
        self.image = pygame.image.load(poop_img)
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y

    def update(self, game):
        self.rect.y -= self.speed

    def incollision(self, game):
        game.lives -= 1
        game.objects.remove(self)
        game.poops.remove(self)


