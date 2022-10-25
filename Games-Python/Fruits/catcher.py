import pygame
from settings import Settings
import game_functions as gf
from cart import Cart
from ball import Ball
from stats import Stats


def run_game():
    pygame.init()
    catcher_settings = Settings()
    screen = pygame.display.set_mode((catcher_settings.screen_width, catcher_settings.screen_height))
    pygame.display.set_caption('Catcher')
    my_cart = Cart(0, catcher_settings.screen_height - 60, screen)
    my_ball = Ball(screen, catcher_settings)
    #missed_balls = my_ball.ball_movement(catcher_settings, my_cart)
    my_stats = Stats(catcher_settings)

    while True:
        screen.blit(catcher_settings.bg, (0, 0))
        gf.check_events(my_cart, catcher_settings)
        my_cart.show_cart()
        if my_stats.game_active:
            my_ball.ball_movement(catcher_settings, my_cart, my_stats)
        gf.screen_update()


run_game()
