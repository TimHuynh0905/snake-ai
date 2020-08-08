from utils import *
from game import SnakeGame
from tqdm import tqdm

def newTrainingData():
    train_X = []
    train_y = []
    train_games = 10
    train_steps = 2000
    for _ in tqdm(range(train_games)):
        snakeHead, snakePositions, applePosition, score = startingPositions()
        game = SnakeGame(snakePositions, applePosition, score)
        for j in range(train_steps):
            angle, appleDV_Normalized, snakeDV_Normalized = angleSnakeApple(snakePositions, applePosition)
            direction, button_direction = nextDirection(snakePositions, angle) # FIRST STEP DETERMINE DIRECTION
            _, isFrontBlocked, isLeftBlocked, isRightBlocked = blockedDirectionsTrain(snakePositions, applePosition) # CHECK IF THAT DIRECTION WORKS
            _, updated_button_direction, train_y = getTrainY(
                snakePositions = snakePositions, 
                angle = angle, 
                button_direction = button_direction, 
                direction = direction, 
                train_y = train_y,
                isFrontBlocked = isFrontBlocked,
                isLeftBlocked = isLeftBlocked, 
                isRightBlocked = isRightBlocked
            )

            if isFrontBlocked == 1 and isLeftBlocked == 1 and isRightBlocked == 1:
                # print("Blocked")
                # print(snakePositions)
                # print(currentDV)
                # print(direction)
                break

            train_X.append(
                [isLeftBlocked, isFrontBlocked, isRightBlocked, 
                 appleDV_Normalized[0], snakeDV_Normalized[0], 
                 appleDV_Normalized[1], snakeDV_Normalized[1]]
            )

            # train_X.append(
            #     [isLeftBlocked, isFrontBlocked, isRightBlocked, angle]
            # )

            snakePositions, applePosition, score = game.run_game(buttonDirection=updated_button_direction)

    return train_X, train_y

def getTrainY(snakePositions, angle, button_direction, direction, train_y,
                             isFrontBlocked, isLeftBlocked, isRightBlocked):
    if direction == -1:
        if isLeftBlocked == 1:
            if isFrontBlocked == 1 and isRightBlocked == 0:
                direction, button_direction = directionVector(snakePositions, angle, 1)
                train_y.append([0, 0, 1])
            elif isFrontBlocked == 0 and isRightBlocked == 1:
                direction, button_direction = directionVector(snakePositions, angle, 0)
                train_y.append([0, 1, 0])
            elif isFrontBlocked == 0 and isRightBlocked == 0:
                direction, button_direction = directionVector(snakePositions, angle, 1)
                train_y.append([0, 1, 0])
        else:
            train_y.append([1, 0, 0])

    elif direction == 0:
        if isFrontBlocked == 1:
            if isLeftBlocked == 1 and isRightBlocked == 0:
                direction, button_direction = directionVector(snakePositions, angle, 1)
                train_y.append([0, 0, 1])
            elif isLeftBlocked == 0 and isRightBlocked == 1:
                direction, button_direction = directionVector(snakePositions, angle, -1)
                train_y.append([1, 0, 0])
            elif isLeftBlocked == 0 and isRightBlocked == 0:
                train_y.append([0, 0, 1])
                direction, button_direction = directionVector(snakePositions, angle, 1)
        else:
            train_y.append([0, 1, 0])
    else:
        if isRightBlocked == 1:
            if isLeftBlocked == 1 and isFrontBlocked == 0:
                direction, button_direction = directionVector(snakePositions, angle, 0)
                train_y.append([0, 1, 0])
            elif isLeftBlocked == 0 and isFrontBlocked == 1:
                direction, button_direction = directionVector(snakePositions, angle, -1)
                train_y.append([1, 0, 0])
            elif isLeftBlocked == 0 and isFrontBlocked == 0:
                direction, button_direction = directionVector(snakePositions, angle, -1)
                train_y.append([0, 1, 0])
        else:
            train_y.append([0, 0, 1])

    return direction, button_direction, train_y

if __name__ == "__main__" :
    train_X, train_y = newTrainingData()
    print(train_X)
    print(np.array(train_X).shape)
    print(train_y)
    print(np.array(train_y).shape)