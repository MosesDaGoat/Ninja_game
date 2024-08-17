class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game  # Reference to the game object to access assets
        self.tile_size = tile_size
        self.tile_map = {"1;1": {"type": "decor", "variant": "0", "pos": (1, 1)},
                         "2;1": {"type": "decor", "variant": "1", "pos": (2, 1)},
                         "3;1": {"type": "decor", "variant": "2", "pos": (3, 1)},
                         "4;1": {"type": "decor", "variant": "3", "pos": (4, 1)}}
        self.off_grid_tiles = []

        # Example hardcoded tiles, you can modify this to fit your needs

    def render(self, surf):
        for loc, tile in self.tile_map.items():
            tile_type = tile["type"]
            tile_variant = tile["variant"]
            tile_pos = tile["pos"]
            tile_image = self.game.assets[tile_type].get(tile_variant)  # Fetch the tile variant image

            if tile_image:
                pixel_pos = (tile_pos[0] * self.tile_size, tile_pos[1] * self.tile_size)
                surf.blit(tile_image, pixel_pos)

            for tilez in self.off_grid_tiles:
                tile_type = tile["type"]
                tile_variant = tile["variant"]
                tile_pos = tile["pos"]
                tile_image = self.game.assets[tile_type].get(tile_variant)

                if tile_image:
                    # Directly use the provided pixel position
                    surf.blit(tile_image, tile_pos)