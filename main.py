import pygame as pg

pg.init()
pg.font.init()

TITLE = 'Half Pong'
WIDTH = 800
HEIGHT = 480

PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 15
platform_rect = pg.rect.Rect(WIDTH / 2 - PLATFORM_WIDTH / 2,
                            HEIGHT - PLATFORM_HEIGHT * 2,
                             PLATFORM_WIDTH,
                             PLATFORM_HEIGHT)

screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption(TITLE)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            continue
        elif event.type == pg.KEYDOWN:
            if event.type == pg.K_ESCAPE:
              running = False
              continue

pg.quit()