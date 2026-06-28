"""
To add
- spinny spin the circle
- label showing pi and r and n
- screenshot
- plot pi on iterations/time
"""

import random
import pygame
import time

WIDTH, HEIGHT = 800, 800
BORDER = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
running = True
bg = "#27187E"
good = "#F38375"
bad = "#717EC3"

screen.fill(bg)

r=0
n=0
start = time.time()

filled_set = set()

while running:
    a=random.random()
    b=random.random()
    rect = pygame.Rect(a*(WIDTH-2*BORDER)+BORDER, b*(HEIGHT-2*BORDER)+BORDER, 1, 1)
    if(a**2+b**2<=1):
        pygame.draw.rect(surface=screen, rect=rect, color=good)
        r+=1
        filled_set.add((int(a*(WIDTH-2*BORDER)+BORDER), int(b*(HEIGHT-2*BORDER)+BORDER)))
    else:
        pygame.draw.rect(surface=screen, rect=rect, color=bad)
    n+=1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.VIDEORESIZE:
            screen.fill(bg)
            WIDTH, HEIGHT = event.w, event.h

    if(n%1000==0):
        pygame.display.flip()
        elapsed = max(time.time() - start,0.0000001)
        total = (WIDTH-2*BORDER)*(HEIGHT-2*BORDER)
        print(f"{r*4/(n):.5f}|{n}|{r}|{elapsed:.2f}s|{n/elapsed:.2f}/s|{len(filled_set)}/{total}({len(filled_set)/total*100:.2f}% filled)")
    