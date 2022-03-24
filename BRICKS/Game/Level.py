import os
import fileinput
import pygame
import random

from Game.Bricks import *
from Game.Shared.GameConstants import GameConstants

class Level:

    def __init__(self, game): #we need a game reference to pass the game down to the bricks
        self.__game = game
        self.__bricks = []
        self.__amountOfBricksLeft = 0
        self.__currentLevel = 0

    def getBricks(self):
        return self.__bricks

    def getAmountOfBricksLeft(self):
        return self.__amountOfBricksLeft
    
    def brickHit(self): #method to record that brick is hit
        self.__amountOfBricksLeft -= 1
    
    def loadNextLevel(self):
        self.__currentLevel +=1
        fileName = os.path.join("Assets", "Levels", "level" + str(self.__currentLevel) + ".dat")

        if not os.path.exists(fileName):
            self.loadRandom()

        else:
            self.load(self.__currentLevel)


    def loadRandom(self):
        self.__bricks = []

        x, y = 0, 0

        maxBricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0]) #max brick connected to the screen_size
        rows = random.randint(2, 8) #randomizing the number of row

        amountOfSuperPowerBricks = 0
        for row in range(0, rows):
            for brick in range (0, maxBricks):
                brickType = random.randint(0, 3) #randomizing the bricktype
                if brickType == 1 or amountOfSuperPowerBricks >= 5: #amountofsuperpower brick is the amount of brick in randomly generated level
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif brickType == 2:
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks +=1

                elif brickType == 3:
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks +=1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]


    def load(self, level):
        self.__currentLevel = level
        self.__bricks = []

        x, y = 0, 0

        for line in fileinput.input(os.path.join("Assets", "Levels", "level" + str(level) + ".dat")):
            for currentBrick in line:
                if currentBrick == "1":
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "2":
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "3":
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

# we want to increase exposition for the next brick we are going to add
#so in each brick in our current size we want to increase X by the brick width
# we can found size of the brick in gameconstants

                x += GameConstants.BRICK_SIZE[0]

#when we reached the end of line we want to reset the x position and
#add the Y position with the higth of our brick

            x = 0
            y += GameConstants.BRICK_SIZE[1]