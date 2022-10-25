import pygame


class Settings():
    def __init__(self):
        self.screen_width = 700
        self.screen_height = 430
        self.bg = pygame.image.load('bg.png')
        self.miss_limit = 3
