import pygame


class Cart():
    def __init__(self, x, y, screen):
        self.width = 60
        self.height = 58
        self.x = x
        self.y = y
        self.image = pygame.image.load('cart.png')
        self.screen = screen
        self.speed = 2

    def show_cart(self):
        self.screen.blit(self.image, (self.x, self.y))
