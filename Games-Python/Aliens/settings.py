import pygame

class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """"Инициализирует настройки игры"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.image = pygame.image.load('images/space__.jpg')
        # Настройки корабля
        self.ship_speed_factor = 5

        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Настройка пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 40
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1
