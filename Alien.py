import pygame
from pygame.sprite import Sprite

import settings


class Alien(Sprite):
    def __init__(self,ai_game):
        super(Alien, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(r'C:\Users\lxy\PycharmProjects\pythonProject6\image\hero2.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True

    def update(self):
        self.x += self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x = self.x