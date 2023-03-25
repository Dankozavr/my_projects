import pygame

class GameObject():
    def __init__(self, x, y, width, height, image_path):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.hitbox_x = self.x + self.width * 0.2
        self.hitbox_y = self.y + self.height * 0.2
        self.hitbox_width = self.width * 0.6
        self.hitbox_height = self.height * 0.6
