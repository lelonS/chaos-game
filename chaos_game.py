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
    return (int((p1[0] + p2[0]) * m), int((p1[1] + p2[1]) * m))


def reset_screen():
    SCREEN.fill(BACKGROUND)
    # SCREEN.blit(bg, (0, 0))
    draw_points(points)


# CONSTANTS
WIDTH = 900
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
    while added_points < amount_per_frame:
        tries += 1
        if tries > MAX_LOOP:
            break
        random_point = random.choice(points)
        if (random_point != prev_point or allow_repeat_point) and SCREEN.get_at(get_new_point(current_point, random_point, mult)) != (255, 255, 255, 255):
            prev_point = random_point
            current_point = get_new_point(current_point, random_point, mult)
            # pygame.draw.rect(SCREEN, (255, 0, 0),
            #                  (current_point[0], current_point[1], 1, 1))
            SCREEN.set_at(current_point, (255, 0, 0))
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
            points = get_points(amount_points, (WIDTH/2, HEIGHT/2))
            reset_screen()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            allow_repeat_point = not allow_repeat_point
            reset_screen()

    pygame.display.update()
# QUIT
pygame.quit()
