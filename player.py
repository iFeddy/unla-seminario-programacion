import pygame
HEIGHT = 1280
WIDTH = 720

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/unla.jpg").convert()
        self.image = pygame.transform.scale(self.image, (10,10))
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
        if self.rect.x > (HEIGHT - self.rect.width):
            self.rect.x = HEIGHT - self.rect.width
    
    def move_up(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y = 0
    
    def move_down(self):
        self.rect.y += self.speed
        if self.rect.y > (WIDTH - self.rect.height):
            self.rect.y = WIDTH - self.rect.height
    
    def stop(self):
        pass

    def update(self):
        
        pass
