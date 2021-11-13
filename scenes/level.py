from salida import Salida
from player import Player
from Pared import Pared
from scenes.menuPausa import menuPausa
from scenes.menuScore import menuScore
from salida import Salida
from Theseus import Maze
from Theseus import MazeFrontend
import pygame
from pygame.locals import *
from pygame import time
from pygame.color import *
from pygame.gfxdraw import *
import random

HEIGHT = 1280
WIDTH = 720

class Level:
    def __init__(self,dificultad,tamaño):
        self.level = 1
        self.clock = pygame.time.Clock()
        self.a_key_down = False
        self.s_key_down = False
        self.d_key_down = False
        self.w_key_down = False
        self.dificultad=dificultad
        self.tamaño=tamaño
        self.exitGame=False
        self.pausa=menuPausa();
        self.mScore=menuScore();
        #contador de tiempo
        self.tiempo = 0
        self.auxTiempo = 1
        #score
        self.score = 0

    def start(self):
        pygame.init()
        pygame.display.set_caption('Nivel ' + str(self.level))
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.screen_rect = self.screen.get_rect()
        pygame.display.flip()
        self.running = True
        self.background = pygame.Surface((HEIGHT, WIDTH))
        self.crear_laverinto()    
        self.crear_jugador_salida()           
        self.level_loop()      
    def posicion_aleatoria(self):
        #self.laberinto.printMaze()
        labRight = self.labLeft + self.laberinto.width * self.tileWidth
        labBottom = self.labTop + self.laberinto.height * self.tileHeight
        xStart=random.randrange(int(self.labLeft),labRight,self.tileWidth)
        yStart=random.randrange(int(self.labTop),labBottom,self.tileHeight)
        return (xStart,yStart)
    def check_colisiones(self,objeto,grupo):
        colision=False
        for pared in grupo:
            if (pygame.sprite.collide_rect(objeto,pared)):
                colision=True
        return colision
    def crear_jugador_salida(self):
        self.jugador_group = pygame.sprite.Group()
        self.salida_group = pygame.sprite.Group()
        colisiones=True;
        while(colisiones==True):
            xyRandom=self.posicion_aleatoria()
            self.player = Player(xyRandom[0],xyRandom[1])
            colisiones=self.check_colisiones(self.player,self.paredes_group)
        #self.player.rect.center = self.screen_rect.center
        self.player.update()
        self.jugador_group.add(self.player)       
        
        colisiones=True;
        distancia=True
        while(colisiones==True or distancia==True):
            xyRandom=self.posicion_aleatoria()
            self.salida=Salida(xyRandom[0],xyRandom[1],self.tileHeight,self.tileWidth,THECOLORS['red'])
            colisiones=self.check_colisiones(self.salida,self.paredes_group)
            if (colisiones==False):
                xStart=int((self.player.rect.x - self.labLeft)/ self.tileHeight)
                yStart=int((self.player.rect.y - self.labTop)/ self.tileHeight)
                xEnd=int((xyRandom[0] - self.labLeft)/ self.tileHeight)
                yEnd=int((xyRandom[1] - self.labTop)/ self.tileHeight)
                caminoSalida=self.laberinto.findWay(xStart,yStart,xEnd,yEnd)
                if(len(caminoSalida)>self.dificultad and len(caminoSalida)<(self.dificultad+20)):
                    distancia=False
        self.salida.update()
        self.salida_group.add(self.salida)
        pass   

    def crear_laverinto(self):
        self.laberinto = Maze(self.tamaño[0],self.tamaño[1],1,1)
        self.laberinto.generateMaze(1,1, 10)
        self.tileHeight = 15
        self.tileWidth = 15
        self.labTop = 80
        self.labLeft = 0
        self.dibujar_laberinto(self.laberinto)
        pass
    def dibujar_laberinto(self,laberinto):
        # posicion en screen
        xpos=self.labLeft
        ypos=self.labTop
        self.paredes_group = pygame.sprite.Group()
        for y in range(laberinto.height):
            line = laberinto.maze[y]
            for x in range(laberinto.width):
                if line[x] == 1:
                    # Draw paredes
                    self.pared=Pared(xpos, ypos, self.tileWidth, self.tileHeight,THECOLORS['orange'])
                    self.pared.update()
                    self.paredes_group.add(self.pared)
                #else:
                    # Draw pasilos
                    #self.pasillo=Pared(xpos, ypos, self.tileWidth, self.tileHeight,THECOLORS['black'])
                    #self.pasillo.update()
                    #self.pasillos_group.add(self.pasillo)
                xpos = xpos + self.tileWidth

            xpos = self.labLeft
            ypos = ypos + self.tileHeight
    def level_loop(self):       
        while self.running:
            self.screen.fill((0,0,0))
            self.jugador_group.update()
            self.jugador_group.clear(self.screen,self.background)
            self.jugador_group.draw(self.screen)

            self.paredes_group.update()
            self.paredes_group.clear(self.screen,self.background)
            self.paredes_group.draw(self.screen)

            self.salida_group.update()
            self.salida_group.clear(self.screen,self.background)
            self.salida_group.draw(self.screen)

            self.tiempo += self.clock.tick()/100
              
            contador = pygame.font.SysFont("Tahoma", 32, bold=False, italic=False).render("Tiempo: "+ str(self.tiempo).split('.', 1)[0], 1, (255, 255, 255))
            self.screen.blit(contador, (0, 0))

            contadorScore = pygame.font.SysFont("Tahoma", 32, bold=False, italic=False).render("Puntaje: "+ str(self.score), 1, (255, 255, 255))
            self.screen.blit(contadorScore, (0, 30))

            pygame.display.update()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.pausa.start()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.pausa.start()
                    elif event.key == K_d:
                        self.d_key_down = True 
                    elif event.key == K_a:
                        self.a_key_down = True 
                    elif event.key == K_w:
                        self.w_key_down = True 
                    elif event.key == K_s:
                        self.s_key_down = True
                elif event.type == KEYUP:
                    if event.key == K_d:
                        self.d_key_down = False
                    elif event.key == K_a:
                        self.a_key_down = False
                    elif event.key == K_w:
                        self.w_key_down = False
                    elif event.key == K_s:
                        self.s_key_down = False
            if self.d_key_down:
                self.player.move_right()
                #Si hay colision vuelve a la ubicacion anterior
                if self.check_colisiones(self.player,self.paredes_group)==True:
                    self.player.move_left()
                else:
                    self.score += 1
            if self.a_key_down:
                self.player.move_left()
                #Si hay colision vuelve a la ubicacion anterior
                if self.check_colisiones(self.player,self.paredes_group)==True:
                    self.player.move_right()
                else:
                    self.score += 1
            if self.w_key_down:
                self.player.move_up()
                #Si hay colision vuelve a la ubicacion anterior
                if self.check_colisiones(self.player,self.paredes_group)==True:
                    self.player.move_down()
                else:
                    self.score += 1
            if self.s_key_down:
                self.player.move_down()
                #Si hay colision vuelve a la ubicacion anterior
                if self.check_colisiones(self.player,self.paredes_group)==True:
                    self.player.move_up()
                else:
                    self.score += 1
            if not self.d_key_down and not self.a_key_down and not self.w_key_down and not self.s_key_down:
                self.player.stop()
            
            if self.check_colisiones(self.player,self.salida_group)==True:
                self.running = False
                self.mScore.start(self.score, self.tiempo)
                #Mensaje de ganador
            if(self.pausa.exitGame==True):
                self.running=False  
                self.exitGame=True
        pass


