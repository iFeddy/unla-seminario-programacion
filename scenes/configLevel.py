from scenes.level import Level
import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.locals import *

from sys import exit


HEIGHT = 720
WIDTH = 1280
class configLevel:


    def __init__(self):
        self.clock = pygame.time.Clock()
        self.a_key_down = False
        self.s_key_down = False
        self.d_key_down = False
        self.w_key_down = False
        self.running=True
        self.level = Level(0,0)

    def start_the_game(self):
        if(self.dificultad>0 and self.tamaño!=(0,0)):
            self.level = Level(self.dificultad,self.tamaño)
            self.level.start()
        pass
    def alSeleccionarDificultad(self,p1,*args,**arvg):
        switcher = {
                0: 25,
                1: 50,
                2: 100,
            }
        if(bool):
            self.dificultad=switcher.get(p1[1])
        pass
    def alSeleccionarTamanio(self,p1,*args,**arvg):
        switcher = {
            0: (45,23),
            1: (65,33),
            2: (79,39),
        }
        if(bool):
            self.tamaño=switcher.get(p1[1])
        pass
    def atras(self):
        self.running=False
        pass
    def start(self):
        self.dificultad=0
        self.tamaño=(0,0)

        pygame.display.set_caption('Configuracion de nivel ')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.flip()
        self.menu = pygame_menu.Menu('Configuracion de nivel', WIDTH, HEIGHT,
                        theme=pygame_menu.themes.THEME_DARK,columns=1,rows=3)
        
        self.menu.add.dropselect("Dificultad: ", [('Fácil', 0), ('Medio', 1), ('Difícil', 2)] ,None,"",self.alSeleccionarDificultad,None,None,False,"Seleccion la dificultad",False)
        self.menu.add.dropselect("Tamaño: ",[('Pequeño', 0), ('Mediano', 1), ('Grande', 2)],None,"",self.alSeleccionarTamanio,None,None,False,"Selecciona el tamaño",False)
                                      

        self.frame=self.menu.add.frame_h(300,100,padding=0)
        self.frame.pack(
            self.menu.add.button('Jugar', self.start_the_game)
        )
        self.frame.pack(
            self.menu.add.button('Atras', self.atras)
        )

        self.config_loop()
        pass
    def config_loop(self):
        while(self.running):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                   self.running=False
            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.screen)
            pygame.display.update()
            if(self.level.exitGame==True):
                self.running=False

