import pygame

import pygame

NEIGHBOR_OFFSETS =[(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {"grass","stone"}


class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game  # Reference to the game object to access assets
        self.tile_size = tile_size
        self.tile_map = {}
        self.off_grid_tiles = []

        screen_width_in_tiles = self.game.screen.get_width() // self.tile_size
        # screen_height_in_tiles = self.game.screen.get_height() // self.tile_size

        # Calculate the starting positions for the grass row and stone column
        y_position = (self.game.screen.get_height() // self.tile_size) - 10 #

        # start_y = (screen_height_in_tiles - 10) // 2  # Center the stone column vertically

        for x in range(screen_width_in_tiles):
            self.tile_map[f"{x};{y_position}"] = {"type": "grass", "variant": "0", "pos": (x, y_position)}

        # for i in range(10):
        #     self.tile_map[f"{start_x + i};{start_y}"] = {"type": "grass", "variant": "1", "pos": (start_x + i, start_y)}
        #
        #     # Add a vertical column of stone tiles
        # for i in range(10):
        #     self.tile_map[f"{start_x};{start_y + i}"] = {"type": "stone", "variant": "0", "pos": (start_x, start_y + i)}

        # Example hardcoded tiles, you can modify this to fit your needs

    def tiles_around(self, pos):
        tiles=[]
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ";" + str(tile_loc[1] + offset[1])
            if check_loc in self.tile_map:
                tiles.append(self.tile_map[check_loc])
                return tiles

    def physics_rect_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile["type"] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile["pos"][0]*self.tile_size, tile["pos"][1] * self.tile_size, self.tile_size, self.tile_size))

    def render(self, surf):
        # Render off-grid tiles first
        for tile in self.off_grid_tiles:
            tile_type = tile["type"]
            tile_variant = tile["variant"]
            tile_pos = tile["pos"]
            tile_image = self.game.assets[tile_type].get(tile_variant)

            if tile_image:
                surf.blit(tile_image, tile_pos)

        # Render grid-aligned tiles
        for loc, tile in self.tile_map.items():
            tile_type = tile["type"]
            tile_variant = tile["variant"]
            tile_pos = tile["pos"]
            tile_image = self.game.assets[tile_type].get(tile_variant)

            if tile_image:
                pixel_pos = (tile_pos[0] * self.tile_size, tile_pos[1] * self.tile_size)
                surf.blit(tile_image, pixel_pos)