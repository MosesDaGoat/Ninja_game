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

        self.movement = {"left": False, "right": False, "up": False, "down": False}

        self.assets = {
            "decor": load_images_from_folder("tiles/decor", size=(16, 16)),  # Assuming each tile is 16x16 pixels
            "grass": load_images_from_folder("tiles/grass", size=(25,25)),
            "large_decor": load_images_from_folder("tiles/large_decor", size=(16, 16)),
            "stone": load_images_from_folder("tiles/stone", size=(25, 25)),
            'player': load_image('assets/entities/player.png', size=(25, 50))
        }

        self.tile_map = Tilemap(self, tile_size=16)

        self.collision_area = pygame.Rect(50,50,300, 50)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15), speed=0.5, gravity=0.3,max_fall_speed=8)


    def run(self):
        while True:
            self.screen.fill(BLUE_GREEN)
            self.tile_map.render(self.screen)
            movement_x = (self.movement["right"] - self.movement["left"]) * 10
            movement_y = (self.movement["down"] - self.movement["up"]) * 10
            self.player.update(self.tile_map,(movement_x, movement_y))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement["left"] = True
                    if event.key == pygame.K_d:
                        self.movement["right"] = True
                    if event.key == pygame.K_w:
                        self.movement["up"] = True
                    if event.key == pygame.K_s:
                        self.movement["down"] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement["left"] = False
                    if event.key == pygame.K_d:
                        self.movement["right"] = False
                    if event.key == pygame.K_w:
                        self.movement["up"] = False
                    if event.key == pygame.K_s:
                        self.movement["down"] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()