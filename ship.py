import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_game):
        #继承sprite父类的特性
        super(Ship, self).__init__()
        #引入屏幕和设置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #导入照片
        self.image = pygame.image.load(r'C:\Users\lxy\PycharmProjects\pythonProject6\image\nini.bmp')
        self.rect = self.image.get_rect()
        #让照片顶部中间与屏幕底部中间相等
        self.rect.midbottom = self.screen_rect.midbottom
        #更新飞船
        self.x=float(self.rect.x)
        #设置标志
        self.moving_right = False
        self.moving_left = False
    #更新飞船
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    #画出飞船
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)