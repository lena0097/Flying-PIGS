from constants import *


class Object(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        super().__init__()
        self.X = X
        self.Y = Y

    def draw(self):
        pass

    def update(self, game):
        pass

    def delete(self):
        self.Object.remove(self)

    def collides_with(self, other):
        return pygame.sprite.collide_mask(self, other)

    def get_type(self):
        pass

