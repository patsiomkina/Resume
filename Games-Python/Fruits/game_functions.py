import sys
import pygame


def check_events(cart, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and cart.x < settings.screen_width - cart.width:
        cart.x += cart.speed
    elif keys[pygame.K_LEFT] and cart.x > 0:
        cart.x -= cart.speed


def screen_update():
    pygame.display.flip()
