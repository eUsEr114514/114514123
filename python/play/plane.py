import pygame
import random

# 初始化游戏
pygame.init()

# 设置游戏窗口大小
screen = pygame.display.set_mode((800, 600))

# 设置游戏标题和图标
pygame.display.set_caption("飞机大战")
icon = pygame.image.load("plane.png")
pygame.display.set_icon(icon)

# 设置玩家飞机
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# 设置敌方飞机
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# 游戏运行
running = True
while running:
    # 设置背景颜色
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 判断键盘操作
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 更新玩家飞机位置
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # 更新敌方飞机位置
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()