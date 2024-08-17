from xml.dom.minidom import Entity
import pygame

class PhysicsEntity:
    def __init__(self, game,e_type,pos,size,speed=5,gravity=0.5,max_fall_speed=10):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.speed = speed
        self.gravity = gravity
        self.max_fall_speed = max_fall_speed

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self,tile_map, movement=(0,0)):
        frame_movement = (movement[0] * self.speed + self.velocity[0], movement[1] + self.velocity[1])

        # apply gravity to vertical velocity
        self.velocity[1]  = min(self.velocity[1] + self.gravity, self.max_fall_speed)

        self.pos[0] += frame_movement[0]

        entity_rect = self.rect()
        for rect in tile_map.physics_rect_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tile_map.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.x

    def render(self, surface):
        surface.blit(self.game.assets["player"], self.pos)