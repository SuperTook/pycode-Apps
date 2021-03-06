#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： C.zf
# 开发人员 ： C.Z.F
# 开发时间 ： 2020/7/26 14:34
# 文件名称 ： NW_Snake.py
# 开发工具 ： PyCharm
import random
import sys
import pygame
from pygame.locals import *

TMS = 0
REFPS = 85
FPS = REFPS  # 屏幕刷新率（在这里相当于贪吃蛇的速度）
CELL_SIZE = 5  # 小方格的大小
WIDTH = CELL_SIZE * 310  # 屏幕宽度（约1750）
HEIGHT = CELL_SIZE * 160  # 屏幕高度（约900）
SCORE = 0
LIFE = 5

# 断言，屏幕的宽和高必须能被方块大小整除
assert WIDTH % CELL_SIZE == 0, "Window width must be a multiple of cell size."
assert HEIGHT % CELL_SIZE == 0, "Window height must be a multiple of cell size."

# 横向和纵向的方格数
CELL_WIDTH = int(WIDTH / CELL_SIZE)
CELL_HEIGHT = int(HEIGHT / CELL_SIZE)

# 定义几个常用的颜色
# R G B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREEN = (0, 155, 0)
DARKBLUE = (0, 0, 155)
DARKRED = (155, 0, 0)
DARKGRAY = (40, 40, 40)
LDARKGRAY = (50, 50, 50)
BGCOLOR = [40] * 3

# 定义贪吃蛇的动作
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

stateList = ['proto', 'big', 'bomb', 'life']  # todo

HEAD = 0
pygame.init()
FPSCLOCK = pygame.time.Clock()  # 获得pygame时钟
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))  # 设置屏幕宽高
BASICFONT = pygame.font.Font("fonts/PAPYRUS.TTF", 18)  # BASICFONT

SCORE_WAV = pygame.mixer.Sound('audio/score.wav')
BUMP_WAV = pygame.mixer.Sound('audio/bump.wav')


def main():
    pygame.display.set_caption('贪吃蛇 - 新版')  # 设置窗口的标题
    showStartScreen()  # 显示开始画面

    while True:
        # 这里一直循环于开始游戏和显示游戏结束画面之间，
        # 运行游戏里有一个循环，显示游戏结束画面也有一个循环
        # 两个循环都有相应的return，这样就可以达到切换这两个模块的效果

        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后，退出程序
                pygame.quit()
                sys.exit()
        status = runGame()  # 运行游戏
        if status == 'over':
            gameOver()  # 显示游戏结束画面


def runGame():
    # 随机初始化设置一个点作为贪吃蛇的起点
    global FPS, SCORE, LIFE, BGCOLOR
    bgcolor = list(DARKGRAY)
    startx = random.randint(5, 10)
    starty = random.randint(5, 10)

    # 以这个点为起点，建立一个贪吃蛇
    snakeCoords = [{'x': startx - i, 'y': starty} for i in range(10)]
    direction = RIGHT  # 初始化一个运动的方向

    # 随机一个apple的位置
    apple1 = randLocation()  # 有点点酸，却也很甜，还很健康的苹果
    apple2 = randLocation()  # 酸大于甜，但却是最健康的的小苹果
    apple3 = randLocation()  # 又香又甜又大，却含剧毒的苹果
    apple4 = randLocation()  # 微毒的苹果，小蛇长大了自可解毒

    while True:  # 游戏主循环
        for event in pygame.event.get():  # 事件处理
            if event.type == QUIT:  # 退出事件
                terminate()
            elif event.type == KEYDOWN:  # 按键事件
                # 如果按下的是左键或A键（传说中的ASDW），且当前的方向不是向右，就改变方向，以此类推
                if event.key == K_LEFT or event.key == K_a:
                    direction = LEFT
                elif event.key == K_RIGHT or event.key == K_d:
                    direction = RIGHT
                elif event.key == K_UP or event.key == K_w:
                    direction = UP
                elif event.key == K_DOWN or event.key == K_s:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    print('[LOG]', TMS, ':', SCORE, '/', FPS)
                    terminate()

        # 检查贪吃蛇是否撞到撞到边界
        if (snakeCoords[HEAD]['x'] <= 0
                or snakeCoords[HEAD]['x'] >= CELL_WIDTH
                or snakeCoords[HEAD]['y'] <= 2
                or snakeCoords[HEAD]['y'] >= CELL_HEIGHT):
            if direction == RIGHT:
                direction = LEFT
            elif direction == DOWN:
                direction = UP
            elif direction == LEFT:
                direction = RIGHT
            elif direction == UP:
                direction = DOWN
            else:
                direction = None
            LIFE -= 3
            BUMP_WAV.play()

        # 检查贪吃蛇是否撞到自己
        # for wormBody in wormCoords[1:]:
        #     if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
        #         return 'over'  # game over

        if LIFE < 0:
            return 'over'

        # 检查贪吃蛇是否吃到apple
        apple1xy = [[i for i in range(apple1['x'] - 3, apple1['x'] + 3)],
                    [i for i in range(apple1['y'] - 3, apple1['y'] + 3)]]
        apple2xy = [[i for i in range(apple2['x'] - 3, apple2['x'] + 3)],
                    [i for i in range(apple2['y'] - 3, apple2['y'] + 3)]]
        apple3xy = [[i for i in range(apple3['x'] - 3, apple3['x'] + 3)],
                    [i for i in range(apple3['y'] - 3, apple3['y'] + 3)]]
        apple4xy = [[i for i in range(apple4['x'] - 3, apple4['x'] + 3)],
                    [i for i in range(apple4['y'] - 3, apple4['y'] + 3)]]
        if snakeCoords[HEAD]['x'] in apple1xy[0] and snakeCoords[HEAD]['y'] in apple1xy[1]:
            SCORE_WAV.play()
            # 不移除蛇的最后一个尾巴格
            apple1 = randLocation()
            apple2 = random.choice([apple2, randLocation()])
            if SCORE < 40:
                FPS += 0.5
                SCORE += 2
            elif SCORE >= 40:
                if FPS > REFPS:
                    FPS -= 0.1
                SCORE += 2
                LIFE += 1

            if bgcolor[0] > 0:
                bgcolor = [i - 1 for i in bgcolor]
                BGCOLOR = bgcolor
        elif snakeCoords[HEAD]['x'] in apple2xy[0] and snakeCoords[HEAD]['y'] in apple2xy[1]:
            SCORE_WAV.play()
            # 不移除蛇的最后一个尾巴格
            apple2 = randLocation()
            apple3 = random.choice([apple3, randLocation()])
            if SCORE < 40:
                FPS += 0.5
                SCORE += 0.5
                LIFE += 5
            elif SCORE >= 40:
                if FPS > REFPS:
                    FPS -= 0.1
                SCORE += 0.5

            if bgcolor[0] > 0:
                bgcolor = [i - 1 for i in bgcolor]
                BGCOLOR = bgcolor
        elif snakeCoords[HEAD]['x'] in apple3xy[0] and snakeCoords[HEAD]['y'] in apple3xy[1]:
            SCORE_WAV.play()
            # 不移除蛇的最后一个尾巴格
            apple3 = randLocation()
            apple4 = random.choice([apple4, randLocation()])
            if SCORE < 40:
                FPS += 0.5
                SCORE += 3
                LIFE -= 1
            elif SCORE >= 40:
                if FPS > REFPS:
                    FPS -= 0.1
                SCORE += 3
                LIFE -= 2

            if bgcolor[0] > 0:
                bgcolor = [i - 1 for i in bgcolor]
                BGCOLOR = bgcolor
        elif snakeCoords[HEAD]['x'] in apple4xy[0] and snakeCoords[HEAD]['y'] in apple4xy[1]:
            SCORE_WAV.play()
            # 不移除蛇的最后一个尾巴格
            apple4 = randLocation()
            apple1 = random.choice([apple1, randLocation()])
            if SCORE < 40:
                FPS += 0.3
                SCORE += 2
                LIFE -= 1
            elif SCORE >= 40:
                if FPS > REFPS:
                    FPS -= 0.1
                SCORE += 1.5

            if bgcolor[0] > 0:
                bgcolor = [i - 1 for i in bgcolor]
                BGCOLOR = bgcolor
        else:
            del snakeCoords[-1]  # 移除蛇的最后一个尾巴格

        new_head = None
        # 根据方向，添加一个新的蛇头，以这种方式来移动贪吃蛇
        if direction == UP:
            new_head = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            new_head = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            new_head = {'x': snakeCoords[HEAD]['x'] - 1, 'y': snakeCoords[HEAD]['y']}
        elif direction == RIGHT:
            new_head = {'x': snakeCoords[HEAD]['x'] + 1, 'y': snakeCoords[HEAD]['y']}

        # 插入新的蛇头在数组的最前面
        snakeCoords.insert(0, new_head)
        # 绘制背景
        DISPLAYSURF.fill(BGCOLOR)
        drawSnake(snakeCoords)
        drawApple(apple1, RED, DARKRED)
        drawApple(apple2, GREEN, DARKGREEN)
        drawApple(apple3, BLUE, DARKBLUE)
        drawApple(apple4, BLUE, DARKBLUE)
        drawScore()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


# 绘制提示消息
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to continue.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WIDTH - 230, HEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


# 检查按键是否有按键事件
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


# 显示开始画面
def showStartScreen():
    DISPLAYSURF.fill(BGCOLOR)

    titleFont = pygame.font.SysFont('SimHei', 100)
    appleFont = pygame.font.SysFont('SimHei', 17)

    titleSurf = titleFont.render('游戏开始！', True, WHITE)
    titleRect = titleSurf.get_rect()
    titleRect.center = (int(WIDTH / 2)+50, int(HEIGHT / 2)-150)
    DISPLAYSURF.blit(titleSurf, titleRect)

    appleSurf1 = appleFont.render('红苹果：有点点酸，却也很甜，还很健康的苹果', True, WHITE)
    appleSurf2 = appleFont.render('绿苹果：酸大于甜，但却是最健康的的小苹果', True, WHITE)
    appleSurf3 = appleFont.render('蓝苹果：又香又甜又大，却含剧毒的苹果', True, WHITE)

    as1Rect = appleSurf1.get_rect()
    as1Rect.topleft = (310, 400)
    DISPLAYSURF.blit(appleSurf1, as1Rect)

    as2Rect = appleSurf1.get_rect()
    as2Rect.topleft = (310, 450)
    DISPLAYSURF.blit(appleSurf2, as2Rect)

    as3Rect = appleSurf1.get_rect()
    as3Rect.topleft = (310, 500)
    DISPLAYSURF.blit(appleSurf3, as3Rect)

    drawPressKeyMsg()

    pygame.display.update()

    while True:

        if checkForKeyPress():
            pygame.event.get()  # 清除事件队列
            return


# 退出
def terminate():
    pygame.quit()
    sys.exit()


# 随机生成一个坐标位置
def randLocation():
    return {'x': random.randint(30, CELL_WIDTH - 30), 'y': random.randint(30, CELL_HEIGHT - 30)}


# 随机生成一个状态
def randState():
    rd = random.randint(0, 10)
    ls = stateList
    if rd in [0, 1, 2, 3]: return ls[0]
    if rd in [4, 5]: return ls[1]
    if rd in [6, 7, 8]: return ls[2]
    if rd in [9, 10]: return ls[3]


# 显示游戏结束画面
def gameOver():
    global TMS, FPS, SCORE
    TMS += 1
    FPS = REFPS
    SCORE = 0
    gameOverFont = pygame.font.Font('fonts/PAPYRUS.TTF', 70)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (int(WIDTH / 2), int(HEIGHT / 2 - gameRect.height - 10))
    overRect.midtop = (int(WIDTH / 2), int(HEIGHT / 2))

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    print('[LOG]', TMS, ':', SCORE, '/', FPS)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return


# 绘制分数
def drawScore():
    scoreSurf = BASICFONT.render(f'Score: {SCORE}', True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WIDTH - 120, 10)

    lifeSurf = BASICFONT.render(f'Life: {LIFE}', True, WHITE)
    lifeRect = lifeSurf.get_rect()
    lifeRect.topleft = (20, 10)

    DISPLAYSURF.blit(scoreSurf, scoreRect)
    DISPLAYSURF.blit(lifeSurf, lifeRect)


# 根据 coord 数组绘制贪吃蛇
def drawSnake(snakeCoord):
    wdt = int(SCORE / 20) + 1
    clr = GREEN

    for coord in snakeCoord:
        x = coord['x'] * CELL_SIZE
        y = coord['y'] * CELL_SIZE
        wormSegmentRect = pygame.Rect(x,
                                      y,
                                      CELL_SIZE * wdt,
                                      CELL_SIZE * wdt)
        pygame.draw.rect(DISPLAYSURF, clr, wormSegmentRect)

        wormInnerSegmentRect = pygame.Rect(x - CELL_SIZE / 2,
                                           y - CELL_SIZE / 2,
                                           CELL_SIZE * wdt + CELL_SIZE / 2,
                                           CELL_SIZE * wdt + CELL_SIZE / 2)
        pygame.draw.rect(DISPLAYSURF, clr, wormInnerSegmentRect)


# 根据 coord 绘制 apple | todo 据state更改模式
def drawApple(coord, color, dcolor):
    x = coord['x'] * CELL_SIZE
    y = coord['y'] * CELL_SIZE

    appleRect1 = pygame.Rect(x - CELL_SIZE * 3,
                             y - CELL_SIZE * 3,
                             CELL_SIZE * 6,
                             CELL_SIZE * 6)
    pygame.draw.rect(DISPLAYSURF, dcolor, appleRect1)

    appleRect2 = pygame.Rect(x - CELL_SIZE * 2,
                             y - CELL_SIZE * 2,
                             CELL_SIZE * 4,
                             CELL_SIZE * 4)
    pygame.draw.rect(DISPLAYSURF, color, appleRect2)


# 绘制所有的方格
# def drawGrid():
#     for x in range(0, WIDTH, CELL_SIZE):  # 横
#         pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, HEIGHT))
#     for y in range(0, HEIGHT, CELL_SIZE):  # 竖
#         pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WIDTH, y))


if __name__ == '__main__':
    main()
