import numpy as np
import math
import random
from settings import Settings

settings = Settings()
screen_width, screen_height = settings.screen_width, settings.screen_height

def startingPositions():
    snakeHead = [100, 100]
    snakePositions = [[100, 100], [100-settings.rows, 100], [100-2*settings.rows, 100],]
    applePosX = random.randint(1,settings.rows-2)*settings.sizeBtwn
    applePosY = random.randint(1,settings.rows-2)*settings.sizeBtwn
    applePosition = [applePosX, applePosY]
    score = 2
    return snakeHead, snakePositions, applePosition, score

def angleSnakeApple(snakePositions, applePosition):
    appleDV = np.array(applePosition) - np.array(snakePositions[0])
    snakeDV = np.array(snakePositions[0]) - np.array(snakePositions[1])

    norm_of_appleDV = np.linalg.norm(appleDV)
    norm_of_snakeDV = np.linalg.norm(snakeDV)
    if norm_of_appleDV == 0:
        norm_of_appleDV = settings.sizeBtwn
    if norm_of_snakeDV == 0:
        norm_of_snakeDV = settings.sizeBtwn

    appleDV_normalized = appleDV / norm_of_appleDV
    snakeDV_normalized = snakeDV / norm_of_snakeDV
    angle = math.atan2(
        appleDV_normalized[1] * snakeDV_normalized[0] - appleDV_normalized[0] * snakeDV_normalized[1],
        appleDV_normalized[1] * snakeDV_normalized[1] + appleDV_normalized[0] * snakeDV_normalized[0]) / math.pi
    return angle, appleDV_normalized, snakeDV_normalized

def nextDirection(snakePositions, angleSnakeApple):
    direction = 0
    if angleSnakeApple > 0:
        direction = 1
    elif angleSnakeApple < 0:
        direction = -1

    return directionVector(snakePositions, angleSnakeApple, direction)

def directionVector(snakePositions, angleSnakeApple, direction):
    currentDV = np.array(snakePositions[0]) - np.array(snakePositions[1]) # [25,0]
    leftDV = np.array([currentDV[1], -currentDV[0]]) # [0, -25]
    rightDV = np.array([-currentDV[1], currentDV[0]]) # [0, 25]

    new_direction = currentDV
    if direction == -1:
        new_direction = leftDV
    if direction == 1:
        new_direction = rightDV
    button_direction = buttonDirection(new_direction)
    return direction, button_direction

def buttonDirection(new_direction):
    button_direction = 0
    if new_direction.tolist() == [settings.sizeBtwn, 0]: 
        button_direction = 1 #RIGHT
    elif new_direction.tolist() == [-settings.sizeBtwn, 0]:
        button_direction = 0 #LEFT
    elif new_direction.tolist() == [0, settings.sizeBtwn]:
        button_direction = 2 #DOWN
    elif new_direction.tolist() == [0, -settings.sizeBtwn]:
        button_direction = 3 #UP
    return button_direction

def blockedDirections(snakePositions):
    currentDV = np.array(snakePositions[0]) - np.array(snakePositions[1])

    leftDV = np.array([currentDV[1], -currentDV[0]])
    rightDV = np.array([-currentDV[1], currentDV[0]])

    isFrontBlocked = isBlocked(snakePositions, currentDV)
    isLeftBlocked = isBlocked(snakePositions, leftDV)
    isRightBlocked = isBlocked(snakePositions, rightDV)

    return currentDV, isFrontBlocked, isLeftBlocked, isRightBlocked

def isBlocked(snakePositions, directionVector):
    newHead = snakePositions[0] + directionVector
    if collidedWithSelf(newHead.tolist(), snakePositions) or collidedWithWall(newHead): return 1
    else: return 0

def collidedWithWall(newHead):
    x, y = newHead[0], newHead[1]
    if (x >= screen_width or x < 0 or y >= screen_height or y < 0): return True
    else: return False


def collidedWithSelf(newHead, snakePositions):
    if newHead in snakePositions[1:]: return True
    else: return False

def blockedDirectionsTrain(snakePositions, applePosition):
    currentDV = np.array(snakePositions[0]) - np.array(snakePositions[1])

    leftDV = np.array([currentDV[1], -currentDV[0]])
    rightDV = np.array([-currentDV[1], currentDV[0]])

    isFrontBlocked = isBlockedTrain(snakePositions, currentDV, applePosition)
    isLeftBlocked = isBlockedTrain(snakePositions, leftDV, applePosition)
    isRightBlocked = isBlockedTrain(snakePositions, rightDV, applePosition)

    return currentDV, isFrontBlocked, isLeftBlocked, isRightBlocked

def isBlockedTrain(snakePositions, directionVector, applePosition):
    newHead = snakePositions[0] + directionVector
    if wouldCollidedWithSelf(snakePositions, directionVector, applePosition) or collidedWithWall(newHead): return 1
    else: return 0
    
def wouldCollidedWithSelf(snakePositions, directionVector, applePosition):
    steps = (snakePositions[0][0] - 0) // settings.sizeBtwn
    if directionVector[0] == 0: steps = (screen_height - snakePositions[0][1]) // settings.sizeBtwn
    for i in range(1,steps+1):    
        newHead = snakePositions[0] + directionVector*i
        if newHead.tolist() == applePosition and applePosition not in snakePositions[1:]: return False
        if newHead.tolist() in snakePositions[1:]: return True
    return False