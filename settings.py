import random

class Settings:
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.screen_color = (255,255,255)
        self.grid_color = (0,0,0)
        self.rows = 20    
        self.sizeBtwn = self.screen_width // self.rows
        self.timeDelayInterval = 500
        
        self.snakeStartPosX = random.randint(0,19)*self.sizeBtwn
        self.snakeStartPosY = random.randint(0,19)*self.sizeBtwn

        self.applePosX = random.randint(1,18)*self.sizeBtwn
        self.applePosY = random.randint(1,18)*self.sizeBtwn
        self.appleColor = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
