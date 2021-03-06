import random
import sys
from itertools import cycle

import pygame
from pygame.locals import *

SCREEN_W = 1380  # 宽度
SCREEN_H = 320  # 高度
FPS = 55  # 帧数（更新画面的时间）
FPSCLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))


def main_game():
    score = 0
    over = False
    pygame.init()

    add_obstacle_timer = 0
    obstacle_list = []
    pygame.display.set_caption('谷歌小恐龙')

    bg1 = Map(0, 0)
    bg2 = Map(800, 0)
    dinosaur = Dinosaur()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

            if event.type == KEYDOWN and event.key == K_SPACE:
                if not over and dinosaur.rect.y <= dinosaur.lowest_y:
                    dinosaur.jump()
                    dinosaur.jump_audio.play()
                if over:
                    main_game()
            if event.type == KEYDOWN and event.key == K_LEFT and not over:
                dinosaur.left()
            elif event.type == KEYDOWN and event.key == K_RIGHT and not over:
                dinosaur.right()
            elif event.type == KEYDOWN and event.key == K_DOWN and not over:
                dinosaur.paxia()

            if event.type == KEYUP and event.key == K_LEFT and not over:
                dinosaur.no_left()
            elif event.type == KEYUP and event.key == K_RIGHT and not over:
                dinosaur.no_right()
            elif event.type == KEYUP and event.key == K_DOWN and not over:
                dinosaur.no_paxia()

        if add_obstacle_timer >= 1300:
            r = random.randint(0, 100)
            if r > 40:
                obstacle = Obstacle()
                obstacle_list.append(obstacle)
            add_obstacle_timer = 0

        if not over:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()

            for i in range(len(obstacle_list)):
                obstacle_list[i].obstacle_move()
                obstacle_list[i].draw_obstacle()

                if pygame.sprite.collide_rect(dinosaur, obstacle_list[i]):
                    over = True
                    game_over()
                else:
                    if (obstacle_list[i].rect.x + obstacle_list[i].rect.width) < dinosaur.rect.x:
                        score += obstacle_list[i].get_score()

                obstacle_list[i].show_score(score)

        dinosaur.move()
        dinosaur.draw_dinosaur()

        add_obstacle_timer += 20
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def game_over():
    bump_audio = pygame.mixer.Sound('./audio/bump.wav')
    bump_audio.play()

    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h

    over_img = pygame.image.load('./image/gameover.png')
    SCREEN.blit(over_img, ((screen_w - over_img.get_width()) / 2,
                           (screen_h - over_img.get_height()) / 2))


class Map:
    def __init__(self, x, y):
        self.bg = pygame.image.load('./image/bg.png')
        self.x = x
        self.y = y

    def map_rolling(self):
        if self.x < -794:
            self.x = 800
        else:
            self.x -= 5

    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


class Dinosaur:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.jump_state = False
        self.right_state = False
        self.left_state = False
        self.paxia_state = False

        self.jump_height = 140
        self.lowest_y = 155
        self.jump_value = 0
        self.dino_index = 0
        self.dino_index_gen = cycle([0,0,0, 1,1,1, 2,2,2])
        self.dino_image = (
            pygame.image.load('./image/dns1.png'),
            pygame.image.load('./image/dns2.png'),
            pygame.image.load('./image/dns3.png'),
            pygame.image.load('./image/dnsp.png')
        )
        self.jump_audio = pygame.mixer.Sound('./audio/jump.wav')
        self.rect.size = self.dino_image[0].get_size()
        self.x = 20
        self.y = self.lowest_y
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.jump_state = True

    def paxia(self):
        if not self.jump_state:
            self.paxia_state = True
            self.rect.top += 20

    def left(self):
        self.left_state = True

    def right(self):
        self.right_state = True

    def no_paxia(self):
        self.paxia_state = False
        if not self.jump_state:
            self.rect.top -= self.rect.top - 155

    def no_left(self):
        self.left_state = False

    def no_right(self):
        self.right_state = False

    def move(self):
        if self.jump_state:
            if self.rect.y >= self.lowest_y:
                self.jump_value = -5
            if self.rect.y <= self.lowest_y - self.jump_height:
                self.jump_value = 5
            self.rect.y += self.jump_value
            self.rect.x += 2
            if self.rect.y >= self.lowest_y:
                self.jump_state = False
        if self.right_state:
            if self.rect.x < 1100:
                self.rect.x += 5
            else:
                self.right_state = False
        if self.left_state:
            if self.rect.x > 20:
                self.rect.x -= 5
            else:
                self.left_state = False
        if self.y <= 155 and not self.jump_state:
            self.y = 155

    def draw_dinosaur(self):
        if not self.paxia_state:
            dino_index = next(self.dino_index_gen)
            x = self.rect.x
            y = self.rect.y
        else:
            dino_index = 3
            x = self.rect.x
            y = self.rect.y + 30
        SCREEN.blit(self.dino_image[dino_index], (x, y))


class Obstacle:
    score = 1

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.stone = pygame.image.load('./image/stone.png')
        self.cacti = pygame.image.load('./image/cacti.png')
        self.bird = pygame.image.load('./image/bird.png')

        self.is_bird = 0
        self.is_stone = 0
        self.is_cacti = 0

        self.number = (pygame.image.load('./image/0.png'),
                       pygame.image.load('./image/1.png'),
                       pygame.image.load('./image/2.png'),
                       pygame.image.load('./image/3.png'),
                       pygame.image.load('./image/4.png'),
                       pygame.image.load('./image/5.png'),
                       pygame.image.load('./image/6.png'),
                       pygame.image.load('./image/7.png'),
                       pygame.image.load('./image/8.png'),
                       pygame.image.load('./image/9.png'),
                       )
        self.score_audio = pygame.mixer.Sound('./audio/score.wav')

        r = random.randint(0, 2)
        if r == 0:
            self.image = self.stone
            self.is_stone = 1
        elif r == 1:
            self.image = self.cacti
            self.is_cacti = 1
        else:
            self.image = self.bird
            self.is_bird = 1

        self.rect.size = self.image.get_size()
        self.w, self.h = self.rect.size

        self.x = SCREEN_W

        if self.is_stone:
            self.y = 200
        if self.is_cacti:
            self.y = 185
        if self.is_bird:
            self.y = random.choice([110, 130, 155, 140, 175, 160])
        # self.y = 215 - (self.h / 2) if not self.is_bird else random.choice([110, 120, 130, 140, 155])
        # self.rect.x = self.x
        # self.rect.y = self.y

        self.rect.center = (self.x, self.y)
        if self.is_bird:
            self.rect.top = self.y-7

    def obstacle_move(self):
        self.rect.x -= 5 if not self.is_bird else 10

    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def get_score(self):
        tmp = self.score
        if tmp:
            self.score_audio.play()
        self.score = 0
        return tmp

    def show_score(self, score):
        self.score_digits = [int(x) for x in list(str(score))]
        total_w = 0
        for digit in self.score_digits:
            total_w += self.number[digit].get_width()
        offset = (SCREEN_W - total_w) / 2
        for digit in self.score_digits:
            SCREEN.blit(self.number[digit], (offset, SCREEN_H * 0.1))
            offset += self.number[digit].get_width()


if __name__ == '__main__':
    main_game()
