import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    """Init game and create a screen object."""
    
    # 初始化所有导入的pygame对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个名为screen的窗口 (1200, 800)是一个元组, 指定游戏窗口尺寸
    # screen 是一个 surface, 游戏中的每个元素(外星人飞船)都是一个surface
    # 激活游戏的动画循环后, 没经过一次循环都将自动重绘这个surface
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # 事件是用户玩游戏时执行的操作, 如按键和移动鼠标
        # 为让程序响应事件, 编写一个事件循环, 以侦听事件, 并根据发生的事件执行相应任务
        for event in pygame.event.get():
            # pygame.QUIT 事件
            if event.type == pygame.QUIT:
                # sys模块来退出
                sys.exit()
        
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # 让最近绘制的屏幕可见
        # 每次执行while循环时都绘制一个空屏幕, 并擦去旧屏幕, 使得只有新屏幕可见
        # 当我们移动游戏元素, pygame.display.flip()将不断更新屏幕 
        # 以显示元素的新位置, 并在原来位置隐藏元素, 从而造成平滑移动的效果
        pygame.display.flip()

run_game()
