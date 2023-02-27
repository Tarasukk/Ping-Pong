import pygame as pg
import random
pg.init()
pg.font.init()

TITLE = "Half Pong"
WIDTH = 800
HEIGHT = 480


FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 15
PLATFORM_SPEED = 10
platform_rect = pg.rect.Rect(
    WIDTH / 2 - PLATFORM_WIDTH / 2,
    HEIGHT - PLATFORM_HEIGHT * 2,
    PLATFORM_WIDTH,
    PLATFORM_HEIGHT,
)

CIRCLE_RADIUS = 15
CIRCLE_SPEED = 10
circle_first_collide = False
circle_x_speed = 0
circle_y_speed = CIRCLE_SPEED


circle_rect = pg.rect.Rect(
    WIDTH / 2 - CIRCLE_RADIUS,
    HEIGHT / 2 - CIRCLE_RADIUS,
    CIRCLE_RADIUS * 2,
    CIRCLE_RADIUS * 2,
)

screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption(TITLE)

running = True
game_over = False
clock = pg.time.Clock()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            continue
        elif event.type == pg.KEYDOWN:
            if event.type == pg.K_ESCAPE:
                running = False
                continue

    screen.fill(BLACK)

    if not game_over:
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            platform_rect.x -= PLATFORM_SPEED
        elif keys[pg.K_d]:
            platform_rect.x += PLATFORM_SPEED

        if platform_rect.colliderect(circle_rect):
            if not circle_first_collide:
                # з відси пиши
        pg.draw.rect(screen, WHITE, platform_rect)

    circle_rect.x += circle_x_speed
    circle_rect.y += circle_y_speed

    if circle_rect.bottom >= HEIGHT:
        game_over = True
        circle_y_speed = -CIRCLE_SPEED
    elif circle_rect.top <= 0:
        circle_y_speed = CIRCLE_SPEED
    elif circle_rect.left <= 0:
        circle_x_speed = CIRCLE_SPEED
    elif circle_rect.right >= WIDTH:
        circle_x_speed = CIRCLE_SPEED


    pg.draw.circle(screen, WHITE, circle_rect.center, CIRCLE_RADIUS)

    clock.tick(FPS)

    pg.display.flip()
pg.quit()
