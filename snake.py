import pygame
import random
# from pygame.sprite import Sprite

class Snake():
    def __init__(self, snake_game, snakePositions):        
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.screen_rect = snake_game.screen_rect
        self.positions = snakePositions
        self.snake_color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
    
    def draw_snake(self):
        for position in self.positions:
            pygame.draw.rect(self.screen, self.snake_color, pygame.Rect(position[0], position[1], self.settings.sizeBtwn, self.settings.sizeBtwn))