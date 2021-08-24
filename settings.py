class Settings:
    def __init__(self):
        #关于屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船设置

        self.ship_limit = 3
        #子弹设置

        self.bullet_width= 5
        self.bullet_height = 15
        self.bullet_color=(60,60,60)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 5
        #加快游戏节奏的scale
        self.speedup_scale = 1.1
        #提高射杀外星人得分数
        self.score_scale = 1.5
        #得分处理
        self.alien_points = 50
        #各种物件的速度设置
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1.0
        self.fleet_direction=1
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
