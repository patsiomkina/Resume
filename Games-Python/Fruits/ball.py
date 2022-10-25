import pygame
from random import randint
from time import sleep


class Ball():
    def __init__(self, screen, settings):
        self.x = randint(1, settings.screen_width - 40)
        self.y = 0
        self.image = pygame.image.load('berry.png')
        self.width = 40
        self.height = 50
        self.speed = 1
        self.screen = screen

    def show_ball(self):
        self.screen.blit(self.image, (self.x, self.y))

    def ball_down(self, settings, stats):
        if self.y < settings.screen_height:
            self.y += self.speed
            self.show_ball()
        else:
            self.ball_reset(settings)
            self.miss_ball(stats)

    def ball_reset(self, settings):
        self.y = 0
        self.x = randint(1, settings.screen_width - 40)

    def ball_movement(self, settings, cart, stats):
        if cart.x < (self.x + self.width) and (cart.x + cart.width) > self.x and cart.y < (
                self.y + self.height) and (cart.height + cart.y) > self.y:
            self.ball_reset(settings)
        else:
            self.ball_down(settings, stats)


    def miss_ball(self, stats):
        if stats.miss_left > 0:
            stats.miss_left -= 1
            print("You have " + str(stats.miss_left) + " misses left!")
            sleep(0.5)
        else:
            stats.game_active = False
