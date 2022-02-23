import pygame
from plane_sprites import *

pygame.init()


# 创建游戏窗口（创建对象） 480 * 700
screen = pygame.display.set_mode((480,700))


# 绘制背景图像
bg = pygame.image.load("./images/images/background.png")
screen.blit(bg, (0,0))
# pygame.display.update()


# 绘制英雄图像
hero = pygame.image.load("./images/images/me1.png")
screen.blit(hero, (200, 500))
# pygame.display.update()


# 可以在所有绘制工作完成之后，再统一调用一次update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 记录英雄的初始位置
hero_rect = pygame.Rect(200,500,102,126)

# 创建敌机的精灵
enemy1 = GamesSprite("./images/images/enemy1.png", 1)
enemy2 = GamesSprite("./images/images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy1,enemy2)


# 游戏循环，游戏正式开始
while True:
    # 指定循环体内部的代码执行的频率
    clock.tick(100)

    # 事件监听,并控制退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏....")

            # 卸载所有模块
            pygame.quit()

            # 直接终止当前正在执行的程序
            exit()

     # 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y == -126:
        hero_rect.y = 700

    # 绘制飞机图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵族调用两个方法
    # update
    enemy_group.update()
    enemy_group.draw(screen)





    # 更新绘制的图像
    pygame.display.update()




