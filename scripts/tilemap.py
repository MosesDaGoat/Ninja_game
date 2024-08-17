class Tilemap:
    def __init__(self, tile_size=16):
        self.tile_size = tile_size
        self.tile_map = {}
        self.off_grid_tiles = []