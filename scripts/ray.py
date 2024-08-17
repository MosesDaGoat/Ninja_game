import pygame

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def cast(self, tilemap):
        # Cast a ray and return the first collision point or None
        for length in range(0, 1000, 1):  # Adjust the range for your game size
            test_point = self.origin + (self.direction * length)
            test_tile_x = int(test_point.x) // tilemap.tile_size
            test_tile_y = int(test_point.y) // tilemap.tile_size

            if tilemap.is_solid(test_tile_x, test_tile_y):
                return pygame.Vector2(test_tile_x, test_tile_y) * tilemap.tile_size

        return None
