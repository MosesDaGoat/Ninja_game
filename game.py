import sys

import pygame

from scripts.tilemap import Tilemap

from scripts.utils import load_image, load_images

from scripts.entities import PhysicsEntity


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()
        
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))
        
        self.img_pos = [160, 260]
        self.movement = [False, False]

        self.assets = {}
        asset_definitions = {
            "decor": ("tiles/decor", True),
            "grass": ("tiles/grass", True),
            "large_stone": ("tiles/large_decor", True),
            "stone": ("tiles/stone", True),
            "player": ("entities/player.png", False)
        }

        for key, (path, is_folder) in asset_definitions.items():
            if is_folder:
                self.assets[key] = load_images(path)
            else:
                self.assets[key] = load_image(path)



        self.player = PhysicsEntity(self,"player" ,(50,50),(8,15))

        self.tilemap = Tilemap(self,tile_size=16)
        
    def run(self):
        while True:
            self.display.fill((14, 219, 248))
            self.tilemap.render(self.display)
            #update function
            self.player.update(self.tilemap,(self.movement[1] - self.movement[0],0))

            self.player.render(self.display)


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

            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size())),
            pygame.display.update()
            self.clock.tick(60)

Game().run()