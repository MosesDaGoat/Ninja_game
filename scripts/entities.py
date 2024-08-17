from xml.dom.minidom import Entity
import pygame
import pymunk
import pymunk.pygame_util

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size, speed=5, gravity=0.5, max_fall_speed=10):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.speed = speed
        self.gravity = gravity
        self.max_fall_speed = max_fall_speed

    def create_physics_entity(space, pos, size):
        body = pymunk.Body(1, pymunk.inf)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.friction = 0.5
        space.add(body, shape)
        return body

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tile_map, movement=(0, 0)):
        self.velocity[1] += self.gravity
        self.velocity[1] = min(self.velocity[1], self.max_fall_speed)

        # Apply horizontal movement
        self.pos[0] += movement[0]

        # Apply vertical movement
        self.pos[1] += self.velocity[1]
        entity_rect = self.rect()

        # Tile-based collision detection
        collisions = tile_map.tile_collision(entity_rect)

        for rect in collisions:
            if self.velocity[1] > 0:  # Falling
                self.pos[1] = rect.top - self.size[1]
                self.velocity[1] = 0  # Stop falling
                break  # Stop checking after first collision

        self.pos[1] = round(self.pos[1])

    def render(self, surface):
        surface.blit(self.game.assets["player"], self.pos)
