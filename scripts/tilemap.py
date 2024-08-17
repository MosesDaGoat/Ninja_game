class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game  # Reference to the game object to access assets
        self.tile_size = tile_size
        self.tile_map = {}
        self.off_grid_tiles = []

        screen_width_in_tiles = self.game.screen.get_width() // self.tile_size
        screen_height_in_tiles = self.game.screen.get_height() // self.tile_size

        # Calculate the starting positions for the grass row and stone column
        start_x = (screen_width_in_tiles - 10) // 2  # Center the grass row horizontally
        start_y = (screen_height_in_tiles - 10) // 2  # Center the stone column vertically

        for i in range(10):
            self.tile_map[f"{start_x + i};{start_y}"] = {"type": "grass", "variant": "1", "pos": (start_x + i, start_y)}

            # Add a vertical column of stone tiles
        for i in range(10):
            self.tile_map[f"{start_x};{start_y + i}"] = {"type": "stone", "variant": "0", "pos": (start_x, start_y + i)}

        # Example hardcoded tiles, you can modify this to fit your needs

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