--[[
    GD50
    Breakout Remake

    -- Paddle Class --

    Author: Me
    aspiridonov971@gmail.com

    Represents a powerup class. Can spawn when a brick is destroyed.
    Used for storing different powerups and their effect?
    When spawn moving only down till the ground and cann't go any further
    then the ground.
    The power up can have a skin that represent its special property.
]]

KEY_POWER = 10
BALL_POWER = 7


PowerUp = Class{}

function PowerUp:init(x, y, power) -- x and y denote the starting position of the powerup, type denotes which powerup is spawned
    --dimensional variables
    self.width = 16
    self.height = 16

    self.x = x
    self.y = y

    --velocity of falling
    self.dy = 30

    --powerup type
    self.power = power

    --flashing effect
    self.timer = 0
    self.withAlpha = true
end

function PowerUp:collides(target)
    -- first, check to see if the left edge of either is farther to the right
    -- than the right edge of the other
    if self.x > target.x + target.width or target.x > self.x + self.width then
        return false
    end

    -- then check to see if the bottom edge of either is higher than the top
    -- edge of the other
    if self.y > target.y + target.height or target.y > self.y + self.height then
        return false
    end 

    -- if the above aren't true, they're overlapping
    return true
end

function PowerUp:update(dt)
    self.y = self.y +self.dy * dt

    self.timer = self.timer + dt
    if (self.timer > 0.5) then
        self.timer = 0
        self.withAlpha = not self.withAlpha
    end
end

function PowerUp:render()  
    if (self.withAlpha) then
        love.graphics.setColor(love.math.colorFromBytes(255, 255, 100))
    end
    love.graphics.draw(gTextures['main'], gFrames['powerups'][self.power], self.x, self.y)
    love.graphics.setColor(love.math.colorFromBytes(255, 255, 255))
end
