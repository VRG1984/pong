import pygame as pg
from pong import TIEMPO_MAXIMO_PARTIDA, ANCHO, ALTO
from pong.pantallas import Menu, Partida

class Controlador:
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        cronometro = pg.time.Clock()

        # self.pantallas = [Menu(pantalla_principal, cronometro), Partida(pantalla_principal, cronometro)]
        # Haciéndolo con listas luego podemos pasar de una pantalla a otra en "jugar" utilizando los índices "ix", accediendo a ellas por posición
        
        self.menu = Menu(pantalla_principal, cronometro)
        self.partida = Partida(pantalla_principal, cronometro)

    def jugar(self):
        salida = False
        while not salida: # (== True)
            salida = self.menu.bucle_ppal()
            if salida: #(== True)
                break
            salida = self.partida.bucle_ppal()
            



