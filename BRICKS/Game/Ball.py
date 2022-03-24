import pygame
from Game.Shared import *

class Ball (GameObject): #our ball have new parametres:
    #speed, how much it moves multiplied by position, direcction for both X and Y in which ball moves, parameter is ball moving or not.
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 3
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__inMotion = 0
        super(Ball, self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def setSpeed(self, newSpeed): #set the speed of our ball
        self.__speed = newSpeed

    def resetSpeed(self): #reseting the speed
        self.setSpeed(3)
    
    def getSpeed(self): #retrieve the speed
        return self.__speed

    def isInMotion(self): #is be able to know is ball moving or not
        return self.__inMotion

    def setMotion(self, isMoving): #reset the speed when we change the motion. SO it would be reset when we restart the game
        self.__inMotion = isMoving
        self.resetSpeed()

    def changeDirection(self, gameObject): #method to change direction of ball
        #it should be used when we hit brick or borders
        #reference to tha game object that it collided with

        position = self.getPosition()#we get position of our ball
        size = self.getSize() #get the size of our ball
        objectPosition = gameObject.getPosition() #same for the other object
        objectSize = gameObject.getSize() #same for the other object

        if position[1] > objectPosition[1] and \
                position[1] < objectPosition[1] + objectSize[1] and \
                position[0] > objectPosition[0] and \
                position[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((position[0], objectPosition[1] + objectSize[1]))
            #we using setposition to set position of
            # the ball based on where it hit the object
            self.__direction[1] *= -1 #inverting the direction of y

        elif position[1] + size[1] > objectPosition[1] and \
                position[1] + size[1] < objectPosition[1] + objectSize[1] and \
                position[0] > objectPosition[0] and \
                position[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((position[0], objectPosition[1] - objectSize[1]))
            self.__direction[1] *= -1 #inverting Y too

        elif position[0] + size[0] > objectPosition[0] and \
                position[0] + size[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((objectPosition[0] - size[0], position[1]))
            self.__direction[0] *= -1 #inverting the X

        else:
            self.setPosition((objectPosition[0] + objectSize[0], position[1]))
            self.__direction[0] *= -1 #inverting both of x and y
            self.__direction[1] *= -1 #inverting both of x and y

    def updatePosition(self): #method for udating the position
        #this method we keep track of ball and make sure that ball doesn't go outside of border application
        #self.setPosition(pygame.mouse.get_pos()) #mouse follow the ball to check prealpha

        #this is to stop ball moving at the begining and position it at centre of the pad, well in theory
        if not self.isInMotion():
            padPosition = self.__game.getPad().getPosition()
            self.setPosition((
                padPosition[0] + (GameConstants.PAD_SIZE[0]/2),
                GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1] - GameConstants.BALL_SIZE[1]
            ))
            return

        #taking the ball and is size
        position = self.getPosition()
        size = self.getSize()
        #changing ball psoition taking in consideration speed of the bball
        newPosition = [position[0] + (self.__increment[0] * self.__speed) * self.__direction[0],
                       position[1] + (self.__increment[1] * self.__speed) * self.__direction[1]]
        #if sttement tot check if in bounds of our app, and if not change the ball riection
        if newPosition[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:
            self.__direction[0] *= -1
            newPosition = [GameConstants.SCREEN_SIZE[0] - size[0], newPosition[1]]
            self.__game.playSound(GameConstants.SOUND_HIT_WALL)

        if newPosition[0] <= 0:
            self.__direction[0] *= -1
            newPosition = [0, newPosition[1]]
            self.__game.playSound(GameConstants.SOUND_HIT_WALL)

        if newPosition[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            self.__direction[1] *= -1
            newPosition = [newPosition[0], GameConstants.SCREEN_SIZE[1] - size[1]]

        if newPosition[1] <= 0:
            self.__direction[1] *= -1
            newPosition = [newPosition[0], 0]
            self.__game.playSound(GameConstants.SOUND_HIT_WALL)

        self.setPosition(newPosition)

    def isBallDead(self): #method to check if the ball is dead or not
        #it should check it whenever the ball approaches the bottom border
        position = self.getPosition()
        size = self.getSize()

        if position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            return 1

        return 0


