import sys

import pygame

from scripts.tilemap import Tilemap
from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player
from scripts.clouds import Clouds

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()


        self.movement = [False, False]

        self.assets = {}
        asset_definitions = {
            "decor": ("tiles/decor", True),
            "grass": ("tiles/grass", True),
            "large_stone": ("tiles/large_decor", True),
            "stone": ("tiles/stone", True),
            "player": ("entities/player.png", False),
            "background": ("background.png", False),  # Background will be resized
            "clouds": ("clouds", True),
            "player/idle": Animation(load_images("entities/player/idle"), 6),
            "player/run": Animation(load_images("entities/player/run"), 4),
            "player/jump": Animation(load_images("entities/player/jump")),
            "player/slide": Animation(load_images("entities/player/slide")),
            "player/wall_slide": Animation(load_images("entities/player/wall_slide"))
        }

        for key, value in asset_definitions.items():
            if isinstance(value, tuple):
                path, is_folder = value
                if is_folder:
                    self.assets[key] = load_images(path)
                else:
                    # Handle background resize
                    if key == "background":
                        background_image = load_image(path)
                        screen_width, screen_height = self.screen.get_size()  # Get the screen dimensions
                        self.assets[key] = pygame.transform.scale(background_image,
                                                                  (320, 240))  # Resize
                    else:
                        self.assets[key] = load_image(path)
            else:
                self.assets[key] = value

        self.clouds = Clouds(self.assets["clouds"], count = 16)

        self.player = Player(self,(50,50),(8,15))

        self.tilemap = Tilemap(self,tile_size=16)

        self.scroll = [0, 0]
        
    def run(self):
        while True:
            self.display.blit(self.assets["background"],(0,0))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset = render_scroll)

            self.tilemap.render(self.display, offset = render_scroll)
            #update function
            self.player.update(self.tilemap,(self.movement[1] - self.movement[0],0))

            self.player.render(self.display, offset = render_scroll)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size())),
            pygame.display.update()
            self.clock.tick(60)

Game().run()