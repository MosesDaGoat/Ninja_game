import pygame, sys

from constants import *

from scripts.utils import load_image,load_images_from_folder
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("RPG")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "decor": load_images_from_folder("tiles/decor", size=(16, 16)),  # Assuming each tile is 16x16 pixels
            "grass": load_images_from_folder("tiles/grass", size=(25,25)),
            "large_decor": load_images_from_folder("tiles/large_decor", size=(16, 16)),
            "stone": load_images_from_folder("tiles/stone", size=(25, 25)),
            'player': load_image('assets/entities/player.png', size=(25, 50))
        }

        self.tile_map = Tilemap(self, tile_size=16)

        self.collision_area = pygame.Rect(50,50,300, 50)

        self.player = PhysicsEntity(self,'player',(500,500),(8,15))

    def run(self):
        while True:
            self.screen.fill(BLUE_GREEN)
            self.tile_map.render(self.screen)
            self.player.update((self.movement[1] - self.movement[0],0)*10)
            self.player.render(self.screen)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()