import pygame
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
# 游戏循环，防止窗口消失
while True:
    pass

pygame.quit()
