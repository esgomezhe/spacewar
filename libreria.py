import pygame
from pygame.locals import *
import random

BLANCO = (255, 255, 255)                        #En esta libreria definimos cosas que se usan en el juego, como los colores, y las clases de los elementos del juego (Jugador, Enemigos, Bala, Vida y modificadores)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
NARANJA = (255, 181, 70)
MASTER = (64, 171, 188)

class Jugador(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.vidas = 5
                self.puntos = 0
                self.ancho = 66
                self.alto = 66
                self.image = pygame.image.load('img/Nave 64.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = 477
                self.rect.y = 544

        def menosVida(self):
                self.vidas = self.vidas -1
        
        def masVida(self):
                self.vidas = self.vidas +1

        def masPuntos(self):
                self.puntos = self.puntos +1

        def menosPuntos(self):
                self.puntos = self.puntos -1
        

class Vida():
        def __init__(self, pantalla, num):
                self.image = pygame.image.load('img/Vida 32.png').convert_alpha()
                self.ancho = 33
                self.sep = 10
                self.pos_y= 40
                self.pos_xini= 952
                self.pos_x= self.pos_xini - (num*(self.ancho + self.sep))
                pantalla.blit(self.image, (self.pos_x,self.pos_y))

class Bala(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.color = NARANJA
                self.velocidad = 7      
                self.ancho = 5
                self.alto = 5
                self.fin = False
                self.image = pygame.Surface([self.ancho, self.alto])
                self.image.fill(self.color)
                self.rect = self.image.get_rect()
                
        def Arriba(self):
                self.rect.y = self.rect.y - self.velocidad



class Enemigo1(pygame.sprite.Sprite):

        def __init__(self, modo, limite_pan):
                pygame.sprite.Sprite.__init__(self)
                self.ancho = 66
                self.alto = 66
                self.fin = False
                if(modo):
                        self.image = pygame.image.load('img/Enem1 32.png').convert_alpha()
                        self.velocidad = 2
                else:
                        self.image = pygame.image.load('img/Enem1 64.png').convert_alpha()
                        self.velocidad = 1
                self.rect = self.image.get_rect()
                self.modojuego = modo
                self.l_pan = limite_pan + self.alto
                self.orientacion = True
                self.lim_orien = 0
                self.Aparecer()

        def Aparecer(self):
                self.rect.y = 0 - self.alto
                pos_x = 111
                self.rect.x = pos_x

        def Mover(self):
                nuevo_y = self.rect.y + self.velocidad
                if(nuevo_y < self.l_pan):
                        self.rect.y = nuevo_y
                        if(self.orientacion):
                                if(self.lim_orien < 50):
                                        self.rect.x = self.rect.x + 1
                                        self.lim_orien = self.lim_orien + 1
                                else:
                                        self.orientacion = False
                        else:
                                if(self.lim_orien > -50):
                                        self.rect.x = self.rect.x - 1
                                        self.lim_orien = self.lim_orien - 1
                                else:
                                        self.orientacion = True
                        
                else:
                        self.fin = True

        def __del__(self):
                print"Destruido"


class Enemigo2(pygame.sprite.Sprite):

        def __init__(self, modo, limite_pan):
                pygame.sprite.Sprite.__init__(self)
                self.ancho = 72
                self.alto = 72
                self.fin = False
                if(modo):
                        self.image = pygame.image.load('img/Enem2 32.png').convert_alpha()
                        self.velocidad = 2
                else:
                        self.image = pygame.image.load('img/Enem2 64.png').convert_alpha()
                        self.velocidad = 2
                self.rect = self.image.get_rect()
                self.l_pan = limite_pan + self.alto             
                self.orientacion = True
                self.lim_orien = 0
                self.Aparecer()

        def Aparecer(self):
                self.rect.y = 0 - self.alto
                pos_x = 282
                self.rect.x = pos_x

        def Mover(self):
                nuevo_y = self.rect.y + self.velocidad
                if(nuevo_y < self.l_pan):
                        self.rect.y = nuevo_y
                        if(self.orientacion):
                                if(self.lim_orien < 50):
                                        self.rect.x = self.rect.x + 1
                                        self.lim_orien = self.lim_orien + 1
                                else:
                                        self.orientacion = False
                        else:
                                if(self.lim_orien > -50):
                                        self.rect.x = self.rect.x - 1
                                        self.lim_orien = self.lim_orien - 1
                                else:
                                        self.orientacion = True
                        
                else:
                        self.fin = True

        def __del__(self):
                print"Destruido"


class Enemigo3(pygame.sprite.Sprite):

        def __init__(self, modo, limite_pan):
                pygame.sprite.Sprite.__init__(self)
                self.ancho = 64
                self.alto = 64
                self.fin = False
                if(modo):
                        self.image = pygame.image.load('img/Enem3 32.png').convert_alpha()
                        self.velocidad = 4
                else:
                        self.image = pygame.image.load('img/Enem3 64.png').convert_alpha()
                        self.velocidad = 2
                self.rect = self.image.get_rect()
                self.l_pan = limite_pan + self.alto             
                self.orientacion = True
                self.lim_orien = 0
                self.Aparecer()

        def Aparecer(self):
                self.rect.y = 0 - self.alto
                pos_x = 459
                self.rect.x = pos_x

        def Mover(self):
                nuevo_y = self.rect.y + self.velocidad
                if(nuevo_y < self.l_pan):
                        self.rect.y = nuevo_y
                        if(self.orientacion):
                                if(self.lim_orien < 50):
                                        self.rect.x = self.rect.x + 1
                                        self.lim_orien = self.lim_orien + 1
                                else:
                                        self.orientacion = False
                        else:
                                if(self.lim_orien > -50):
                                        self.rect.x = self.rect.x - 1
                                        self.lim_orien = self.lim_orien - 1
                                else:
                                        self.orientacion = True
                        
                else:
                        self.fin = True

        def __del__(self):
                print"Destruido"


class Enemigo4(pygame.sprite.Sprite):

        def __init__(self, modo, limite_pan):
                pygame.sprite.Sprite.__init__(self)
                self.ancho = 78
                self.alto = 78
                self.fin = False
                if(modo):
                        self.image = pygame.image.load('img/Enem4 32.png').convert_alpha()
                        self.velocidad = 3
                else:
                        self.image = pygame.image.load('img/Enem4 64.png').convert_alpha()
                        self.velocidad = 1
                self.rect = self.image.get_rect()
                self.l_pan = limite_pan + self.alto             
                self.orientacion = True
                self.lim_orien = 0
                self.Aparecer()

        def Aparecer(self):
                self.rect.y = 0 - self.alto
                pos_x = 628
                self.rect.x = pos_x

        def Mover(self):
                nuevo_y = self.rect.y + self.velocidad
                if(nuevo_y < self.l_pan):
                        self.rect.y = nuevo_y
                        if(self.orientacion):
                                if(self.lim_orien < 50):
                                        self.rect.x = self.rect.x + 1
                                        self.lim_orien = self.lim_orien + 1
                                else:
                                        self.orientacion = False
                        else:
                                if(self.lim_orien > -50):
                                        self.rect.x = self.rect.x - 1
                                        self.lim_orien = self.lim_orien - 1
                                else:
                                        self.orientacion = True
                        
                else:
                        self.fin = True

        def __del__(self):
                print"Destruido"



class Enemigo5(pygame.sprite.Sprite):

        def __init__(self, modo, limite_pan):
                pygame.sprite.Sprite.__init__(self)
                self.ancho = 64
                self.alto = 64
                self.fin = False
                if(modo):
                        self.image = pygame.image.load('img/Enem5 32.png').convert_alpha()
                        self.velocidad = 3
                else:
                        self.image = pygame.image.load('img/Enem5 64.png').convert_alpha()
                        self.velocidad = 1
                self.rect = self.image.get_rect()
                self.l_pan = limite_pan + self.alto             
                self.orientacion = True
                self.lim_orien = 0
                self.Aparecer()

        def Aparecer(self):
                self.rect.y = 0 - self.alto
                pos_x = 811
                self.rect.x = pos_x

        def Mover(self):
                nuevo_y = self.rect.y + self.velocidad
                if(nuevo_y < self.l_pan):
                        self.rect.y = nuevo_y
                        if(self.orientacion):
                                if(self.lim_orien < 50):
                                        self.rect.x = self.rect.x + 1
                                        self.lim_orien = self.lim_orien + 1
                                else:
                                        self.orientacion = False
                        else:
                                if(self.lim_orien > -50):
                                        self.rect.x = self.rect.x - 1
                                        self.lim_orien = self.lim_orien - 1
                                else:
                                        self.orientacion = True
                        
                else:
                        self.fin = True

        def __del__(self):
                print"Destruido"


class Modificador(pygame.sprite.Sprite):
        def __init__(self, tipoM):
                pygame.sprite.Sprite.__init__(self)
                self.tipo= tipoM

                if(self.tipo == 0):
                        self.image = pygame.image.load('img/Vida 64.png').convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.x = random.randint(50,950)
                        self.rect.y = random.randint(50,575)

                if(self.tipo == 1):
                        self.image = pygame.image.load('img/Estrella 64.png').convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.x = random.randint(50,950)
                        self.rect.y = random.randint(50,575)

                if(self.tipo == 2):
                        self.image = pygame.image.load('img/Moneda 64.png').convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.x = random.randint(50,950)
                        self.rect.y = random.randint(50,575)

                if(self.tipo == 3):
                        self.image = pygame.image.load('img/Fuego 64.png').convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.x = random.randint(50,950)
                        self.rect.y = random.randint(50,575)

