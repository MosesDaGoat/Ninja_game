import os

import pygame

BASE_IMG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/images/')

def load_image(path):
    img = pygame.image.load(os.path.join(BASE_IMG_PATH, path)).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    full_path = os.path.join(BASE_IMG_PATH, path)
    try:
        for img_name in sorted(os.listdir(full_path)):
            images.append(load_image(os.path.join(path, img_name)))
    except FileNotFoundError:
        print(f"Error: The path '{full_path}' does not exist.")
    return images


class Animation:
    def __init__(self, images, img_dur =5, loop=True):
        self.images = images
        self.img_duration = img_dur
        self.loop = loop
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) -1)
            if self.frame >= self.img_duration * len(self.images)-1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)]