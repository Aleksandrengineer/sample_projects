from Game.Shared import GameObject
from Game.Shared import GameConstants

class Brick(GameObject):
    def __init__(self, position, sprite, game): #we also want to pass position, sprite and a reference to our game
        #reference if we inheret from brick to create a life brick or speed brick, we want to be able to interact with a game
        self.__game = game #private field for brick object
        self.__hitPoints = 100
        self.__lives = 1
        super(Brick, self).__init__(position, GameConstants.BRICK_SIZE, sprite)
    
    def getGame(self):
        return self.__game
    
    def isDestroyed(self): #is the brick it self is destroyed
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitPoints
    
    def hit(self): #decreasing the lives of the brick on hit
        self.__lives -= 1

    def gethitSound(self):
        return GameConstants.SOUND_HIT_BRICK

