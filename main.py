import pygame
import sys

PATH = "assets/images/"


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.cloud = pygame.image.load(f"{PATH}cloud_1.png")
        self.cloud.set_colorkey((0, 0, 0))
        self.cloud_pos = [160, 260]
        self.movement = [False, False]
        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.window.fill((0, 56, 129))
            self.cloud_pos[1] += self.movement[1] - self.movement[0]

            self.window.blit(self.cloud, self.cloud_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.run()

