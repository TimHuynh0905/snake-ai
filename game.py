import sys
import pygame

from settings import Settings
from utils import *
from snake import Snake
from apple import Apple

class SnakeGame:
    def __init__(self, snakePositions=None, applePosition=None, score=0):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.score = score
        
        if snakePositions is not None: self.snake = Snake(self, snakePositions=snakePositions)
        else: self.snake = Snake(self, snakePositions=self.settings.snakePositions)
        
        if applePosition is not None: self.apple = Apple(self, applePosition=applePosition)
        else: self.apple = Apple(self, applePosition=self.settings.applePosition)
        
        self.clock = pygame.time.Clock()
    
    def run_game(self, buttonDirection=None):
        gameover = False
        while gameover is not True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
                    sys.exit()
            self.screen.fill(self.settings.screen_color)
            self._drawGrid(rows=self.settings.rows)
            if buttonDirection is not None: 
                self._updateSnake(buttonDirection)
            else: 
                self._checkPressed()
                currentDV, isFrontBlocked, isLeftBlocked, isRightBlocked = blockedDirections(self.snake.positions)
                if isFrontBlocked == 1 and isLeftBlocked == 1 and isRightBlocked == 1: 
                    gameover = True
            self._updateScreen()
            self.clock.tick(20)
            if buttonDirection is not None: return self.snake.positions, self.apple.position, self.score

    def _updateSnake(self, buttonDirection):
        newHead = self.snake.positions[0].copy()
        if buttonDirection == 3:   newHead[1] = self.snake.positions[0][1] - self.settings.sizeBtwn
        elif buttonDirection == 2: newHead[1] = self.snake.positions[0][1] + self.settings.sizeBtwn
        elif buttonDirection == 0: newHead[0] = self.snake.positions[0][0] - self.settings.sizeBtwn
        elif buttonDirection == 1: newHead[0] = self.snake.positions[0][0] + self.settings.sizeBtwn
        
        if newHead == self.apple.position:
            self.apple.updatePosition()
            self.score += 1
            self.snake.positions.insert(0, newHead)
        else:
            self.snake.positions.insert(0, newHead)
            self.snake.positions.pop()
        
    def _checkPressed(self):
        keys = pygame.key.get_pressed()
        pressed=False
        newHead = self.snake.positions[0].copy()
        if keys[pygame.K_UP]:
            newHead[1] = self.snake.positions[0][1] - self.settings.sizeBtwn
            pressed=True
        elif keys[pygame.K_DOWN]:
            newHead[1] = self.snake.positions[0][1] + self.settings.sizeBtwn
            pressed=True
        elif keys[pygame.K_LEFT]:
            newHead[0] = self.snake.positions[0][0] - self.settings.sizeBtwn
            pressed=True
        elif keys[pygame.K_RIGHT]:
            newHead[0] = self.snake.positions[0][0] + self.settings.sizeBtwn
            pressed=True
        
        if pressed:
            if newHead == self.apple.position:
                self.apple.updatePosition()
                self.score += 1
                self.snake.positions.insert(0, newHead)
            else:
                self.snake.positions.insert(0, newHead)
                self.snake.positions.pop()

    def _updateScreen(self):
        self.snake.draw_snake()
        self.apple.draw_apple()
        pygame.display.set_caption(f"YOUR SCORE = {self.score}")
        pygame.display.update()

    def _drawGrid(self, rows):
        x = 0
        y = 0
        for l in range(rows):
            x = x + self.settings.sizeBtwn
            y = y + self.settings.sizeBtwn
            pygame.draw.line(self.screen, self.settings.grid_color, (x,0),(x,self.settings.screen_width))
            pygame.draw.line(self.screen, self.settings.grid_color, (0,y),(self.settings.screen_width,y))

if __name__ == "__main__" :
    game = SnakeGame()
    game.run_game()