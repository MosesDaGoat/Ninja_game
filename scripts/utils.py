import pygame

import os

from constants import BLACK

# Dynamically get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the images directory relative to the script's location
BASE_IMG_PATH = os.path.join(BASE_DIR, '../images/')

def load_image(path, size=None, color_key=(255, 255, 255)):
    # Combine the base path with the relative path provided
    full_path = os.path.join(BASE_IMG_PATH, path)
    print("Loading image from:", full_path)  # Debug print statement
    img = pygame.image.load(full_path).convert()
    if size:
        img = pygame.transform.scale(img, size)
    img.set_colorkey(color_key)
    return img