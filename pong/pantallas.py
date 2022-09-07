import pygame as pg
from pong.entities import Bola, Raqueta
from pong import ALTO, ANCHO, AMARILLO, BLANCO, MAGENTA, NARANJA, NEGRO, FPS, PRIMER_AVISO, PUNTUACION_GANADORA, ROJO, SEGUNDO_AVISO, TIEMPO_MAXIMO_PARTIDA, PRIMER_AVISO, SEGUNDO_AVISO

pg.init()

class Partida:
    def __init__(self, pantalla, cronometro):
        self.pantalla_principal = pantalla
        pg.display.set_caption("Pong")
        self.cronometro = cronometro
        self.cronometro_p = TIEMPO_MAXIMO_PARTIDA

        self.bola = Bola(ANCHO // 2, ALTO //2, color = BLANCO)
        self.raqueta1 = Raqueta(20, ALTO // 2, w=30, h=114, color = AMARILLO)
        self.raqueta1.vy = 5
        self.raqueta2 = Raqueta(ANCHO - 20, ALTO // 2, w=30, h=114, color = AMARILLO)
        self.raqueta2.imagen = "drcha"
        self.raqueta2.vy = 5
        
        self.puntuacion1 = 0
        self.puntuacion2 = 0

        self.fuenteMarcador = pg.font.Font("pong/fonts/Silkscreen.ttf", 40)
        self.fuenteCronometro_p = pg.font.Font("pong/fonts/Silkscreen.ttf", 20)

        self.contadorFotogramas = 0
    
        self.colorFondo = NEGRO
    
    def fijar_fondo(self):
        self.contadorFotogramas += 1

        if self.cronometro_p > PRIMER_AVISO:
            self.contadorFotogramas = 0
            return NEGRO
        elif self.cronometro_p > SEGUNDO_AVISO:
            if self.contadorFotogramas == 10:
                if self.colorFondo == NEGRO:
                    self.colorFondo = NARANJA
                else:
                    self.colorFondo = NEGRO
                self.contadorFotogramas = 0
        else:
            if self.contadorFotogramas == 5:
                if self.colorFondo == ROJO:
                    self.colorFondo = NEGRO
                else:
                    self.colorFondo = ROJO
                self.contadorFotogramas = 0
        
        return self.colorFondo

    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.cronometro_p = TIEMPO_MAXIMO_PARTIDA
        
        game_over = False
        self.cronometro.tick()
        while not game_over and self.puntuacion1 < PUNTUACION_GANADORA and self.puntuacion2 < PUNTUACION_GANADORA and self.cronometro_p > 1:
            salto_tiempo = self.cronometro.tick(FPS)
            self.cronometro_p -= salto_tiempo
        #1000 milisegundos/60 fps = 16 ms entre un fotograma y otro
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
        
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.raqueta1.mover(pg.K_a, pg.K_z)
            
            quien = self.bola.mover()
            if quien == "RIGHT":
                self.puntuacion2 += 1            
                print(f"{self.puntuacion1} - {self.puntuacion2}")
            elif quien == "LEFT":
                self.puntuacion1 += 1
                print(f"{self.puntuacion1} - {self.puntuacion2}")
            
            self.bola.comprobar_choque(self.raqueta1, self.raqueta2)

            self.pantalla_principal.fill(self.fijar_fondo())

        #Le pasa la info a la tarjeta gráfica y lo saca por pantalla
            self.bola.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            p1 = self.fuenteMarcador.render(str(self.puntuacion1), True, BLANCO)
            self.pantalla_principal.blit(p1, (20,10))

            p2 = self.fuenteMarcador.render(str(self.puntuacion2), True, BLANCO)
            self.pantalla_principal.blit(p2, (740,10))

            crono = self.fuenteCronometro_p.render(str(self.cronometro_p // 1000), True, BLANCO)
            self.pantalla_principal.blit(crono, (ANCHO // 2, 10))
        
            pg.display.flip()

class Menu:
    def __init__(self, pantalla, cronometro):
        self.pantalla_principal = pantalla
        pg.display.set_caption("Menú")
        self.cronometro = cronometro
        self.imagenFondo = pg.image.load("pong/images/portada.jpeg")
        self.fuenteComenzar = pg.font.Font("pong/fonts/Silkscreen.ttf", 50)
        self.musica = pg.mixer.Sound("pong/sounds/duelo.ogg")

    def bucle_ppal(self):
        game_over = False
        self.musica.play(-1)

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True

            self.pantalla_principal.blit(self.imagenFondo, (0,0))
            menu = self.fuenteComenzar.render("Pulsa ENTER para comenzar", True, MAGENTA)
            self.pantalla_principal.blit(menu, (ANCHO // 2, ALTO - 200))
            pg.display.flip()
        
        self.musica.stop()


