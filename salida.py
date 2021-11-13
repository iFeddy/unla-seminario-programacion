import pygame


class Salida(pygame.sprite.Sprite):
    def __init__(self, x, y,tileWidth,tileHeight,color):
        super().__init__()
        # Crea una imagen del bloque y lo rellena de color.
        #self.image = pygame.Surface([tileWidth, tileHeight])
        self.image = pygame.image.load("assets/puerta.jpg").convert()
        #self.image.fill(color)
        self.image = pygame.transform.scale(self.image, (tileWidth, tileHeight))
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y
    
    def stop(self):
        pass

    def update(self):
        pass
