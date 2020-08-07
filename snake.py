import pygame
import random
# from pygame.sprite import Sprite

class Snake():
    def __init__(self, snake_game):        
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.screen_rect = snake_game.screen_rect
        self.startPos = [self.settings.snakeStartPosX, self.settings.snakeStartPosY]
        self.positions = [self.startPos, ]
        self.snake_color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))

        self.lastTime = 0
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
    
    def draw_snake(self):
        for position in self.positions:
            pygame.draw.rect(self.screen, self.snake_color, pygame.Rect(position[0], position[1], self.settings.sizeBtwn, self.settings.sizeBtwn))
        # self.update()

    def update(self):
        temp = self.positions[0].copy()
        self.updateHead()
        if len(self.positions) > 1:
            # print("flag1")
            # print(self.positions)
            i = len(self.positions) - 1
            while (i > 1):
                self.positions[i] = self.positions[i-1]
                i -= 1
            self.positions[1] = temp
            # print("flag2")
            # print(self.positions)

    def updateHead(self):
        if self.moving_up and self.positions[0][1] > 0:
            self.positions[0][1] -= self.settings.sizeBtwn
                
        if self.moving_down and self.positions[0][1] < self.settings.screen_height-self.settings.sizeBtwn:
            self.positions[0][1] += self.settings.sizeBtwn
                
        if self.moving_right and self.positions[0][0] < self.settings.screen_width-self.settings.sizeBtwn:
            self.positions[0][0] += self.settings.sizeBtwn
                
        if self.moving_left and self.positions[0][0] > 0:
            self.positions[0][0] -= self.settings.sizeBtwn