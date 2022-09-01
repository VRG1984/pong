import pygame as pg
from entities import Bola, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("Pong")
cronometro = pg.time.Clock()

game_over = False

bola = Bola(400, 300, color=(255, 255, 255))
bola.vx = 4
bola.vy = 4
raqueta1 = Raqueta(20, 300, w=20, h=120)
raqueta2 = Raqueta(780, 300, w=20, h=120)
raqueta2.vy = 3
raqueta1.vy = 3

while not game_over:
    dt = cronometro.tick(60)
    #1000 milisegundos/60 fps = 16 ms entre un fotograma y otro
    #Eventos que hace el usuario y devuelve una lista de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
        """elif evento.type == pg.KEYDOWN:
            if evento.key == pg.K_DOWN:
                raqueta2.center_y += raqueta2.vy
            elif evento.key == pg.K_UP:
                raqueta2.center_y -= raqueta2.vy"""
    
    # El get_pressed lo que hace es devolver una lista con todas las teclas donde le dice con false o true qué teclas se han pulsado
    
    """Tarea"""
    # Meter esto como método "actualizar" en Raqueta
    raqueta2.mover(pg.K_UP, pg.K_DOWN)
    raqueta1.mover(pg.K_a, pg.K_z)
    bola.mover()
    bola.comprobar_choque(raqueta1, raqueta2)

    pantalla_principal.fill((0, 0, 0))
    #Le pasa la info a la tarjeta gráfica y lo saca por pantalla
    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    
    pg.display.flip()