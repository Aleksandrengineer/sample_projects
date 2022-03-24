from Game.Bricks import Brick
from Game.Shared import *

class LifeBrick(Brick):

    def __init__(self, position, sprite, game):
        super(LifeBrick, self).__init__(position, sprite, game)
        #we cann add here a new method "hit", which will override the previous method hit, so we can get lives in thee game

    def hit(self):
        game = self.getGame()
        game.increaseLives()

        super(LifeBrick, self).hit()

    def gethitSound(self):
        return GameConstants.SOUND_HIT_BRICK_LIFE