from ast import Break
from tkinter.tix import MAX
import pygame
import random
from math import cos, sin, pi

pygame.init()


def draw_points(points, r=5, color=(255, 0, 255)):
    global SCREEN
    pygame.draw.circle(SCREEN, (255, 255, 0), (0, 0), r)
    for p in points:
        pygame.draw.circle(SCREEN, color, p, r)


def get_points(amount, center):
    global RADIUS
    points = []
    for i in range(amount):
        x = cos(i/amount*2*pi - pi/2)*RADIUS + center[0]
        y = sin(i/amount*2*pi - pi / 2)*RADIUS + center[1]
        points.append((int(x), int(y)))
    return points


def get_new_point(p1, p2, m):
    x_dif = p2[0] - p1[0]
    y_dif = p2[1] - p1[1]
    x_mult = p1[0] + x_dif * m
    y_mult = p1[1] + y_dif * m
    return (int(x_mult), int(y_mult))

def draw_text(t, pos, color=(255,255,255)):
    global SCREEN
    myFont = pygame.font.Font(None, 20)
    text = str(t)
    renderFont = myFont.render(text, 1, color)
    SCREEN.blit(renderFont, pos)

def reset_screen():
    global SCREEN
    global allow_repeat_point
    global mult
    global step
    SCREEN.fill(BACKGROUND)
    # SCREEN.blit(bg, (0, 0))
    draw_points(points)
    draw_text("allow_repeat_point=" + str(allow_repeat_point), (0, 20))
    draw_text("mult=" + str(mult), (0, 40))
    draw_text("step=" + str(step), (0, 60))

def add_point():
    global SCREEN
    global MAX_LOOP
    global points
    global prev_point
    global allow_repeat_point
    global current_point
    global mult
    tries = 0
    while tries < MAX_LOOP:
        random_point = random.choice(points)
        if (random_point != prev_point or allow_repeat_point):# and SCREEN.get_at(get_new_point(current_point, random_point, mult)) != (255, 255, 255, 255):
            prev_point = random_point
            current_point = get_new_point(current_point, random_point, mult)
            # pygame.draw.rect(SCREEN, (255, 0, 0),
            #                  (current_point[0], current_point[1], 1, 1))
            SCREEN.set_at(current_point, (255, 0, 0))
            return
    print("error")
        

# CONSTANTS
WIDTH = 800
HEIGHT = WIDTH

RADIUS = WIDTH / 2 if WIDTH <= HEIGHT else HEIGHT / 2
RADIUS = RADIUS - 10

MAX_LOOP = 1000

BACKGROUND = (0, 0, 0)
# bg = pygame.image.load("img/test.png")


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()

# Variables
amount_points = 3
step = False
allow_repeat_point = True
amount_per_frame = 200
mult = 0.5

points = get_points(amount_points, (WIDTH/2, HEIGHT/2))
current_point = random.choice(points)
prev_point = current_point


running = True

reset_screen()
while running:

    added_points = 0
    tries = 0
    while added_points < amount_per_frame and not step:
        tries += 1
        if tries > MAX_LOOP:
            break
        add_point()
        added_points += 1

    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            amount_points += 1
            points = get_points(amount_points, (WIDTH/2, HEIGHT/2))
            reset_screen()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            amount_points -= 1
            if amount_points <= 0: amount_points = 1
            points = get_points(amount_points, (WIDTH/2, HEIGHT/2))
            reset_screen()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            allow_repeat_point = not allow_repeat_point
            reset_screen()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            mult += 0.02
            reset_screen()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            mult -= 0.02
            reset_screen()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            step = not step
            reset_screen()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and step:
            for i in range(amount_per_frame):
                add_point()


    pygame.display.update()
# QUIT
pygame.quit()
