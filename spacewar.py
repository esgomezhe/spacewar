# -*- coding: cp1252 -*-
import pygame
import sys
import time
from pygame.locals import *
from libreria import *

ALTO = 625              #De la ventana
ANCHO = 1000

###############################################

pygame.init()                   #Crear pantalla
pantalla = pygame.display.set_mode([ANCHO,ALTO])
pygame.display.set_caption("Space Invaders :v")

fondo = pygame.image.load('img/Fondo.png').convert()       #Poner fondo
pantalla.blit(fondo, (0,0))
pygame.display.flip()

pygame.mixer.music.load('sounds/Fondo.mp3')            #Se cargan todos los sounds
pygame.mixer.music.play(-1)                                                     #Cancion de fondo
Laser = pygame.mixer.Sound('sounds/Disparo.wav')       
Estrella = pygame.mixer.Sound('sounds/Estrella.wav')
Explosion = pygame.mixer.Sound('sounds/Explosion.wav')
Moneda = pygame.mixer.Sound('sounds/Moneda.wav')
Vidas = pygame.mixer.Sound('sounds/Vida.wav')
Danio = pygame.mixer.Sound('sounds/Danio.wav')
Win = pygame.mixer.Sound('sounds/Win.ogg')

todos = pygame.sprite.Group()                   #Grupos de sprites en donde se van a guardar los objetos
enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()
mods = pygame.sprite.Group()

###############################################
muchasbalas = False                     #Variables para alterar el juego
hard = False

jugador = Jugador()             #Creamos un jugador
todos.add(jugador)              #Lo a�adimos a el grupo de todos

###############################################

enemigo1 = Enemigo1(hard, 625)          #Creamos los enemigos, son 5 tipos
enemigos.add(enemigo1)
todos.add(enemigo1)

enemigo2 = Enemigo2(hard, 625)
enemigos.add(enemigo2)
todos.add(enemigo2)

enemigo3 = Enemigo3(hard, 625)
enemigos.add(enemigo3)
todos.add(enemigo3)

enemigo4 = Enemigo4(hard, 625)
enemigos.add(enemigo4)
todos.add(enemigo4)

enemigo5 = Enemigo5(hard, 625)
enemigos.add(enemigo5)
todos.add(enemigo5)

###############################################

reloj = pygame.time.Clock()             #Un reloj, para controlar animaciones
terminar = False                                        #Variable para terminar el juego

###############################################

fuente = pygame.font.Font(None, 40)             #Cargamos los tipos de fuentes
fuente2 = pygame.font.Font(None, 24)

###############################################
while(not terminar):                    #Ciclo principal, en donde se ejecuta el juego

        tecla=pygame.key.get_pressed()          #Obtener pulsaciones en el teclado
        for event in pygame.event.get():                #Validaci�n de qu� tecla se oprimio
                if event.type == pygame.QUIT:                   #Si se oprimi� el bot�n de salir, salir :v
                    terminar = True
                    
                if tecla[K_ESCAPE]:                     #Si se oprimi� escape, salir :v
                        terminar = True
        
                elif tecla[K_SPACE]:                    #Si se oprime espacio, el personaje dispara
                        Laser.play()                            #Sonido bala
                        if(muchasbalas):                        #Validaci�n de tipo de balas (Muchas balas = 3 balas por disparo)
                                b = Bala()
                                b1 = Bala()
                                b2 = Bala()
                                b.rect.x = jugador.rect.x + 30                  #Rect x, rect y, funcionan para dar una posici�n en la patalla a un objeto
                                b.rect.y = jugador.rect.y
                                b1.rect.x = jugador.rect.x + 20
                                b1.rect.y = jugador.rect.y
                                b2.rect.x = jugador.rect.x + 40
                                b2.rect.y = jugador.rect.y
                                balas.add(b)                                    #A�adimos las balas, a el grupo de las balas
                                balas.add(b1)
                                balas.add(b2)
                                todos.add(b)                            #A�adimos las balas, al grupo de todos
                                todos.add(b1)
                                todos.add(b2)

                        else:
                                b = Bala()
                                b.rect.x = jugador.rect.x + 30
                                b.rect.y = jugador.rect.y
                                balas.add(b)
                                todos.add(b)
                        
                                        
                                
        todos.update()                          #Actualizar todos los items creados
        pantalla.blit(fondo, (0,0))             #Poner fondo

        puntos = fuente2.render("PUNTAJE", True, BLANCO)                        #Cargamos la fuente, y posicionamos "Puntaje"
        puntos2 = fuente.render(str(jugador.puntos), True, NARANJA)     #Cargamos la fuente, y posicionamos el valor del puntaje, los ponemos uno junto al otro
        puntos_rect = puntos.get_rect()
        puntos_x = 15   
        puntos_y = 20
        puntos2_rect = puntos.get_rect()
        puntos2_x = 20   
        puntos2_y = 50
        pantalla.blit(puntos, [puntos_x, puntos_y])
        pantalla.blit(puntos2, [puntos2_x, puntos2_y])



        vidas = fuente2.render("VIDAS", True, BLANCO)                   #Vidas del jugador en pantalla
        vidas_rect = puntos.get_rect()
        vidas_x = 930
        vidas_y = 20
        pantalla.blit(vidas, [vidas_x, vidas_y])


        if (jugador.vidas == 0):                                                        #Si el jugador se ha quedado sin vidas, game over
                texto = fuente.render("G A M E   O V E R", True, BLANCO)
                texto_rect = texto.get_rect()
                texto_x = pantalla.get_width() / 2 - texto_rect.width / 2       
                texto_y = pantalla.get_height() / 2 - texto_rect.height / 2
                pantalla.blit(texto, [texto_x, texto_y])
                todos.remove(jugador)
                for e1 in enemigos:                     #Eliminar enemigos
                        enemigos.remove(e1)
                        todos.remove(e1)

        if (jugador.puntos == 100):                             #Si se logran 100 puntos, el juego termina
                texto = fuente.render("Y O U   W I N", True, BLANCO)
                texto_rect = texto.get_rect()
                texto_x = pantalla.get_width() / 2 - texto_rect.width / 2       
                texto_y = pantalla.get_height() / 2 - texto_rect.height / 2
                pantalla.blit(texto, [texto_x, texto_y])
                todos.remove(jugador)
                for e1 in enemigos:
                        enemigos.remove(e1)
                        todos.remove(e1)
                Win.play()                              #Sonido victoria
                                
        else:                                   #Ac� validamos las dem�s teclas
                if event.type == pygame.KEYDOWN:                #Flecha arriba, abajo, derecha, izquiera para moverse, repectivamente
                        if event.key == pygame.K_LEFT:
                                if(jugador.rect.x >= 10):
                                        jugador.rect.x = jugador.rect.x - 5
                        elif event.key == pygame.K_RIGHT:
                                if(jugador.rect.x <= 990 - jugador.ancho):
                                        jugador.rect.x = jugador.rect.x + 5
                        elif event.key == pygame.K_UP:
                                if(jugador.rect.y >= 10):
                                        jugador.rect.y = jugador.rect.y - 5
                        elif event.key == pygame.K_DOWN:
                                if(jugador.rect.y <= 615 - jugador.alto):
                                        jugador.rect.y = jugador.rect.y + 5

                col_obj = pygame.sprite.spritecollide(jugador, enemigos, True)                  #Grupo en el que guardamos las colisiones del jugador con los enemigos

                for ec in col_obj:                              #Para cada colisi�n
                        Danio.play()                                    #Sonido da�o
                        tipoenem3 = random.randint(0,4)                 #Creamos un nuevo enemigo al azar, un n�mero entero del 0 al 4. cada n�mero me representa un tipo de enmigo
                        if (tipoenem3 == 0):
                                ene = Enemigo1(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        elif (tipoenem3 == 1):
                                ene = Enemigo2(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        elif (tipoenem3 == 2):
                                ene = Enemigo3(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        elif (tipoenem3 == 3):
                                ene = Enemigo4(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        elif (tipoenem3 == 4):
                                ene = Enemigo5(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        
                        jugador.menosVida()             #Quitamos vida al jugador

                       
        
                for nv in range(jugador.vidas):         #Para cada vida, ponemos un coraz�n en pantalla
                        vd = Vida(pantalla, nv)
        
                
                for bl in balas:                        #Para cada bala
                        l_impactos = pygame.sprite.spritecollide(bl, enemigos, True)            #Guardamos en un grupo de colisiones, colisiones de balas con enemigos
                        for en in l_impactos:                           #Para cada impacto, eliminamos el enemigo y creamos uno nuevo, al azar 
                                balas.remove(bl)
                                todos.remove(bl)
                                tipoenem = random.randint(0,4)
                                if (tipoenem == 0):
                                        ene = Enemigo1(hard, 625)
                                        enemigos.add(ene)
                                        todos.add(ene)
                                elif (tipoenem == 1):
                                        ene = Enemigo2(hard, 625)
                                        enemigos.add(ene)
                                        todos.add(ene)
                                elif (tipoenem == 2):
                                        ene = Enemigo3(hard, 625)
                                        enemigos.add(ene)
                                        todos.add(ene)
                                elif (tipoenem == 3):
                                        ene = Enemigo4(hard, 625)
                                        enemigos.add(ene)
                                        todos.add(ene)
                                elif (tipoenem == 4):
                                        ene = Enemigo5(hard, 625)
                                        enemigos.add(ene)
                                        todos.add(ene)

                                jugador.masPuntos()                     #Por cada enemigo eliminado, sumamos el puntaje

                                if (jugador.puntos == 60):              #Si el jugador alcanza 60 puntos, el juego se hace dificil
                                        hard = True
        
                                
                                if(jugador.puntos == 20 or jugador.puntos == 40 or jugador.puntos == 60 or jugador.puntos == 80):               #Cada 20 puntos, damos un modificador al jugador (Vida, Puntos, M�s balas o explosi�n) al azar
                                        tipomod = random.randint(0,3)
                                        if (tipomod == 0):
                                                Mod = Modificador(0)
                                                mods.add(Mod)
                                                todos.add(Mod)
                                        elif (tipomod == 1):
                                                Mod = Modificador(1)
                                                mods.add(Mod)
                                                todos.add(Mod)
                                        elif (tipomod == 2):
                                                Mod = Modificador(2)
                                                mods.add(Mod)
                                                todos.add(Mod)
                                        elif (tipomod == 3):
                                                Mod = Modificador(3)
                                                mods.add(Mod)
                                                todos.add(Mod)
                                                                        

                        if bl.rect.y < -10:                     #Cuando la bala se sale de la pantalla, la borramos
                                balas.remove(bl)
                                todos.remove(bl)


        for md in mods:         #Para cada modificador
                col_mod = pygame.sprite.spritecollide(jugador, mods, True)              #Groupo de colisiones entre el modificador y el jugador
                for en in col_mod:                              #Para cada colisi�n, miramos que tipo de modificador es. Reproducimos el sonido y su acci�n correspondiente 
                        if (md.tipo == 0):                      #Vida
                                Vidas.play()
                                jugador.masVida()
                        elif (md.tipo == 1):            #M�s balas
                                Estrella.play()
                                muchasbalas= True                                
                        elif (md.tipo == 2):            #Puntos
                                Moneda.play()
                                jugador.puntos = jugador.puntos + 15
                        elif (md.tipo == 3):            #Explosi�n (Cuando hay una explosi�n, se eliminan todos lo enemigos que hayan en el momento)
                                Explosion.play()
                                for e1 in enemigos:
                                        enemigos.remove(e1)
                                        todos.remove(e1)
                                
                                enemigo1 = Enemigo1(hard, 625)
                                enemigos.add(enemigo1)
                                todos.add(enemigo1)

                                enemigo2 = Enemigo2(hard, 625)
                                enemigos.add(enemigo2)
                                todos.add(enemigo2)

                                enemigo3 = Enemigo3(hard, 625)
                                enemigos.add(enemigo3)
                                todos.add(enemigo3)

                                enemigo4 = Enemigo4(hard, 625)
                                enemigos.add(enemigo4)
                                todos.add(enemigo4)

                                enemigo5 = Enemigo5(hard, 625)
                                enemigos.add(enemigo5)
                                todos.add(enemigo5)                                


        for e1 in enemigos:             #Para cada enemigo
                e1.Mover()                      #Lo ponemos a moverse, de manera regular en zig zag, de arriba hacia abajo
                if e1.fin:                                      #Si ya alcanz� el limite de la pantalla, lo borramos y creamos uno nuevo
                        enemigos.remove(e1)
                        todos.remove(e1)
                        tipoenem2 = random.randint(0,4)
                        if (tipoenem2 == 0):
                                ene = Enemigo1(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        elif (tipoenem2 == 1):
                                ene = Enemigo2(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        elif (tipoenem2 == 2):
                                ene = Enemigo3(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        elif (tipoenem2 == 3):
                                ene = Enemigo4(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                        elif (tipoenem2 == 4):
                                ene = Enemigo5(hard, 625)
                                enemigos.add(ene)
                                todos.add(ene)
                                
                        jugador.menosPuntos()           #Cada que un enemigo llega hasta abajo, el jugador pierde puntos
                
                for bl in balas:                #Movemos las balas hacia arriba
                        bl.Arriba()

        todos.draw(pantalla)            #Dibujamos todo
        reloj.tick(60)                          #Ponemos en marcha el reloj
        pygame.display.flip()                   #Actualizamos pantalla

###############################################

pygame.quit()           #Salir
