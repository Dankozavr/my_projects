import pygame
import math
from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)
        self.initial_y = y
        self.speed = speed

    def move(self, max_width):
        if self.x <= 0:
            self.speed = abs(self.speed)
            self.turn()
        elif self.x >= max_width - self.width:
            self.speed = -self.speed
            self.turn()
        self.x += self.speed
        self.y = 10 * math.sin(self.x / 40) + self.initial_y
        self.hitbox_x += self.speed
    
    def turn(self):
        self.image = pygame.transform.flip(self.image, True, False)