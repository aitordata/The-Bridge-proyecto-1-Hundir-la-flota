import numpy as np
import pygame

tablero_maquina=np.full((10,10)," ")
tablero_maquina_vista_usuario=np.full((10,10),"S")
tablero_jugador=tablero_maquina.copy()
esloras_vivas_jugador=20
esloras_vivas_maquina=20
#Los sonidos de acertado y fallado han sido obtenidos del siguiente repositorio: https://github.com/parzibyte/juego_batalla_naval_python/tree/main
sonido_acertado = pygame.mixer.Sound("../sonidos/acertado.wav")
sonido_fallado = pygame.mixer.Sound("../sonidos/fallado.wav")