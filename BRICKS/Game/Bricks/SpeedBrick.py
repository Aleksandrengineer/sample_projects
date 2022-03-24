from Game.Bricks import Brick
from Game.Shared import *

class SpeedBrick(Brick):

    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.getGame()
        #we going to increse the speed of all the balls
        for ball in game.getBalls():
            ball.setSpeed(ball.getSpeed() + 1) #supplying new speed for the ball

        super(SpeedBrick, self).hit()

    def gethitSound(self):
        return GameConstants.SOUND_HIT_BRICK_SPEED