import time
from functions import bienvenida_y_dificultad,preguntar_colocar_barcos_manual,colocar_barcos,colocar_barcos_manual
from functions import disparo_usuario,disparo_maquina,contador_esloras_vivas
from functions import limpiar_consola
from functions import esloras_vivas_jugador,esloras_vivas_maquina
from functions import tablero_maquina_vista_usuario,tablero_jugador,tablero_maquina
from functions import sonido_victoria_play,sonido_derrota_play

     

def empezar_hundir_la_flota(esloras_vivas_jugador,esloras_vivas_maquina,tablero_maquina_vista_usuario,tablero_jugador): #Estructura del juego
    limpiar_consola()
    dificultad=bienvenida_y_dificultad()
    colocar_barcos_manual_var=preguntar_colocar_barcos_manual()
    if colocar_barcos_manual_var:
     colocar_barcos(tablero_maquina)
     colocar_barcos_manual(tablero_jugador)
    else:
      colocar_barcos(tablero_maquina)
      colocar_barcos(tablero_jugador)
    esloras_vivas_maquina= 20
    if dificultad==1: 
        while esloras_vivas_jugador>0 and esloras_vivas_maquina>0:  
         esloras_vivas_maquina=contador_esloras_vivas(tablero_maquina)        
         jugar=disparo_usuario(tablero_maquina,tablero_maquina_vista_usuario,esloras_vivas_maquina,tablero_jugador)
         if jugar==False:
           break
         time.sleep(2)
         disparo_maquina(tablero_jugador,esloras_vivas_jugador, tablero_maquina_vista_usuario)
         time.sleep(2)  
    elif dificultad==2:
        while esloras_vivas_jugador>0 and esloras_vivas_maquina>0:                
         jugar=disparo_usuario(tablero_maquina,tablero_maquina_vista_usuario,esloras_vivas_maquina,tablero_jugador)
         if jugar==False:
           break
         time.sleep(2)
         disparo_maquina(tablero_jugador,esloras_vivas_jugador, tablero_maquina_vista_usuario)
         time.sleep(2)
         disparo_maquina(tablero_jugador,esloras_vivas_jugador, tablero_maquina_vista_usuario)
         time.sleep(2) 
    elif dificultad==3:
         while esloras_vivas_jugador>0 and esloras_vivas_maquina>0:             
          jugar=disparo_usuario(tablero_maquina,tablero_maquina_vista_usuario,esloras_vivas_maquina,tablero_jugador)
          if jugar==False:
           break
          time.sleep(2)
          disparo_maquina(tablero_jugador,esloras_vivas_jugador, tablero_maquina_vista_usuario)
          time.sleep(2)
          disparo_maquina(tablero_jugador,esloras_vivas_jugador, tablero_maquina_vista_usuario)
          time.sleep(2)
          disparo_maquina(tablero_jugador,esloras_vivas_jugador, tablero_maquina_vista_usuario)
          time.sleep(2)  
    if esloras_vivas_maquina==0:
     print("Felicidades, has ganado!")
     sonido_victoria_play()
    elif esloras_vivas_jugador==0:
     print("La máquina ha ganado, intentalo de nuevo!")
     sonido_derrota_play()
    else:
      print("Has salido del juego Hundir la flota, vuelve pronto.")
      
empezar_hundir_la_flota(esloras_vivas_jugador,esloras_vivas_maquina,tablero_maquina_vista_usuario,tablero_jugador)
     
    
        