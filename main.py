import pygame 
import sys

pygame.init()

pygame.display.set_caption("")
window = pygame.display.set_mode((640, 480))

england = pygame.Rect(150, 50, 100, 110)
denmark = pygame.Rect(120, 150, 150, 100)
brazil = pygame.Rect(150, 250, 100, 100)
united_states = pygame.Rect(270, 150, 100, 100)

clock = pygame.time.Clock()

while True:
    window.fill((0, 30, 250))

    pygame.draw.rect(window, (200, 0, 0), england)
    pygame.draw.rect(window, (200, 0, 0), denmark)
    pygame.draw.rect(window, (200, 0, 0), brazil)
    pygame.draw.rect(window, (200, 0, 0), united_states)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)