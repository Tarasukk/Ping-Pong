import pygame
import pygame as pg
import random
from Textures import Player, Player2
pg.init()
pg.font.init()
pg.mixer.init()
music = pygame.mixer.music.load('res\BackgroundMusic.wav')
hit=pg.mixer.Sound('res\Ball-hit.wav')
gameover=pg.mixer.Sound('res\GameOver.wav')
pg.mixer.music.play(-1)
restart="Press R for restart"
TITLE = "Ping Pong"
i=0
WIDTH = 800
HEIGHT = 480
score=0
FPS = 60
ARIAL_FONT_PATH = pg.font.match_font('arial')
ARIAL_FONT_48= pg.font.Font(ARIAL_FONT_PATH, 48)
ARIAL_FONT_36= pg.font.Font(ARIAL_FONT_PATH, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 15
PLATFORM_SPEED = 10
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption(TITLE)
platform=pg.image.load("res\Sky.jpg").convert_alpha()
plt=platform.get_rect()
player = Player()
player2 = Player2()
#Texture Logic
screen.fill(BLACK)
screen.blit(platform, plt)
#Base attributes
def render(screen, player):
    # pygame.draw.rect(screen, (255, 255, 255), (0 + player.x, 0 + player.y, 50, 50))
    player.render(player.x, player.y, screen)
def render2(screen, player2):
    player2.render(player2.x, player.y, screen)
def update(player):
    player.update()
def update2(player2):
    player2.update()

platform_rect = pg.rect.Rect(
    WIDTH / 2 - PLATFORM_WIDTH / 2,
    HEIGHT - PLATFORM_HEIGHT * 2,
    PLATFORM_WIDTH,
    PLATFORM_HEIGHT,
)
platform_rect2 = pg.rect.Rect(
    WIDTH / 2 - PLATFORM_WIDTH/2 ,
    PLATFORM_HEIGHT ,
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
            elif event.key==pg.K_r:
                player.x = 350
                player.y = 450
                player2.x=350
                player2.y=15
                game_over= False
                platform_rect.centerx=WIDTH/2
                platform_rect.bottom=HEIGHT - PLATFORM_HEIGHT
                platform_rect2.centerx = WIDTH / 2
                platform_rect2.bottom = 30
                circle_rect.center= [WIDTH/2, HEIGHT/2]
                circle_x_speed = 0
                circle_y_speed = CIRCLE_SPEED
                circle_first_collide=False
                score=0
                i=0
    screen.fill(BLACK)
    screen.blit(platform, plt)
    if event.type == pygame.KEYDOWN:
        player.key_down(event.key)
    if event.type == pygame.KEYUP:
        player.key_up(event.key)

    if not game_over:
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            platform_rect.x -= PLATFORM_SPEED
        elif keys[pg.K_d]:
            platform_rect.x += PLATFORM_SPEED
        if keys[pg.K_LEFT]:
            platform_rect2.x -= PLATFORM_SPEED
        elif keys[pg.K_RIGHT]:
            platform_rect2.x += PLATFORM_SPEED
        if keys[pg.K_a]:
            player.x-=PLATFORM_SPEED
        elif keys[pg.K_d]:
            player.x += PLATFORM_SPEED
        if keys[pg.K_LEFT]:
            player2.x -= PLATFORM_SPEED
        elif keys[pg.K_RIGHT]:
            player2.x += PLATFORM_SPEED

        if platform_rect.colliderect(circle_rect):
            if not circle_first_collide:
                if random.randint(0, 1) == 0:
                    circle_x_speed = (CIRCLE_SPEED/(random.uniform(1, 2)))
                else:
                    circle_x_speed = -(CIRCLE_SPEED/(random.randint(1, 2)))
                circle_first_collide = True
            circle_y_speed = -CIRCLE_SPEED
            pg.mixer.Sound.play(hit)
            score += 1
        pg.draw.rect(screen, WHITE, platform_rect)

        if platform_rect2.colliderect(circle_rect):
            if circle_first_collide:
                if random.randint(0, 1) == 0:
                    circle_x_speed = (CIRCLE_SPEED/(random.uniform(1, 2)))
                else:
                    circle_x_speed = -(CIRCLE_SPEED/(random.uniform(1, 2)))
                circle_first_collide = False
            circle_y_speed = CIRCLE_SPEED
            pg.mixer.Sound.play(hit)
            score += 1
        pg.draw.rect(screen, WHITE, platform_rect2)
        update(player)
        render(screen, player)
        update2(player2)
        render2(screen, player2)

    circle_rect.x += circle_x_speed
    circle_rect.y += circle_y_speed

    if circle_rect.bottom >= HEIGHT:
        game_over = True
        circle_y_speed = -CIRCLE_SPEED
    elif circle_rect.top <= 0:
        game_over = True
        circle_y_speed = CIRCLE_SPEED
    elif circle_rect.left <= 0:
        circle_x_speed = CIRCLE_SPEED
    elif circle_rect.right >= WIDTH:
        circle_x_speed = -CIRCLE_SPEED
    update(player)

    pg.draw.circle(screen, WHITE, circle_rect.center, CIRCLE_RADIUS)
    if not game_over:
        score_surface = ARIAL_FONT_48.render(str(score), True, WHITE)
        # screen.blit(score_surface, [WIDTH / 2 - score_surface.get_width() / 2,
        #                             15])
    else:
        player.x = 350
        player.y = 450
        retry_surface = ARIAL_FONT_36.render(restart,  True, WHITE)
        # screen.blit(score_surface, [WIDTH / 2 - score_surface.get_width() / 2,
        #                             HEIGHT/3])
        # screen.blit(retry_surface, [WIDTH / 2 - score_surface.get_width() / 2,
        #                             HEIGHT / 3+ score_surface.get_height()])
        screen.blit(retry_surface,[280, 240])
        pg.mixer.Sound.play(gameover)
    clock.tick(FPS)

    pg.display.flip()
pg.quit()