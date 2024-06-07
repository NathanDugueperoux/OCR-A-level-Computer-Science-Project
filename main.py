import pygame
import sys
#
# PATH = "assets/images/"
#
#
# class Game:
#     def __init__(self):
#         pygame.init()
#         self.window = pygame.display.set_mode((640, 480))
#         self.clock = pygame.time.Clock()
#         self.cloud = pygame.image.load(f"{PATH}cloud_1.png")
#
#     def run(self):
#         while True:
#             self.window.blit(self.cloud, (200, 200))
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         print("hello")
#             self.clock.tick(60)
#
#
# game = Game()
# game.run()

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
cloud = pygame.image.load("assets/images/cloud_1.png")

while True:
    window.blit(cloud, (100, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)