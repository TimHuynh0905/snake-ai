import pygame
import random

class Apple:
    def __init__(self, snake_game, applePosition):
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.position = applePosition
        self.color = self.settings.appleColor

    def draw_apple(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.position[0], self.position[1], self.settings.sizeBtwn, self.settings.sizeBtwn))

    def updatePosition(self):
        # temp = self.position.copy()
        self.position = [random.randint(1,self.settings.rows-2)*self.settings.sizeBtwn, random.randint(1,self.settings.rows-2)*self.settings.sizeBtwn]
        # while (temp == self.position):
        #     self.position = [random.randint(1,18)*self.settings.sizeBtwn, random.randint(1,18)*self.settings.sizeBtwn]
        self.color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))  