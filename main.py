from scenes.configLevel import configLevel
import pygame
import pygame_menu
from sys import exit

pygame.init()
HEIGHT = 1280
WIDTH = 720

screen = pygame.display.set_mode((HEIGHT, WIDTH))
running = True
pygame.display.set_caption("Seminario de Lenguajes - Laberinto")
pygame.display.set_icon(pygame.image.load('assets/gamepad.png'))
clock = pygame.time.Clock()

def start_the_game():
    # Poner el primer nivel aca
    level = configLevel()
    level.start()
    pass

def main():
    menu = pygame_menu.Menu('Seminario de Lenguajes - Laberinto', HEIGHT, WIDTH,
                       theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Jugar', start_the_game)
    menu.add.button('Salir', pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pass

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
    main()