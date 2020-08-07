import sys
import pygame

from settings import Settings
from snake import Snake
from apple import Apple

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Snake AI Game")
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.clock = pygame.time.Clock()
    
    def run_game(self):
        gameover = False
        while gameover is not True:
            self._checkEvents()
            self.snake.update()
            self._checkCollision()
            self._updateScreen()
            if self.snake.positions[0] in self.snake.positions[1:len(self.snake.positions)]: gameover = True
            self.clock.tick(20)

    def _checkCollision(self):
        if (self.snake.positions[0] == self.apple.position):
            temp = self.apple.position
            self.apple.updatePosition()
            self.snake.updateHead()
            self.snake.positions.append(temp)

    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            self._checkPressed()
    
    def _checkPressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: 
            self.snake.moving_up = True
            self.snake.moving_down = False
            self.snake.moving_left = False
            self.snake.moving_right = False
        elif keys[pygame.K_DOWN]:
            self.snake.moving_up = False
            self.snake.moving_down = True
            self.snake.moving_left = False
            self.snake.moving_right = False
        elif keys[pygame.K_LEFT]:
            self.snake.moving_up = False
            self.snake.moving_down = False
            self.snake.moving_left = True
            self.snake.moving_right = False
        elif keys[pygame.K_RIGHT]:
            self.snake.moving_up = False
            self.snake.moving_down = False
            self.snake.moving_left = False
            self.snake.moving_right = True

    def _updateScreen(self):
        self.screen.fill(self.settings.screen_color)
        self._drawGrid(rows=self.settings.rows)
        self.snake.draw_snake()
        self.apple.draw_apple()
        pygame.display.flip()

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