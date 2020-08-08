import random

class Settings:
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        
        color = random.randint(0,1)
        if color == 1: 
            self.screen_color = (255,255,255)
            self.grid_color = (0,0,0)
        else: 
            self.screen_color = (0,0,0)
            self.grid_color = (255,255,255)

        self.rows = 20
        self.sizeBtwn = self.screen_width // self.rows
        
        self.snakeStartPosX = random.randint(0,self.rows-1)*self.sizeBtwn
        self.snakeStartPosY = random.randint(0,self.rows-1)*self.sizeBtwn
        self.snakeHead = [self.snakeStartPosX, self.snakeStartPosY]
        self.snakeTail = [self.snakeStartPosX-self.sizeBtwn, self.snakeStartPosY]
        self.snakePositions = [self.snakeHead, self.snakeTail]

        self.applePosX = random.randint(1,self.rows-2)*self.sizeBtwn
        self.applePosY = random.randint(1,self.rows-2)*self.sizeBtwn
        self.applePosition = [self.applePosX, self.applePosY]
        self.appleColor = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
