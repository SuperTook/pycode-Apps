import sys
import time
import pygame
from pygame.locals import *
import blocks

SIZE = 30  # 每个小方格大小
BLOCK_HEIGHT = 25  # 游戏区高度
BLOCK_WIDTH = 10  # 游戏区宽度
BORDER_WIDTH = 4  # 游戏区边框宽度
BORDER_COLOR = (40, 40, 200)  # 游戏区边框颜色
SCREEN_WIDTH = SIZE * (BLOCK_WIDTH + 5)  # 游戏屏幕的宽
SCREEN_HEIGHT = SIZE * BLOCK_HEIGHT  # 游戏屏幕的高

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('俄罗斯方块')

BG_COLOR = (50, 50, 80)  # 背景色
BLOCK_COLOR = (20, 200, 100)  # 方块颜色
BLACK = (0, 0, 0)
RED = (200, 30, 30)  # GAME OVER 的字体颜色
DUANG_WAV = pygame.mixer.Sound('audio/duang.wav')
SHU_WAV = pygame.mixer.Sound('audio/Shu_.wav')


def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))


def main():
    up = 0
    down = 0
    left = 0
    right = 0

    font1 = pygame.font.SysFont('SimHei', 24)  # 黑体24
    font2 = pygame.font.Font('SimHei', 90)  # GAME OVER 的字体
    font_pos_x = BLOCK_WIDTH * SIZE + BORDER_WIDTH + 10  # 右侧信息显示区域字体位置的X坐标
    gameover_size = font2.size('GAME OVER')
    font1_height = int(font1.size('得分')[1])

    this_block = None  # 当前下落方块
    next_block = None  # 下一个方块
    this_block_pos_x, this_block_pos_y = 0, 0

    game_area = None  # 整个游戏区域
    game_over = True
    start = False  # 是否开始，当start = True，game_over = True 时，才显示 GAME OVER
    score = 0  # 得分
    orispeed = 0.6  # 原始速度
    speed = orispeed  # 当前速度
    pause = False  # 暂停
    last_drop_time = None  # 上次下落时间

    def _dock():
        nonlocal this_block, next_block, game_area, this_block_pos_x, this_block_pos_y, game_over, score, speed
        for _i in range(this_block.start_pos.Y, this_block.end_pos.Y + 1):
            for _j in range(this_block.start_pos.X, this_block.end_pos.X + 1):
                if this_block.template[_i][_j] != '.':
                    game_area[this_block_pos_y + _i][this_block_pos_x + _j] = '0'
        if this_block_pos_y + this_block.start_pos.Y <= 0:
            game_over = True
        else:
            # 计算消除
            remove_index = []
            for _y in range(this_block.start_pos.Y, this_block.end_pos.Y + 1):
                if all(_x == '0' for _x in game_area[this_block_pos_y + _y]):
                    remove_index.append(this_block_pos_y + _y)
            if remove_index:
                # 计算得分
                remove_count = len(remove_index)
                if remove_count == 1:
                    score += 250
                elif remove_count == 2:
                    score += 500
                elif remove_count == 3:
                    score += 1400
                elif remove_count == 4:  # 由于最长的方块只有4格，所以不可能连消5层
                    score += 3000

                SHU_WAV.play()
                speed = orispeed - 0.03 * (score // 2000)
                # 消除
                _i = _j = remove_index[-1]
                while _i >= 0:
                    while _j in remove_index:
                        _j -= 1
                    if _j < 0:
                        game_area[_i] = ['.'] * BLOCK_WIDTH
                    else:
                        game_area[_i] = game_area[_j]
                    _i -= 1
                    _j -= 1
            else:
                DUANG_WAV.play()
            this_block = next_block
            next_block = blocks.get_block()
            this_block_pos_x = (BLOCK_WIDTH - this_block.end_pos.X - 1) // 2
            this_block_pos_y = -1 - this_block.end_pos.Y

    def _judge(pos_x, pos_y, block):  # 判断是否可以继续下落
        nonlocal game_area
        if pos_y + block.end_pos.Y >= BLOCK_HEIGHT:
            return False
        for _i in range(block.start_pos.Y, block.end_pos.Y + 1):
            for _j in range(block.start_pos.X, block.end_pos.X + 1):
                if pos_y + _i >= 0 and block.template[_i][_j] != '.' and game_area[pos_y + _i][pos_x + _j] != '.':
                    return False
        return True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    start = True
                    game_over = False
                    score = 0
                    last_drop_time = time.time()
                    # last_press_time = time.time()
                    game_area = [['.'] * BLOCK_WIDTH for _ in range(BLOCK_HEIGHT)]
                    this_block = blocks.get_block()
                    next_block = blocks.get_block()
                    this_block_pos_x = (BLOCK_WIDTH - this_block.end_pos.X - 1) // 2
                    this_block_pos_y = -1 - this_block.end_pos.Y
                if event.key == K_SPACE:
                    if not game_over:
                        pause = not pause
                elif event.key in (K_w, K_UP):
                    up = True

                elif event.key in (K_a, K_LEFT):
                    left = True

                elif event.key in (K_d, K_RIGHT):
                    right = True

                elif event.key in (K_s, K_DOWN):
                    down = True

            if event.type == KEYUP:
                if event.key in (K_w, K_UP):
                    up = False

                elif event.key in (K_a, K_LEFT):
                    left = False

                elif event.key in (K_d, K_RIGHT):
                    right = False

                elif event.key in (K_s, K_DOWN):
                    down = False
        if pause:
            continue

        if up:
            # 旋转
            # 在最右边靠边的情况下是不能旋转的，这里我们就按不能旋转来做
            # 我们在形状设计的时候做了很多的空白，这样只需要规定整个形状包括空白部分全部在游戏区域内时才可以旋转
            if 0 <= this_block_pos_x <= BLOCK_WIDTH - len(this_block.template[0]):
                _next_block = blocks.get_next_block(this_block)
                if _judge(this_block_pos_x, this_block_pos_y, _next_block):
                    this_block = _next_block
            time.sleep(0.17)
        if left and not game_over:
            # if time.time() - last_press_time > 0.07:
            #     last_press_time = time.time()
            if this_block_pos_x > - this_block.start_pos.X:
                if _judge(this_block_pos_x - 1, this_block_pos_y, this_block):
                    this_block_pos_x -= 1
            time.sleep(0.157)
        if right and not game_over:
            # if time.time() - last_press_time > 0.07:
            #     last_press_time = time.time()
            # 不能移出右边框
            if this_block_pos_x + this_block.end_pos.X + 1 < BLOCK_WIDTH:
                if _judge(this_block_pos_x + 1, this_block_pos_y, this_block):
                    this_block_pos_x += 1
            time.sleep(0.157)
        if down and not game_over:
            # if time.time() - last_press_time > 0.07:
            #     last_press_time = time.time()
            if not _judge(this_block_pos_x, this_block_pos_y + 1, this_block):
                _dock()
            else:
                last_drop_time = time.time()
                this_block_pos_y += 1
            time.sleep(0.13)

        try:
            color = next_block.color
        except AttributeError:
            color = (30, 200, 30)

        draw_background(screen, BG_COLOR)
        draw_game_area(screen, game_area)
        draw_gridlines(screen)
        draw_info(screen, font1, font_pos_x, font1_height, score)
        draw_block(screen, next_block, font_pos_x, 30 + (font1_height + 6) * 5, 0, 0, color)

        if not game_over:
            this_drop_time = time.time()
            draw_gridlines(screen)
            if this_drop_time - last_drop_time > speed:
                if pause:
                    continue

                # 不应该在下落的时候来判断到底没，我们玩俄罗斯方块的时候，方块落到底的瞬间可以进行左右移动
                if not _judge(this_block_pos_x, this_block_pos_y + 1, this_block):
                    _dock()
                else:
                    last_drop_time = this_drop_time
                    this_block_pos_y += 1
        else:
            if start:
                print_text(screen, font2,
                           (SCREEN_WIDTH - gameover_size[0]) // 2, (SCREEN_HEIGHT - gameover_size[1]) // 2,
                           'GAME OVER', RED)
            else:
                screen.fill(BG_COLOR)
                print_text(screen, font1, SCREEN_WIDTH - 370, SCREEN_HEIGHT - 500, 'Press any key to continue.')

        # 画当前下落方块
        try:
            color = this_block.color
        except:
            color = (30, 200, 30)
        draw_block(screen, this_block, 0, 0, this_block_pos_x, this_block_pos_y, color)

        pygame.display.flip()


# 画背景
def draw_background(screen, bgcolor):
    # 填充背景色
    screen.fill(bgcolor)
    # 画游戏区域分隔线
    pygame.draw.line(screen, BORDER_COLOR,
                     (SIZE * BLOCK_WIDTH + BORDER_WIDTH // 2, 0),
                     (SIZE * BLOCK_WIDTH + BORDER_WIDTH // 2, SCREEN_HEIGHT), BORDER_WIDTH)


# 画网格线
def draw_gridlines(screen):
    # 画网格线 竖线
    for x in range(BLOCK_WIDTH):
        pygame.draw.line(screen, BLACK, (x * SIZE, 0), (x * SIZE, SCREEN_HEIGHT), 1)
    # 画网格线 横线
    for y in range(BLOCK_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, y * SIZE), (BLOCK_WIDTH * SIZE, y * SIZE), 1)


# 画已经落下的方块
def draw_game_area(screen, game_area):
    if game_area is not None:
        for i, row in enumerate(game_area):
            for j, cell in enumerate(row):
                if cell != '.':
                    pygame.draw.rect(screen, BLOCK_COLOR, (j * SIZE, i * SIZE, SIZE, SIZE), 0)


# 画单个方块
def draw_block(screen, block, offset_x, offset_y, pos_x, pos_y, color):
    if block:
        for i in range(block.start_pos.Y, block.end_pos.Y + 1):
            for j in range(block.start_pos.X, block.end_pos.X + 1):
                if block.template[i][j] != '.':
                    pygame.draw.rect(screen, color,
                                     (offset_x + (pos_x + j) * SIZE,
                                      offset_y + (pos_y + i) * SIZE,
                                      SIZE, SIZE), 0)


# 画得分等信息
def draw_info(screen, font, pos_x, font_height, score):
    print_text(screen, font, pos_x, 10, f'得分: ')
    print_text(screen, font, pos_x, 10 + font_height + 6, f'{score}')
    print_text(screen, font, pos_x, 20 + (font_height + 6) * 2, f'速度: ')
    print_text(screen, font, pos_x, 20 + (font_height + 6) * 3, f'{score // 10000}')
    print_text(screen, font, pos_x, 30 + (font_height + 6) * 4, f'下一个：')


if __name__ == '__main__':
    main()
