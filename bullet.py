import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_game):
        super(Bullet, self).__init__()
        #继承父类，到此为止，接下来是导入screen和设置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #画出子弹轮廓，并将其与飞船上沿对齐
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # 旧活重整
        self.y=float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y=self.y

    def draw_bullets(self):
        pygame.draw.rect(self.screen,self.color,self.rect)