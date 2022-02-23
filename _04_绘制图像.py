import pygame
pygame.init()
# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
bg = pygame.image.load("./images/images/background.png")
screen.blit(bg, (0,0))
pygame.display.update()

# 绘制英雄图像


# 游戏循环，防止窗口消失
while True:
    pass

pygame.quit()
