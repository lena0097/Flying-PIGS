from objects import Object
from constants import *


class Bullet(Object):
    def __init__(self, bulletX, bulletY, state, game):
        self.speed = -10
        super().__init__(bulletX, bulletY)
        self.game = game
        self.image = pygame.image.load(bullet1_img)
        self.rect = self.image.get_rect()
        self.rect.x = bulletX
        self.rect.y = bulletY
        self.state = state
        self.bonus_type = 0
        if game.score >= 50:
            self.image = pygame.image.load(bullet2_img)
        if game.score >= 100:
            self.image = pygame.image.load(bullet3_img)

    def update(self, game):
        self.rect.y += self.speed
        if self.rect.y < 0:
            game.objects.remove(self)
            game.bullets.remove(self)
            game.bullets_list = pygame.sprite.Group.sprites(game.bullets)

        if len(game.bullets_list) > 0:
            if self.rect.y == game.bullets_list[len(game.bullets) - 1].rect.y:
                if pygame.time.get_ticks() - game.time > (1000 / fire_rate):
                    game.ok = True

        if self.bonus_type == 1:
            self.image = pygame.image.load(reward1_img)
        elif self.bonus_type == 2:
            self.image = pygame.image.load(reward2_img)
        elif self.bonus_type == 3:
            self.image = pygame.image.load(reward3_img)

    def incollision_enemy(self, game):
        self.speed *= -0.5
        self.state = "hit"
        game.score += 1
        if self.state == "hit":
            self.bonus_type = random.choice([1, 2, 3])

    def incollision_barbeque(self, game):
        if self.bonus_type == 1:
            game.score += 1
        elif self.bonus_type == 2:
            game.score += 2
        elif self.bonus_type == 3:
            game.score += 3

        game.objects.remove(self)
        game.bullets.remove(self)
        game.bullets_list = pygame.sprite.Group.sprites(game.bullets)
