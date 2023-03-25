import pygame
from game_object import GameObject
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):

        self.width = 800
        self.height = 800

        self.white_colour = (255, 255, 255)
        
        self.game_window = pygame.display.set_mode((self.width, self.height))
        
        self.clock = pygame.time.Clock()
        
        self.backbround = GameObject(0, 0, 800, 800, "treasure_walk_game/assets/background.png")
        self.treasure = GameObject(375, 50, 50, 50, "treasure_walk_game/assets/treasure.png")

        self.level = 1.0

        self.reset_map()
        
    def reset_map(self):
        self.player = Player(375, 700, 60, 60, "treasure_walk_game/assets/player.png", 5)

        speed = 5 + (self.level * 2)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(50, 600, 50, 50, "treasure_walk_game/assets/enemy1.png", speed),
                Enemy(750, 400, 50, 50, "treasure_walk_game/assets/enemy2.png", speed),
                Enemy(50, 200, 50, 50, "treasure_walk_game/assets/enemy3.png", speed)
            ]
        elif self.level >= 2:
            self.enemies = [
                Enemy(50, 600, 50, 50, "treasure_walk_game/assets/enemy1.png", speed),
                Enemy(750, 400, 50, 50, "treasure_walk_game/assets/enemy2.png", speed),
            ]
        else:
            self.enemies = [
                Enemy(50, 600, 50, 50, "treasure_walk_game/assets/enemy1.png", speed),
            ]
    
    def draw_game_objects(self):
        self.game_window.fill(self.white_colour)

        self.game_window.blit(self.backbround.image, (self.backbround.x, self.backbround.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        pygame.display.update()

    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False
        
    def detect_collision(self, object_1, object_2):
        # if object 1 is below object 2
        if object_1.hitbox_y > (object_2.hitbox_y + object_2.hitbox_height):
            return False
        # of object 1 is above object 2
        elif (object_1.hitbox_y + object_2.hitbox_height) < object_2.hitbox_y:
            return False
        # if object 1 is to the right of object 2
        elif object_1.hitbox_x > (object_2.hitbox_x + object_2.hitbox_width):
            return False
        # if object 1 is to the left of object 2
        elif (object_1.hitbox_x + object_2.hitbox_width) < object_2.hitbox_x:
            return False
        else: return True

    def run_game_loop(self):
        player_direction = 0
        while True:
            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

            # Execute logic
            self.move_objects(player_direction)

            # Update display
            self.draw_game_objects()

            # Detect collisions
            if self.check_if_collided():
                self.reset_map()
                
            self.clock.tick(60)