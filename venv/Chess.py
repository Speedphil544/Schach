import pygame
from Figures import Figure
from Player import Player
import itertools
import pygame as pg
#ahah

pg.init()
pg.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))


BROWN = pg.Color(130,70,30)
WHITE = pg.Color('white')

screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

colors = itertools.cycle((WHITE, BROWN))
tile_size = 60
width, height = 8*tile_size, 8*tile_size
background = pg.Surface((width, height))

for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        rect = (x, y, tile_size, tile_size)
        pg.draw.rect(background, next(colors), rect)
    next(colors)

game_exit = False
while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True

    screen.fill((180, 130, 20))
    screen.blit(background, (0, 100))
    screen.blit(textsurface, (0, 0))
    pg.display.flip()
    clock.tick(30)

pg.quit()


cb = Figure.chessboard
pWhite = Player("white")
pBlack = Player("black")


