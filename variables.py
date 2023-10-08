import numpy as np
import pygame
import os

tablero_maquina=np.full((10,10)," ")
tablero_maquina_vista_usuario=np.full((10,10),"S")
tablero_jugador=tablero_maquina.copy()
esloras_vivas_jugador=20
esloras_vivas_maquina=20
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "sí"
pygame.init()
pygame.mixer.init()
#Los sonidos de acertado y fallado han sido obtenidos del siguiente repositorio: https://github.com/parzibyte/juego_batalla_naval_python/tree/main
sonido_acertado= pygame.mixer.Sound("sonidos/acertado.wav")
sonido_fallado= pygame.mixer.Sound("sonidos/fallado.wav")
sonido_victoria= pygame.mixer.Sound("sonidos/victoria.wav")
sonido_derrota=pygame.mixer.Sound("sonidos/derrota.wav")