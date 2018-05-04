import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button


def run_game():
    """初始化游戏并创建一个屏幕对象"""

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            # 删除已消失的子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 每次循环时都重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button)


run_game()
