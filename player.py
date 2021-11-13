import pygame
import math
HEIGHT = 720
WIDTH = 1280

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y, tileWidth, tileHeight):
        super().__init__()
        self.image = pygame.image.load("assets/unla.jpg").convert()
        self.image = pygame.transform.scale(self.image, (math.floor(tileWidth * 0.75),math.floor(tileHeight * 0.75)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
    
    def move_right(self):
        self.rect.x += self.speed
        if self.rect.x > (WIDTH - self.rect.width):
            self.rect.x = WIDTH - self.rect.width
    
    def move_up(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y = 0
    
    def move_down(self):
        self.rect.y += self.speed
        if self.rect.y > (HEIGHT - self.rect.height):
            self.rect.y = HEIGHT - self.rect.height
    
    def stop(self):
        pass

    def update(self):
        
        pass
