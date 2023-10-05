import numpy as np
import os
from tabulate import tabulate
import time

tablero_maquina=np.full((10,10)," ")
tablero_maquina_vista_usuario=np.full((10,10),"S")
tablero_jugador=tablero_maquina.copy()
esloras_vivas_jugador=20
esloras_vivas_maquina=20

def limpiar_consola():
    os.system('clear')
    
def hacer_tabla(tablero, titulo="Tabla"): #Esta funcion se ha realizado con chat gpt
    tablero = list(tablero)
    
    # Verificar que el tablero tenga 10 filas y 10 columnas
    if len(tablero) != 10 or any(len(fila) != 10 for fila in tablero):
        return

    # Crear una lista de listas que contenga los datos y los encabezados
    data = []
    for i in range(10):
        fila = [i]  # Agregar el encabezado en el eje Y (fila)
        fila.extend(tablero[i])
        data.append(fila)

    # Encabezados de la tabla
    headers_x = [""] + list(range(10))  # Encabezados en el eje X (columna)

    # Imprimir el título
    print(titulo)

    # Imprimir la tabla en la consola
    tabla_final = tabulate(data, headers_x, tablefmt="fancy_grid")

    # Imprimir el encabezado en el eje X y la tabla
    print(tabla_final)



    
def condicion_no_salir_tabla(eslora,orientacion,x,y):
    if eslora==2:
        if orientacion==1 and y==0:
            return False
        elif orientacion==2 and x==0:
            return False
        else:
            return True
    elif eslora==3:
        if orientacion==1 and (y==0 or y==1):
            return False
        elif orientacion==2 and (x==0 or x==2):
            return False
        else:
            return True
    elif eslora==4:
        if orientacion==1 and (y==0 or y==1 or y==2):
            return False
        elif orientacion==2 and (x==0 or x==1 or x==2):
            return False
        else:
            return True
          
def comprobar_barco_hundido(my_array,x,y): #Devuelve True cuando el barco no tiene esloras vivas alrrededor -es decir, se ha hundido- y false en caso contrario.
    if len(my_array)-1==x and len(my_array)-1==y:
         condicion=(my_array[x][y-1]!="O") and (my_array[x-1][y-1]!="O") and (my_array[x-1][y]!="O")
         return condicion
    elif len(my_array)-1>x and len(my_array)-1==y and x!=0:
         condicion=(my_array[x-1][y]!="O")and (my_array[x-1][y-1]!="O")and(my_array[x][y-1]!="O")and(my_array[x+1][y]!="O")
         return condicion 
    elif 0==x and len(my_array)-1==y:
         condicion= (my_array[x][y-1]!="O")and (my_array[x+1][y-1]!="O")and (my_array[x+1][y]!="O")
         return condicion
    elif len(my_array)-1==x and y< len(my_array)-1:
          condicion= (my_array[x][y+1]!="O")and (my_array[x-1][y]!="O")and (my_array[x-1][y+1]!="O")and (my_array[x][y-1]!="O")and (my_array[x-1][y-1]!="O")
          return condicion
    else:
      condicion= (my_array[x-1][y]!="O") and (my_array[x-1][y+1]!="O") and (my_array[x][y+1]!="O") and (my_array[x+1][y-1]!="O") and (my_array[x+1][y+1]!="O") and (my_array[x+1][y]!="O") and (my_array[x][y-1]!="O") and (my_array[x-1][y-1]!="O")
      return condicion


def condcionante_alrrededor(my_array,x,y):
    if len(my_array)-1==x and len(my_array)-1==y:
         condicion=(my_array[x][y-1]==" ") and (my_array[x-1][y-1]==" ") and (my_array[x-1][y]==" ")
         return condicion
    elif len(my_array)-1>x and len(my_array)-1==y and x!=0:
         condicion=(my_array[x-1][y]==" ")and (my_array[x-1][y-1]==" ")and(my_array[x][y-1]==" ")and(my_array[x+1][y]==" ")
         return condicion 
    elif 0==x and len(my_array)-1==y:
         condicion= (my_array[x][y-1]==" ")and (my_array[x+1][y-1]==" ")and (my_array[x+1][y]==" ")
         return condicion
    elif len(my_array)-1==x and y< len(my_array)-1:
          condicion= (my_array[x][y+1]==" ")and (my_array[x-1][y]==" ")and (my_array[x-1][y+1]==" ")and (my_array[x][y-1]==" ")and (my_array[x-1][y-1]==" ")
          return condicion
    else:
      condicion= (my_array[x-1][y]==" ") and (my_array[x-1][y+1]==" ") and (my_array[x][y+1]==" ") and (my_array[x+1][y-1]==" ") and (my_array[x+1][y+1]==" ") and (my_array[x+1][y]==" ") and (my_array[x][y-1]==" ") and (my_array[x-1][y-1]==" ")
      return condicion
  
def eleguir_orientacion():
      orientacion= np.random.randint(1,3)
      # horizontal=1 ; vertical=2 
      return orientacion
    
def eleguir_coordenadas(orientación,x,y,eslora):
        if eslora ==2:
         if orientación==1:
                 coordenada_x=x
                 coordenada_y=y-1
                 return [coordenada_x,coordenada_y]
         elif orientación==2:
                coordenada_x=x-1
                coordenada_y=y
                return [coordenada_x,coordenada_y]
        if eslora ==3:
         if orientación==1:
                 coordenada_x=x
                 coordenada_y=y-1
                 coordenada_x2=x
                 coordenada_y2=y-2
                 return [coordenada_x,coordenada_y,coordenada_x2,coordenada_y2]
         elif orientación==2:
                coordenada_x=x-1
                coordenada_y=y
                coordenada_x2=x-2
                coordenada_y2=y
                return [coordenada_x,coordenada_y,coordenada_x2,coordenada_y2]
        if eslora ==4:
         if orientación==1:
                 coordenada_x=x
                 coordenada_y=y-1
                 coordenada_x2=x
                 coordenada_y2=y-2
                 coordenada_x3=x
                 coordenada_y3=y-3
                 return [coordenada_x,coordenada_y,coordenada_x2,coordenada_y2,coordenada_x3,coordenada_y3]
         elif orientación==2:
                coordenada_x=x-1
                coordenada_y=y
                coordenada_x2=x-2
                coordenada_y2=y
                coordenada_x3=x-3
                coordenada_y3=y
                return [coordenada_x,coordenada_y,coordenada_x2,coordenada_y2,coordenada_x3,coordenada_y3]
                      

def colocar_barcos(my_array):
     contador_eslora1=0
     contador_eslora2=0
     contador_eslora3=0
     contador_eslora4=0
     while contador_eslora1<4:
        x=np.random.randint(0,10)
        y=np.random.randint(0,10)
        condicion= condcionante_alrrededor(my_array,x,y)
        if my_array[x][y]==" " and condicion:
          my_array[x][y]="O"
          contador_eslora1= contador_eslora1+1
        else:
         continue
     while contador_eslora2<3:
        eslora=2
        orientación_barco_eslora_2=eleguir_orientacion()
        x=np.random.randint(0,10)
        y=np.random.randint(0,10)
        coordenada_x,coordenada_y=eleguir_coordenadas(orientación_barco_eslora_2,x,y,eslora)
        condicion1= condcionante_alrrededor(my_array,x,y)
        condicion2=condcionante_alrrededor(my_array,coordenada_x,coordenada_y)
        condicion_no_salir_var=condicion_no_salir_tabla(eslora,orientación_barco_eslora_2,x,y)
        if my_array[x][y]==" " and my_array[coordenada_x][coordenada_y]==" " and condicion1 and condicion2 and condicion_no_salir_var:
          my_array[x][y]="O"
          my_array[coordenada_x][coordenada_y]="O"
          contador_eslora2= contador_eslora2+1
        else:
         continue
     while contador_eslora3<2:
        eslora=3
        orientación_barco_eslora_3=eleguir_orientacion()
        x=np.random.randint(0,10)
        y=np.random.randint(0,10)
        coordenada_x,coordenada_y,coordenada_x2,coordenada_y2=eleguir_coordenadas(orientación_barco_eslora_3,x,y,eslora)
        condicion1= condcionante_alrrededor(my_array,x,y)
        condicion2=condcionante_alrrededor(my_array,coordenada_x,coordenada_y)
        condicion3=condcionante_alrrededor(my_array,coordenada_x2,coordenada_y2)
        condicion_no_salir_var=condicion_no_salir_tabla(eslora,orientación_barco_eslora_3,x,y)
        if my_array[x][y]==" " and my_array[coordenada_x][coordenada_y]==" "and my_array[coordenada_x2][coordenada_y2]==" "  and condicion1 and condicion2 and condicion3 and condicion_no_salir_var:
          my_array[x][y]="O"
          my_array[coordenada_x][coordenada_y]="O"
          my_array[coordenada_x2][coordenada_y2]="O"
          contador_eslora3= contador_eslora3+1
        else:
         continue
     while contador_eslora4<1:
         eslora=4
         orientación_barco_eslora_4=eleguir_orientacion()
         x=np.random.randint(0,10)
         y=np.random.randint(0,10)
         coordenada_x,coordenada_y,coordenada_x2,coordenada_y2,coordenada_x3,coordenada_y3=eleguir_coordenadas(orientación_barco_eslora_4,x,y,eslora)
         condicion1= condcionante_alrrededor(my_array,x,y)
         condicion2=condcionante_alrrededor(my_array,coordenada_x,coordenada_y)
         condicion3=condcionante_alrrededor(my_array,coordenada_x2,coordenada_y2)
         condicion4=condcionante_alrrededor(my_array,coordenada_x3,coordenada_y3)
         condicion_no_salir_var=condicion_no_salir_tabla(eslora,orientación_barco_eslora_4,x,y)
         if my_array[x][y]==" " and my_array[coordenada_x][coordenada_y]==" "and my_array[coordenada_x2][coordenada_y2]==" " and my_array[coordenada_x3][coordenada_y3]==" "and condicion1 and condicion2 and condicion3 and condicion4 and condicion_no_salir_var:
          my_array[x][y]="O"
          my_array[coordenada_x][coordenada_y]="O"
          my_array[coordenada_x2][coordenada_y2]="O"
          my_array[coordenada_x3][coordenada_y3]="O"
          contador_eslora4= contador_eslora4+1
          
def disparo_usuario(tablero,tablero_oculto,esloras_vivas_maquina,tablerojug):
        limpiar_consola() 
        time.sleep(2)
        hacer_tabla(tablerojug, "Tablero del jugador")
        hacer_tabla(tablero_oculto,"Tablero de la máquina")
        coord_x=int
        coord_y=int
        while True: 
         try:
           coord_x = int(input('Introduzca coordenada x (-1 para salir del juego):'))
           if coord_x==-1:
             break
           coord_y = int(input('Introduzca coordenada y (-1 para salir del juego):'))
           if coord_y==-1:
             break 
           if (coord_x<-1) or (coord_x>9) or (coord_y<-1) or (coord_y>9):
            print("Por favor, introduzca un caracter válido. Recuerde que las coordenadas sólo pueden tomar valores desde el 0 al 9.")
            continue
           if tablero[coord_x, coord_y] == "O":
            tablero[coord_x, coord_y] = "X"
            tablero_oculto[coord_x, coord_y] = "X"
            esloras_vivas_maquina-=1
            print("Has acertado!")
            barco_hundido=comprobar_barco_hundido(tablero,coord_x,coord_y)
            if barco_hundido:
              tablero[coord_x, coord_y] = "!"
              tablero_oculto[coord_x, coord_y] = "!"
              print("Barco hundido!")
            limpiar_consola()
           elif tablero[coord_x, coord_y] == " ":
            tablero[coord_x, coord_y] = "-"
            tablero_oculto[coord_x, coord_y] = "-"
            limpiar_consola()
            print("Has fallado!")
            break
           elif tablero[coord_x, coord_y] == "X":
            print("Disparo previamente realizado!")
           elif tablero[coord_x, coord_y] == "-":
            print("Disparo previamente realizado!")
              
         except:
          print("Por favor, introduzca un caracter válido. Recuerde que las coordenadas sólo pueden tomar valores desde el 0 al 9.")
        if coord_x==-1 or coord_y==-1:
          return False
        else: 
          return True
                 
def disparo_maquina(tablero,esloras_vivas_jugador,tablero_oculto):
        while True: 
                coord_x = np.random.randint(0, 10)
                coord_y = np.random.randint(0, 10)
                if tablero[coord_x, coord_y] == "O":
                 tablero[coord_x, coord_y] = "X"
                 esloras_vivas_jugador-=1
                 limpiar_consola()
                 print("La máquina ha acertado!")
                 barco_hundido=comprobar_barco_hundido(tablero,coord_x,coord_y)
                 if barco_hundido:
                  tablero[coord_x, coord_y] = "!"
                  tablero_oculto[coord_x, coord_y] = "!"
                  print("Barco hundido!")
                elif tablero[coord_x, coord_y] == " ":
                 tablero[coord_x, coord_y] = "-"
                 limpiar_consola()
                 print("La máquina ha fallado!, es tu turno!")
                 break
                elif tablero[coord_x, coord_y] == "X":
                 continue
                elif tablero[coord_x, coord_y] == "-":
                 continue
         
def bienvenida_y_dificultad():
    print("Bienvenido al juego Hundir la flota, las reglas son blablabla")
    while True:
     try:
      dificultad=int(input("Por favor, eliga la dificultad (1:normal,2:dificil,3:muy dificil): "))
      if dificultad==1:
        return dificultad
      elif dificultad==2:
        return dificultad
      elif dificultad==3:
        return dificultad
      else: 
          print("Por favor, introduzca un número del 1 al 3.")
     except:
         print("Por favor,introduzca un número del 1 al 3.")

def empezar_hundir_la_flota(esloras_vivas_jugador,esloras_vivas_maquina,tablero_maquina_vista_usuario):
  
    limpiar_consola()
    
    dificultad=bienvenida_y_dificultad()
    
    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)
    
    if dificultad==1: 
        while esloras_vivas_jugador>0 and esloras_vivas_maquina>0:            
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
    elif esloras_vivas_jugador==0:
     print("La máquina ha ganado, intentalo de nuevo!")
     
def salir_hundir_la_flota():
     print("Has salido de Hundir la flota, vuelve pronto!")
     
     
     
    
        
        

    
    

        

