# imports
import pygame
from Figures import Figure
from Player import Player
import itertools
import pygame as pg
from pygame_functions import *



# sets up the screen
screenSize(500,600)
#setBackgroundImage("images/cut_wood.png")
drawRect(0,0,500,50,"dark grey")
titleLabel = makeLabel("Chess Champions", 30, 10, 10, "brown", "Cooper Black","dark grey")
showLabel(titleLabel)
drawRect(0,550,500,50,"dark grey")
playerLabel = makeLabel("Spieler 1 (Weiß) ist dran!", 20, 10, 563, "white", "Cooper Black","dark grey")
showLabel(playerLabel)

# draws the chessboard
colors = itertools.cycle(("grey","brown"))
tile_size = 50
for row in range(8):
    for column in range(8):
        drawRect(50+tile_size*column,100+tile_size*row,tile_size,tile_size,next(colors))
    next(colors)
drawRect(50,100,8*tile_size,8*tile_size,"black",5)

# create objects
cb = Figure.chessboard
pWhite = Player("white")
pBlack = Player("black")

# sprite test
class Box(pygame.sprite.Sprite):
    def __init__(self, color, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.speed = 300
    def update(self, time_passed):
        moved_distance = time_passed * self.speed
        self.rect.left += moved_distance

box = Box((255,0,0),(50,50))

# pawn sprite
pawnSprite = makeSprite("images/pawn-icon-50.png")
moveSprite(pawnSprite,50,50)
#showSprite(pawnSprite)

# necessary at the end
endWait()
