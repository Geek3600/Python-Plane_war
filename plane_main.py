import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):

        # 创建背景和背景组（将背景当作精灵创建）
        bg1 = BackGround()
        bg2 = BackGround(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")

        # 游戏主程序在这！！！
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 事件监听
            self.__event__handler()

            # 碰撞检测
            self.__check__collide()

            # 更新绘制各精灵组的位置
            self.__update__sprites()

            # 更新所有帧的绘制显示
            pygame.display.update()

    # 事件监听（根据监听用户的操作来做出相应的反应）
    def __event__handler(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over__()

            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到精灵组中
                self.enemy_group.add(enemy)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            print("向右移动...")
        elif keys_pressed[pygame.K_LEFT]:
            print("向左移动...")

    # 碰撞检测
    def __check__collide(self):
        pass

    # 游戏所有元素的实时更新
    def __update__sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over__():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()


