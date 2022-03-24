import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import *

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)



    def render(self):
        super(PlayingGameScene, self).render() #calling super class and render method on that
        #then we need to addd balls and render them
        game = self.getGame() #retrieving the balls
        level = game.getLevel()
        balls = game.getBalls()

        if level.getAmountOfBricksLeft() <= 0:
            for ball in balls:
                ball.setMotion(0)

            level.loadNextLevel()

        #when there no lives i need to change scenes, but frist i am cheking about the lives number
        if game.getLives() <= 0:
            game.playSound(GameConstants.SOUND_GAMEOVER)
            game.changeScene(GameConstants.GAMEOVER_SCENE)

        pad = game.getPad() #get the pad
        #iteration of all the balls

        for ball in balls:
            for ball2 in balls:
                if ball != ball2 and ball.intersects(ball2):
                    ball.changeDirection(ball2)

            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and ball.intersects(brick): #check for intersection and destruction of the brick
                    game.playSound(brick.gethitSound())
                    brick.hit() #tell the brick it being hit
                    level.brickHit() #we need tell the level that we are hitting a brick
                    game.increaseScore(brick.getHitPoints()) #we ar eusing hitpoints as a number for score increase
                    ball.changeDirection(brick) #changing direction for ball after hiting brick
                    break
            if ball.intersects(pad):
                game.playSound(GameConstants.SOUND_HIT_PAD)
                ball.changeDirection(pad)

            #define the getballs method withing our game to retriev the collection of balls
            ball.updatePosition()

            if ball.isBallDead():
                ball.setMotion(0)
                game.reduceLives()

            #we need to render our ball by screen.blit method
            game.screen.blit(ball.getSprite(), ball.getPosition())
        # in other word in this loop we are updating position of the ball and retrieving it's sprite

        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed(): #if brick is destroyed we stop rendering it
                game.screen.blit(brick.getSprite(), brick.getPosition())

        #code to  render our pad and stick to the bottom of the screen

        pad.setPosition((pygame.mouse.get_pos()[0], pad.getPosition()[1]))
        game.screen.blit(pad.getSprite(), pad.getPosition())

        self.clearText()

        self.addText("Your Score: " + str(game.getScore()),
                     x = 0,
                     y = GameConstants.SCREEN_SIZE[1] - 60, size = 30)

        self.addText("Lives " + str(game.getLives()),
                     x = 0,
                     y = GameConstants.SCREEN_SIZE[1] - 30, size = 30)

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        #this event to exit the game
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            #this event for mouse click to launch the ball
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame().getBalls():
                    ball.setMotion(1)
#we have a playing game scene to start rendering things onto our screen
