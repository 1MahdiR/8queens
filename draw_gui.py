import itertools
import pygame as pg


pg.init()

size = width, height = 800, 600

screen = pg.display.set_mode(size)
clock = pg.time.Clock()

def drawBoard(n, s):
    BLACK = pg.Color('black')
    WHITE = pg.Color('white')


    colors = itertools.cycle((WHITE, BLACK))
    tile_size = s
    width, height = n*tile_size, n*tile_size
    background = pg.Surface((width, height))

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            rect = (x, y, tile_size, tile_size)
            pg.draw.rect(background, next(colors), rect)
        next(colors)

    return background

mover = -10

game_exit = False
while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True

        if event.type == pg.MOUSEBUTTONDOWN:

            if event.button == 4:
                if mover > 0:
                    mover -= 15

            if event.button == 5:
                if mover < (height-120)-60:
                    mover += 15

    screen.fill((60, 70, 90))
    
    for i in range(3):
        screen.blit(drawBoard(8, 30), (100, height-(550 - i * 300)-mover))

    pg.draw.rect(screen, (0,51,51), (width-30,10,25,height-20)) #SCROLL BAR

    pg.draw.rect(screen, (0,0,0), (width-29,mover+29,23,130)) #SCROLLING BAR


    pg.display.flip()
    clock.tick(300)

pg.quit()
