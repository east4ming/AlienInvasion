import pygame
"""Game Character.

创建一个类, 将该游戏角色绘制到屏幕中央, 并将该图像的背景色设置为屏幕的背景色.
"""

class GameCharacter():
    def __init__(self, screen):
        """初始化游戏角色并设置其初始位置."""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/cciclogo.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        # 居中
        self.rect.center = self.screen_rect.center


    def blitme(self):
        """在指定位置绘制游戏角色."""
        self.screen.blit(self.image, self.rect)
