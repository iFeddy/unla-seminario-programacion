import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.locals import *
from pygame_menu.events import *
from datetime import date
import os
import json

from sys import exit

WIDTH = 1280
HEIGHT = 720

class menuScore:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.a_key_down = False
        self.s_key_down = False
        self.d_key_down = False
        self.w_key_down = False
        self.running = True
        self.exitGame = False
        self.score = 0
        self.time = 0
        self.leaderboard = []
        self.today = date.today()
        self.fileJson = os.path.join(os.getcwd() + '/leaderboards/scores.json')
        self.dificultad = 'Fácil'

    def irAlMenuPrincipal(self):
        self.running = False
        # NO se como salir al menu principal todavia
        self.exitGame = True
        pass

    def continuarPartida(self):
        self.running = False
        pass

    def start(self, playerScore=0, playerTime=0, dificultad=0):
        self.running = True
        self.tamaño = (0, 0)

        pygame.mixer.music.load('assets/victory.wav')
        pygame.mixer.music.play() 
        
        pygame.display.set_caption('Fin - Seminario de Lenguajes - Laberinto')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.flip()
        self.menu = pygame_menu.Menu('Juego Finalizado', WIDTH, HEIGHT,
                                     theme=pygame_menu.themes.THEME_DARK)

        #switch dificultad
        if dificultad == 1:
            self.dificultad = 'Fácil'
        elif dificultad == 1.5:
            self.dificultad = 'Normal'
        elif dificultad == 2:
            self.dificultad = 'Difícil'

        self.get_high_scores()

        self.leaderboard.append([playerScore, playerTime, self.dificultad, self.today.strftime('%d/%m/%Y')])

        self.update_high_scores()

        table = self.menu.add.table(table_id='leaderboard', font_size=32)
        table.default_cell_padding = 10
        table.default_row_color = (0, 0, 0)
        table.default_row_background_color = (33, 33, 33)
        table.set_margin(0, 25)

        table.add_row(['#', 'Puntaje', 'Tiempo', 'Dificultad', 'Fecha'],
                      cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD)

        for i in range(len(self.leaderboard)):
            if i < 5:
                table.add_row([str(i + 1), str(self.leaderboard[i][0]),
                               str(self.leaderboard[i][1]).split('.')[0]  + "s",
                               str(self.leaderboard[i][2]),
                               str(self.leaderboard[i][3])])

        self.menu.add.button('Volver a Empezar', self.irAlMenuPrincipal)

        self.pausa_loop()
        pass

    def get_high_scores(self):
        #self.fileJson = os.path.join( os.getcwd() + '/leaderboards/scores.json')
        if(os.path.exists(self.fileJson)):
            f = open(self.fileJson, 'r')
            try:
                self.leaderboard = json.loads(f.read())
            except ValueError:
                return False
            f.close()
        pass

    def update_high_scores(self):
        self.leaderboard.sort(key=lambda x: x[0], reverse=True)
        f = open(self.fileJson, 'w')
        f.write(json.dumps(self.leaderboard))
        f.close()
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
