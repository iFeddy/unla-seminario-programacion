import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.locals import *
from pygame_menu.events import *

from sys import exit


HEIGHT = 720
WIDTH = 1280
class menuPausa:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.a_key_down = False
        self.s_key_down = False
        self.d_key_down = False
        self.w_key_down = False
        self.running = True
        self.exitGame=False

    def irAlMenuPrincipal(self):
        self.running=False
        #NO se como salir al menu principal todavia
        self.exitGame=True
        pass
    def continuarPartida(self):
        self.running=False
        pass
    def start(self):
        self.running=True
        self.dificultad=0
        self.tamaño=(0,0)

        pygame.display.set_caption('Menu pausa')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.flip()
        self.menu = pygame_menu.Menu('Menu pausa', WIDTH, HEIGHT,
                        theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button('Continuar',self.continuarPartida)
        self.menu.add.button('Salir al menu principal',self.irAlMenuPrincipal)
        
        self.pausa_loop()
        pass
    def pausa_loop(self):
        while(self.running):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                   self.continuarPartida

            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.screen)

            pygame.display.update()


