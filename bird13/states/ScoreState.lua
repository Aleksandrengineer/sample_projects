--[[
    ScoreState Class
    Author: Colton Ogden
    cogden@cs50.harvard.edu

    A simple state used to display the player's score before they
    transition back into the play state. Transitioned to from the
    PlayState when they collide with a Pipe.
]]

ScoreState = Class{__includes = BaseState}

--Images for the medals
local BRONZE_IMAGE = love.graphics.newImage('bronze.png')
local SILVER_IMAGE = love.graphics.newImage('silver.png')
local GOLD_IMAGE = love.graphics.newImage('gold.png')

--[[
    When we enter the score state, we expect to receive the score
    from the play state so we know what to render to the State.
]]
function ScoreState:enter(params)
    self.score = params.score
end

function ScoreState:update(dt)
    -- go back to play if enter is pressed
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        gStateMachine:change('countdown')
    end
end

function ScoreState:render()
    -- simply render the score to the middle of the screen
    love.graphics.setFont(flappyFont)
    love.graphics.printf('Oof! You lost!', 0, 64, VIRTUAL_WIDTH, 'center')

    love.graphics.setFont(mediumFont)
    love.graphics.printf('Score: ' .. tostring(self.score), 0, 100, VIRTUAL_WIDTH, 'center')

    love.graphics.printf('Press Enter to Play Again!', 0, 120, VIRTUAL_WIDTH, 'center')

    -- this code is checking the score and what medal image is to render on the score screen
    if self.score <= 1 then
        love.graphics.draw(BRONZE_IMAGE, 256-51, 140)
    elseif self.score <=2 then
        love.graphics.draw(SILVER_IMAGE, 256-51, 140)
    elseif self.score >=3 then
        love.graphics.draw(GOLD_IMAGE, 256-75, 140)
    end

end