import pygame

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tile_map = {}
        self.solid_tiles = {"grass", "stone"}  # Define "grass" and "stone" as solid tiles

        # Calculate screen dimensions in tiles
        screen_width_in_tiles = self.game.screen.get_width() // self.tile_size
        screen_height_in_tiles = self.game.screen.get_height() // self.tile_size

        # Determine the middle x position for the vertical stone wall
        middle_x = screen_width_in_tiles // 2

        # Define the three connected grass rows
        self.top_row_y = screen_height_in_tiles - 5  # Fifth-to-bottom row (hidden)
        self.middle_row_y = screen_height_in_tiles - 4  # Fourth-to-bottom row (hidden)
        self.bottom_row_y = screen_height_in_tiles - 3  # Third-to-bottom row (visible)

        # Populate the three connected grass rows with grass tiles
        for x in range(screen_width_in_tiles):
            # Top row (invisible, used for physics only)
            self.tile_map[f"{x};{self.top_row_y}"] = {"type": "grass", "variant": "0", "pos": (x, self.top_row_y)}
            # Middle row (invisible, used for physics only)
            self.tile_map[f"{x};{self.middle_row_y}"] = {"type": "grass", "variant": "0", "pos": (x, self.middle_row_y)}
            # Bottom row (visible, used for rendering and physics)
            self.tile_map[f"{x};{self.bottom_row_y}"] = {"type": "grass", "variant": "0", "pos": (x, self.bottom_row_y)}

        # Populate the vertical stone wall
        for y in range(screen_height_in_tiles):
            self.tile_map[f"{middle_x};{y}"] = {"type": "stone", "variant": "0", "pos": (middle_x, y)}

    def is_solid(self, x, y):
        """Check if the tile at (x, y) is solid."""
        tile_key = f"{x};{y}"
        if tile_key in self.tile_map and self.tile_map[tile_key]["type"] in self.solid_tiles:
            return True
        return False

    def tile_collision(self, rect):
        """Check for collisions with solid tiles."""
        tiles_to_check = []
        tile_x_start = rect.left // self.tile_size
        tile_x_end = rect.right // self.tile_size
        tile_y_start = rect.top // self.tile_size
        tile_y_end = rect.bottom // self.tile_size

        for y in range(tile_y_start, tile_y_end + 1):
            for x in range(tile_x_start, tile_x_end + 1):
                if self.is_solid(x, y):
                    tiles_to_check.append(pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

        return tiles_to_check

    def render(self, surf):
        """Render only the bottom row of grass and the vertical stone wall."""
        for loc, tile in self.tile_map.items():
            tile_type = tile["type"]
            tile_variant = tile.get("variant", "0")
            tile_pos = tile["pos"]
            tile_image = self.game.assets[tile_type].get(tile_variant, None)

            if tile_image:
                pixel_pos = (tile_pos[0] * self.tile_size, tile_pos[1] * self.tile_size)

                # Render only the bottom row of grass (skip the top two rows)
                if tile_type == "grass" and (tile_pos[1] == self.top_row_y or tile_pos[1] == self.middle_row_y):
                    continue

                # Render the tile (grass or stone)
                surf.blit(tile_image, pixel_pos)





