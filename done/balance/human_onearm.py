import pygame
import math

# pygame init

pygame.init()
pygame.font.init()

# constants

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
bg = "#27187E"
primary = "#F38375"
secondary = "#717EC3"

# variables

running = True
x = 400
x_dot = 0
y = 1
y_dot = 0
theta = 0
theta_dot = 0

def get_acceleration(theta):
    return 

def get_theta_double_dot(theta, y_dot):
    return math.sin(theta)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg)

    # Display
    pressed = pygame.mouse.get_pressed()
    if any(pressed):
        mouse_pos = pygame.mouse.get_pos()
        delta_x = mouse_pos[0] - x
        x = mouse_pos[0]
        x_dot = x_dot # idk

    arm = pygame.rect.Rect(x-10, 200-100*y, 20, 100)

    pygame.draw.rect(surface=screen, color=primary, rect=arm)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()