import itertools
import sys
import pygame as pg

import queens

image = pg.image.load(r'queen.png')

def drawBoard(n, s, ls):
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
            if abs(ls[y//tile_size] - x/tile_size) < 1:
                pg.draw.circle(background, (200,0,0), (x+15,y+15), 10)
        if n % 2 == 0:
            next(colors)

    return background

def main(n, ls):
    r = len(ls)
    pg.init()

    size = width, height = 800, 600

    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    mover = -10

    game_exit = False
    while not game_exit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_exit = True

            if event.type == pg.MOUSEBUTTONDOWN:

                if event.button == 4:
                    if mover > 0:
                        mover -= 1

                if event.button == 5:
                    if mover < (height-120)-60:
                        mover += 1

        screen.fill((60, 70, 90))

        for i in range(r):
            font = pg.font.Font(None, 48)
            text = str(i+1)
            txt_surface = font.render(text, True, pg.Color('black'))
            screen.blit(txt_surface, (50, height-((550 - n*13) - i * (37.5 * n))-(mover*(r))))
            screen.blit(drawBoard(n, 30, ls[i]), (150, height-(550 - i * (37.5 * n))-(mover*(r))))


        pg.draw.rect(screen, (0,51,51), (width-30,10,25,height-20)) #SCROLL BAR
        pg.draw.rect(screen, (0,0,0), (width-29,mover+29,23,130)) #SCROLLING BAR


        pg.display.flip()
        clock.tick(300)

    pg.quit()

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        sys.exit(1)

    ls = queens.main(n)

    main(n, ls)
