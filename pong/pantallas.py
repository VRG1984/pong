import pygame as pg
from pong.entities import Bola, Raqueta
from pong import ALTO, ANCHO, AMARILLO, BLANCO, NEGRO, FPS

pg.init()

class Partida:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Pong")
        self.cronometro = pg.time.Clock()

        self.bola = Bola(ANCHO // 2, ALTO //2, color = BLANCO)
        self.raqueta1 = Raqueta(20, ALTO // 2, w=20, h=120, color = AMARILLO)
        self.raqueta1.vy = 5
        self.raqueta2 = Raqueta(ANCHO - 20, ALTO // 2, w=20, h=120, color = AMARILLO)
        self.raqueta2.vy = 5
        
        self.puntuacion1 = 0
        self.puntuacion2 = 0

        self.fuenteMarcador = pg.font.Font("pong/fonts/Silkscreen.ttf", 40)

    
    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5
        
        game_over = False

        while not game_over and self.puntuacion1 < 10 and self.puntuacion2 < 10:
            self.cronometro.tick(FPS)
        #1000 milisegundos/60 fps = 16 ms entre un fotograma y otro
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
        
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

            self.pantalla_principal.fill(NEGRO)
        #Le pasa la info a la tarjeta gráfica y lo saca por pantalla
            self.bola.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            p1 = self.fuenteMarcador.render(str(self.puntuacion1), True, BLANCO)
            self.pantalla_principal.blit(p1, (20,10))

            p2 = self.fuenteMarcador.render(str(self.puntuacion2), True, BLANCO)
            self.pantalla_principal.blit(p2, (740,10))
        
            pg.display.flip()