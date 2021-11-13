import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.locals import *
from pygame_menu.events import *
from datetime import date

from sys import exit

HEIGHT = 720
WIDTH = 1280
class menuScore:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.a_key_down = False
        self.s_key_down = False
        self.d_key_down = False
        self.w_key_down = False
        self.running = True
        self.exitGame=False
        self.score = 0
        self.time = 0
        self.leaderboard = []
        self.today = date.today()

    def irAlMenuPrincipal(self):
        self.running=False
        #NO se como salir al menu principal todavia
        self.exitGame=True
        pass
    def continuarPartida(self):
        self.running=False
        pass
    def start(self, playerScore = 0, playerTime = 0):
        self.running=True
        self.dificultad=0
        self.tamaño=(0,0)

        pygame.display.set_caption('Fin - Seminario de Lenguajes - Laberinto')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.flip()
        self.menu = pygame_menu.Menu('Juego Finalizado', WIDTH, HEIGHT,
                        theme=pygame_menu.themes.THEME_DARK)       
        
        
        table = self.menu.add.table(table_id='leaderboard', font_size=32)
        table.default_cell_padding = 10
        table.default_row_color = (0, 0, 0)
        table.default_row_background_color = (33, 33, 33)
        table.set_margin(0,25)

        table.add_row(['#', 'Puntaje', 'Tiempo', 'Fecha'],
                    cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD)
        table.add_row([1, playerScore, str(playerTime).split('.', 1)[0], self.today.strftime('%d/%m/%Y')])       
    
        self.menu.add.button('Volver a Empezar',self.irAlMenuPrincipal)

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


