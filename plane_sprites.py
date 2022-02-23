import random
import pygame


# 定义一个屏幕大小的常量（创建矩形对象）
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 100
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GamesSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在垂直方向上移动
        self.rect.y += self.speed


class BackGround(GamesSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):

        # 调用父类方法
        super().__init__("./images/images/background.png")

        # 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 调用父类的方法实现
        super().update()

        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GamesSprite):

    def __init__(self):
        # 调用父类方法创建敌机精灵
        super().__init__("./images/images/enemy1.png")
        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 5)
        # 指定敌机的初始随机位置

        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 调用父类初始化方法
        super().update()

        # 判断敌机是否飞出了屏幕
        if self.rect.y >= SCREEN_RECT.height:

            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GamesSprite):

    def __init__(self):

        # 调用父类方法
        super().__init__("./images/images/me1.png", 0)

        # 设置英雄的初始位置
        self.rect.centerx= SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120