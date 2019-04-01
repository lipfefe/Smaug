import pygame
from pygame.locals import *

screemDimension = (510, 500)
screen = pygame.display.set_mode(screemDimension, 0, 32)
pygame.display.set_caption("Testando isometria")

x = 50
y = 40
height = 60
vel = 5

run = True



while True:
    pygame.time.delay(100)
    pygame.display.flip()



    pygame.draw.polygon(screen, (0, 200, 0), ((10, 250), (250, 110), (500, 250), (250, 390), (10, 250)), 0)
    pygame.draw.line(screen, (170, 150, 0), (9, 270), (250, 410), 42)
    pygame.draw.line(screen, (100, 80, 0), (250, 410), (499, 270), 42)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)








































