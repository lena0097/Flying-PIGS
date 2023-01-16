from objects import Object
from constants import *


class Barbeque(Object):
    def __init__(self, playerX, playerY, state):
        super().__init__(playerX, playerY)
        self.image = pygame.image.load(barbeque_img)
        self.rect = self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY
        self.state = state

    def move_left(self):
        self.rect.x -= 30

    def move_right(self):
        self.rect.x += 30

    def update(self, game):
        if self.rect.x < -10:
            self.rect.x = -10
        if self.rect.x > width - 110:
            self.rect.x = width - 110

    def get_type(self):
        return "barbeque"