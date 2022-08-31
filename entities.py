import pygame as pg
import random


class Bola:
    def __init__(self, center_x, center_y, radio=10, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.radio = radio
        self.color = color
    
        self.vx = 0
        self.vy = 0

    def dibujar(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.center_x, self.center_y), self.radio)
    
    def mover(self, x_max = 800, y_max = 600):
        self.center_x += self.vx
        self.center_y += self.vy

        if self.center_y >= y_max -self.radio or self.center_y < self.radio:
            self.vy = self.vy * -1
        
        if self.center_x >= x_max or self.center_x <= 0: #Se cuela por la dere
            self.center_x = x_max // 2
            self.center_y = y_max // 2

            #Hacer un random en el eje y para que la bola salga con distinta inclinación
            self.vx *= -1
            self.vy = random.randint(-4, -1)

    @property #Para ahorrarte el paréntesis y hacer pasar el método por un atributo  
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
    def __init__(self, center_x, center_y, w=20, h=120, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.w = w
        self.h = h
    
        self.vx = 0
        self.vy = 0

    def dibujar(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.center_x - self.w//2, self.center_y - self.h//2, self.w, self.h))

    def mover(self, tecla_arriba, tecla_abajo, y_max=600):
        estado_teclas = pg.key.get_pressed()
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

    