--[[
    GD50
    Match-3 Remake

    -- Tile Class --

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    The individual tiles that make up our game board. Each Tile can have a
    color and a variety, with the varietes adding extra points to the matches.
]]

Tile = Class{}

function Tile:init(x, y, color, variety, shiny)
    -- board positions
    self.gridX = x
    self.gridY = y

    -- coordinate positions
    self.x = (self.gridX - 1) * 32
    self.y = (self.gridY - 1) * 32

    -- tile appearance/points
    self.color = color
    self.variety = variety


    self.shiny = math.random()
    if self.shiny > 0.95 then
        self.shiny = true
    else
        self.shiny = false
    end

    if self.shiny then
        self.psystem = love.graphics.newParticleSystem(gTextures['particle'], 12)
        self.psystem:setEmitterLifetime(-1)
        self.psystem:setParticleLifetime(3, 5)
        self.psystem:setColors(1, 0.83, 0, 1, 1, 1, 1, 0)
        self.psystem:setAreaSpread('normal', 5, 5)
        self.psystem:setEmissionRate(5)
        self.psystem:start()
    end
end

function Tile:update(dt)
    if self.psystem then
        self.psystem:update(dt)
    end
end
--[[
    Function to swap this tile with another tile, tweening the two's positions.
]]
function Tile:swap(tile)
end

function Tile:render(x, y)

    -- draw shadow
    love.graphics.setColor(love.math.colorFromBytes(34, 32, 52, 255))
    love.graphics.draw(gTextures['main'], gFrames['tiles'][self.color][self.variety],
        self.x + x + 2, self.y + y + 2)

    --to render the shiny implementation
    if self.shiny == true then
        love.graphics.setColor(love.math.colorFromBytes(255,255,255,255))
        love.graphics.draw(gTextures['main'], gFrames['tiles'][self.color][self.variety],
        self.x + x, self.y + y)
    else
        -- draw tile itself
        love.graphics.setColor(love.math.colorFromBytes(255, 255, 255, 255))
        love.graphics.draw(gTextures['main'], gFrames['tiles'][self.color][self.variety],
        self.x + x, self.y + y)
    end

    --draw particles
    if self.psystem then
        love.graphics.draw(self.psystem, self.x + x + 16, self.y + y + 16)
    end
end

function Tile:destroy()
    if self.psystem then
        self.psystem:stop()
    end
end