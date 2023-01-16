import pygame as pygame

from barbeque import Barbeque
from enemy import Enemy
from bullet import Bullet
from objects import Object
from poop import Poop
from constants import *


class Game:
    def __init__(self):
        # pygame init
        pygame.init()
        pygame.display.set_caption(game_name)
        self.icon = pygame.image.load(pig_img)
        pygame.display.set_icon(self.icon)
        self.window = pygame.display.set_mode((width, height))
        self.background = pygame.image.load(background_img)

        # spawn objects
        self.spawn_objects()

        # init game variables
        self.highscore = 0
        self.score = 0
        self.lives = init_lives
        self.nr_levels = 0
        self.lose_messages = random.choice(gameover_messages)
        self.win_messages = random.choice(win_messages)
        self.font_30 = pygame.font.Font(font, 30)
        self.font_60 = pygame.font.Font(font, 60)
        self.ribbon = pygame.image.load(ribbon_img)
        self.ok = True
        self.time = 0
        self.ribbon_shown = 0
        self.poop_rate = 0

    def spawn_objects(self):
        self.enemies = pygame.sprite.Group()
        self.enemies_list = pygame.sprite.Group.sprites(self.enemies)
        self.objects = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bullets_list = pygame.sprite.Group.sprites(self.bullets)
        self.poops = pygame.sprite.Group()
        self.spawn_enemies()
        self.spawn_barbeque()

    def spawn_enemies(self):
        for row in range(4):
            for column in range(7):
                enemy = Enemy(-70 + (110 * (column + 1)), 25 + (50 * (row + 1)), "alive")
                self.objects.add(enemy)
                self.enemies.add(enemy)
                self.enemies_list.append(enemy)

    def spawn_barbeque(self):
        self.barbeque = Barbeque(width / 2 - 50, height / 2 + 180, init_lives)
        self.objects.add(self.barbeque)

    def draw(self):
        self.window.blit(self.background, (0, 0))
        self.objects.draw(self.window)

        if self.lives > 0:
            self.show_score()

        if self.ribbon_shown == 1:
            self.level_up()
        if self.ribbon_shown == 2:
            self.game_over()

            # self.reset_game()

        pygame.display.update()
        pygame.time.Clock().tick(30)

    def fire_bullet(self):
        bullet = Bullet(self.barbeque.rect.x + 64, self.barbeque.rect.y + 64, "fire", self)
        self.bullets.add(bullet)
        self.bullets_list.append(bullet)
        self.objects.add(bullet)
        self.time = pygame.time.get_ticks()

    def pooping(self):
        elem = random.choice(self.enemies_list)
        poop = Poop(elem.rect.x + 15, elem.rect.y + 15)
        self.poops.add(poop)
        self.objects.add(poop)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.barbeque.move_left()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.barbeque.move_right()
        if keys[pygame.K_SPACE] and self.ok == True:
            self.fire_bullet()
            self.ok = False

    def update(self):
        self.objects.update(self)
        self.poop_rate += 1
        if self.poop_rate % poop_frequency == 0:
            self.pooping()
        self.collision_BE()  # collision bullet-enemy
        self.collision_BB()  # collision bullet-barbeque
        self.collision_PB()  # collision poop-barbeque
        for obj in self.objects:
            obj.update(self)

    def level_up(self):
        self.level_up_message = self.font_60.render("LEVEL " + str(self.nr_levels + 1), True, white)
        self.window.blit(self.ribbon, (100, 200))
        self.window.blit(self.level_up_message, (width / 2 - 100, height / 2))
        self.ribbon_shown = 0
        pygame.display.update()
        pygame.time.wait(5000)
        self.ok = True
        self.spawn_objects()

    def game_over(self):
        if (self.score > self.highscore):
            self.highscore = self.score

        self.window.blit(self.ribbon, (100, 200))
        self.gameover_message = self.font_30.render(self.lose_messages, True, white)
        self.window.blit(self.gameover_message, (width / 2 - 200, height / 2 - 50))

        self.highscore_message = self.font_30.render("HighScore: " + str(self.highscore), 1, white)
        self.window.blit(self.highscore_message, (width / 2 - 75, height / 2))

        self.score = 0
        self.ribbon_shown = 0
        pygame.display.update()
        pygame.time.wait(1000)

    def win(self):
        if (self.score > self.highscore):
            self.highscore = self.score

        self.window.blit(self.ribbon, (100, 200))
        self.win_message = self.font_30.render(self.win_messages, True, white)
        self.window.blit(self.win_message, (width / 2 - 50, height / 2 - 50))

        self.highscore_message = self.font_30.render("HighScore: " + str(self.highscore), 1, white)
        self.window.blit(self.highscore_message, (width / 2 - 75, height / 2))

        pygame.display.update()
        pygame.time.wait(5000)

        self.score = 0
        self.ribbon_shown = 0

    def collision_BE(self):
        for target in self.enemies:
            for bullet in self.bullets:
                if target.collides_with(bullet) and bullet.state != "hit":
                    bullet.incollision_enemy(self)
                    target.incollision(self)

    def collision_BB(self):
        for bullet in self.bullets:
            if bullet.state == "hit":
                if bullet.collides_with(self.barbeque):
                    bullet.incollision_barbeque(self)

    def collision_PB(self):
        for poop in self.poops:
            if poop.collides_with(self.barbeque):
                poop.incollision(self)

    def removeObject(self, obj):
        self.objects.remove(obj)

    def show_score(self):
        score_written = self.font_60.render("SCORE: " + str(self.score), True, white)
        self.window.blit(score_written, (10, 0))
        self.lives_label = self.font_60.render("Lives: " + str(self.lives), True, white)
        self.window.blit(self.lives_label, (width - 220, 0))

    def check_game_status(self):
        if self.lives > 0 and len(self.enemies) == 0:
            self.ribbon_shown = 1
            self.nr_levels += 1
            self.objects.empty()
            self.bullets.empty()

        if self.score % lives_increment == lives_increment - 1:
            self.lives += 1
            self.score += 1

        if self.lives <= 0:
            self.ribbon_shown = 2
            self.lives == init_lives
            self.objects.empty()
            self.bullets.empty()
        if self.nr_levels > nr_levels_max:
            self.win()

    def run(self):
        while (True):
            self.input()
            self.update()
            self.draw()
            self.check_game_status()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
