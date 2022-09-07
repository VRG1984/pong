import pygame as pg
import random


class Bola:
    def __init__(self, center_x, center_y, radio=10, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.radio = radio
        self.color = color

        # El "self." + "" es como vas a llamar tú al atributo/variable de cada objeto.
        # Lo normal es que el "" coincida con los nombres de los atributos/variables inicializadores del init, pero pueden ser distintos.
    
        self.vx = 0
        self.vy = 0

    def dibujar(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.center_x, self.center_y), self.radio)
    
    def mover(self, x_max = 800, y_max = 600):

        self.center_x += self.vx
        self.center_y += self.vy

        if self.center_y >= y_max -self.radio or self.center_y < self.radio:
            self.vy = self.vy * -1
        
        # Funcionamiento de rebotes arriba y abajo
        
        if self.center_x >= x_max:
            self.center_x = x_max // 2
            self.center_y = y_max // 2
            self.vx *= -1
            self.vy = random.randint(-4, -1)
        
            return "LEFT"

        if self.center_x <= 0:
            self.center_x = x_max // 2
            self.center_y = y_max // 2
            self.vx *= -1
            self.vy = random.randint(-4, -1)
        
            return "RIGHT"
        
        # Funcionamiento de goles

    def comprobar_choque(self, *raquetas):
        for raqueta_activa in raquetas:
            
            if  self.izquierda <= raqueta_activa.derecha and \
                self.derecha >= raqueta_activa.izquierda and \
                self.arriba <= raqueta_activa.abajo and \
                self.abajo >= raqueta_activa.arriba:
                
                    self.vx = self.vx * -1

    @property
    def izquierda(self):
        return self.center_x - self.radio
    
    @property
    def derecha(self):
        return self.center_x + self.radio
    
    @property
    def arriba(self):
        return self.center_y - self.radio
    
    @property
    def abajo(self):
        return self.center_y + self.radio
    

class Raqueta:
    imagenes = {
        "izqda": "electric00.png",
        "drcha": "electric00d.png"
    }
    
    def __init__(self, center_x, center_y, w=20, h=120, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.w = w
        self.h = h
    
        self.vx = 0
        self.vy = 0

        self._imagen = pg.image.load(f"pong/images/{self.imagenes['izqda']}")
    
    @property
    def imagen(self):
        return self._imagen
    
    @imagen.setter
    def imagen(self, valor):
        self._imagen = pg.image.load(f"pong/images/{self.imagenes[valor]}")


    def dibujar(self, pantalla):
        # pg.draw.rect(pantalla, self.color, (self.center_x - self.w//2, self.center_y - self.h//2, self.w, self.h))
        pantalla.blit(self.imagen, (self.center_x - self.w//2, self.center_y - self.h//2, self.w, self.h))

    def mover(self, tecla_arriba, tecla_abajo, y_max=600):
        estado_teclas = pg.key.get_pressed()
        # Este método devuelve una lista con las teclas pulsadas (¿diccionario de todas las teclas con "True-False"?)

        if estado_teclas[tecla_arriba]: #Movimiento hacia arriba
            self.center_y -= self.vy
        if self.center_y < self.h // 2:
            self.center_y = self.h // 2
        
        if estado_teclas[tecla_abajo]: # Movimiento hacia abajo
            self.center_y += self.vy
        if self.center_y > y_max - self.h // 2:
            self.center_y = y_max - self.h // 2
    
    @property #Para ahorrarte el paréntesis y hacer pasar el método por un atributo  
    def izquierda(self):
        return self.center_x - self.w // 2
    
    @property
    def derecha(self):
        return self.center_x + self.w // 2    
    @property
    def arriba(self):
        return self.center_y - self.h // 2
    
    @property
    def abajo(self):
        return self.center_y + self.h // 2

    