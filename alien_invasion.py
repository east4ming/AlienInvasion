import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from game_character import GameCharacter
import game_functions as gf


def run_game():
    """Init game and create a screen object."""
    
    # 初始化所有导入的pygame对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个名为screen的窗口 (1200, 800)是一个元组, 指定游戏窗口尺寸
    # screen 是一个 surface, 游戏中的每个元素(外星人飞船)都是一个surface
    # 激活游戏的动画循环后, 每经过一次循环都将自动重绘这个surface
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建一个游戏logo
    game_character = GameCharacter(screen)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    # 创建一艘飞船, 一个子弹编组, 一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # 事件是用户玩游戏时执行的操作, 如按键和移动鼠标
        # 为让程序响应事件, 编写一个事件循环, 以侦听事件, 并根据发生的事件执行相应任务
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
                        bullets)
        if stats.game_active:
            # 更新飞船位置, 未消失的子弹, 外星人位置
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, game_character,
                         aliens, bullets, play_button)


run_game()
