import pygame
import sys
from pygame.locals import *

pygame.init() # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((626,601))

bg = pygame.image.load("\Background.png")
topostrich= pygame.image.load("\frame_00_delay-0.04s.gif")


pygame.mouse.set_visible(1)

pygame.display.set_caption('Race Game')

# fix indentation

while True:
    clock.tick(60)
    screen.blit(bg, (0,0))
    x,y = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
