import numpy as np

tablero_maquina=np.full((10,10)," ")
tablero_maquina_vista_usuario=np.full((10,10),"S")
tablero_jugador=tablero_maquina.copy()
esloras_vivas_jugador=20
esloras_vivas_maquina=20