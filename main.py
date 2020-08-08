import numpy as np
from keras.models import model_from_json

from game import SnakeGame
from utils import *

def playAI(numGames, numSteps, model):
    sum = 0
    highScore = 0
    for _ in range(numGames):
        game = SnakeGame()
        for _ in range(numSteps):
            angle, appleDV_Normalized, snakeDV_Normalized = angleSnakeApple(game.snake.positions, game.apple.position)
            currentDV, isFrontBlocked, isLeftBlocked, isRightBlocked = blockedDirectionsTrain(game.snake.positions, game.apple.position)
            X = [isLeftBlocked, isFrontBlocked, isRightBlocked, 
                 appleDV_Normalized[0], snakeDV_Normalized[0], 
                 appleDV_Normalized[1], snakeDV_Normalized[1]]
            # X = [isLeftBlocked, isFrontBlocked, isRightBlocked, angle]
            X = np.array(X).reshape(-1,len(X))
            predicted_direction = np.argmax(np.array(model.predict(X)))-1
            # print(predicted_direction)
            updated_direction, button_direction = directionVector(game.snake.positions,angle,predicted_direction)
            
            if isBlocked(game.snake.positions, currentDV) == 1: 
                # print(X)
                # print(predicted_direction)
                break

            _, _, _ = game.run_game(buttonDirection=button_direction)
        print("SCORE = "+str(game.score))
        sum += game.score
        if (game.score > highScore): highScore = game.score
    return sum//numGames, highScore

if __name__ == "__main__":
    numGames = 20
    numSteps = 2000

    json_file = open('snake_ai.json', 'r')
    loaded_model = json_file.read()
    model = model_from_json(loaded_model)
    model.load_weights('snake_ai.h5')
    averagedScore, highScore = playAI(numGames=numGames, numSteps=numSteps, model=model)
    print("AVERAGED SCORE = "+str(averagedScore))
    print("HIGH SCORE = "+str(highScore))
