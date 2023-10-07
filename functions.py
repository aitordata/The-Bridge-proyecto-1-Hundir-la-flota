import numpy as np
import os
from tabulate import tabulate
import time
import pygame

from variables import tablero_jugador,tablero_maquina,tablero_maquina_vista_usuario
from variables import esloras_vivas_jugador,esloras_vivas_maquina
from variables import sonido_acertado,sonido_fallado

def limpiar_consola(): #Limpia la consola
    os.system('clear')
    
def hacer_tabla(tablero, titulo="Tabla"): #Esta funcion se ha realizado con chat gpt, imprime una tabla a partir de un numpy arry
    tablero = list(tablero)
    if len(tablero) != 10 or any(len(fila) != 10 for fila in tablero):
        return
    data = []
    for i in range(10):
        fila = [i]  
        fila.extend(tablero[i])
        data.append(fila)
    headers_x = [""] + list(range(10))  
    print(titulo)
    tabla_final = tabulate(data, headers_x, tablefmt="fancy_grid")
    print(tabla_final)



    
def condicion_no_salir_tabla(eslora,orientacion,x,y): #Función que devuelve True si los barcos no se salen de la tabla y False en caso contrario
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


def condcionante_alrrededor(my_array,x,y):#Comprueba que no hay otro barco alrredor de unas coordenadas x e y.
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
  
def eleguir_orientacion(): #Elige aleatoriamente la orientacion (horizontal=1,vertical=2)
      orientacion= np.random.randint(1,3)
      # horizontal=1 ; vertical=2 
      return orientacion
    
def eleguir_coordenadas(orientación,x,y,eslora): #Pasandole la orientacion, las coordenads iniciales y el tamaño de eslora, devuelve las coordenadas de todas las esloras del barco
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
                      

def colocar_barcos(my_array): #Coloca los barcos aleatoriamente, sin que se solapen, se salgan del tablero o haya otro barco en las posiciones colindantes. 
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
         else:
           continue

def colocar_barcos_manual(tablero_jug): #Colocacion manual de los barcos, proporcionando coordenadas iniciales y orientación
    contador_eslora1=0
    contador_eslora2=0
    contador_eslora3=0
    contador_eslora4=0
    print("Debe introducir las coordenadas (x,y) de la posición inicial del barco, y, en caso de tener más de una eslora, especificar si desea que el barco se coloque horizontalmente (hacia la izquierda) o verticalmente (hacia arriba) a partir de las coordenadas iniciales. Para colocar los barcos manualmente debes tener presente que (1) los barcos no pueden salirse del tablero, (2) no pueden tener otro barco en las coordenadas colindantes y (3) no puede haber más de un barco en la misma posición.")
  
    while contador_eslora1<4:
        try:
            coord_x=int(input("Introduca la coordenada x inicial (barco eslora 1): "))
            coord_y=int(input("Introduca la coordenada y inicial (barco eslora 1): "))
            condicion= condcionante_alrrededor(tablero_jug,coord_x,coord_y)
            if tablero_jug[coord_x][coord_y]==" " and condicion:
                tablero_jug[coord_x][coord_y]="O"
                limpiar_consola()
                print(f"Ha introducido un barco de 1 eslora en la posición ({coord_x,coord_y})")
                hacer_tabla(tablero_jug,"Tabla del jugador")
                contador_eslora1= contador_eslora1+1
            else:
               print("No es posible introducir el barco donde ha especificado, vuelva intentarlo teniendo presente las siguientes instruciones: Para colocar los barcos manualmente debes tener presente que (1) los barcos no pueden salirse del tablero, (2) no pueden tener otro barco en las coordenadas colindantes y (3) no puede haber más de un barco en la misma posición.")
               continue
        except:
          print("Por favor, introduzca un caracter válido.")
            
    while contador_eslora2<3:
        try:
            eslora=2
            orientación_barco_eslora_2=int(input("Posicionar barco eslora 2 horizontalmente (1) o verticalmente (2): "))
            if orientación_barco_eslora_2==1:
                orientación_barco_eslora_2_string="horizontal"
            elif orientación_barco_eslora_2==2:
                orientación_barco_eslora_2_string="vertical"  
            coord_x=int(input("Introduca la coordenada x inicial (barco eslora 2): "))
            coord_y=int(input("Introduca la coordenada y inicial (barco eslora 2): "))
            coord_x2,coord_y2=eleguir_coordenadas(orientación_barco_eslora_2,coord_x,coord_y,eslora)
            condicion1= condcionante_alrrededor(tablero_jug,coord_x,coord_y)
            condicion2=condcionante_alrrededor(tablero_jug,coord_x2,coord_y2)
            condicion_no_salir_var=condicion_no_salir_tabla(eslora,orientación_barco_eslora_2,coord_x,coord_y)
            if tablero_jug[coord_x][coord_y]==" " and tablero_jug[coord_x2][coord_y2]==" " and condicion1 and condicion2 and condicion_no_salir_var:
              tablero_jug[coord_x][coord_y]="O"
              tablero_jug[coord_x2][coord_y2]="O"
              limpiar_consola()
              print(f"Ha introducido un barco de 2 esloras en la posición inicial {coord_x,coord_y}, con orientación {orientación_barco_eslora_2_string}.")
              hacer_tabla(tablero_jug,"Tabla del jugador")
              contador_eslora2= contador_eslora2+1
            else:
              print("No es posible introducir el barco donde ha especificado, vuelva intentarlo teniendo presente las siguientes instruciones: Para colocar los barcos manualmente debes tener presente que (1) los barcos no pueden salirse del tablero, (2) no pueden tener otro barco en las coordenadas colindantes y (3) no puede haber más de un barco en la misma posición.")
              continue
        except:
            print("Por favor, introduzca un caracter válido.")
            
    while contador_eslora3<2:
        try:
            eslora=3
            orientación_barco_eslora_3=int(input("Posicionar barco eslora 3 horizontalmente (1) o verticalmente (2): "))
            if orientación_barco_eslora_3==1:
                    orientación_barco_eslora_3_string="horizontal"
            elif orientación_barco_eslora_3==2:
                    orientación_barco_eslora_3_string="vertical"  
            coord_x=int(input("Introduca la coordenada x inicial (barco eslora 3): "))
            coord_y=int(input("Introduca la coordenada y inicial (barco eslora 3): "))
            coord_x2,coord_y2,coord_x3,coord_y3=eleguir_coordenadas(orientación_barco_eslora_3,coord_x,coord_y,eslora)
            condicion1= condcionante_alrrededor(tablero_jug,coord_x,coord_y)
            condicion2=condcionante_alrrededor(tablero_jug,coord_x2,coord_y2)
            condicion3=condcionante_alrrededor(tablero_jug,coord_x3,coord_y3)
            condicion_no_salir_var=condicion_no_salir_tabla(eslora,orientación_barco_eslora_3,coord_x,coord_y)
            if tablero_jug[coord_x][coord_y]==" " and tablero_jug[coord_x2][coord_y2]==" "and tablero_jug[coord_x3][coord_y3]==" "  and condicion1 and condicion2 and condicion3 and condicion_no_salir_var:
             tablero_jug[coord_x][coord_y]="O"
             tablero_jug[coord_x2][coord_y2]="O"
             tablero_jug[coord_x3][coord_y3]="O"
             limpiar_consola()
             print(f"Ha introducido un barco de 2 esloras en la posición inicial {coord_x,coord_y}, con orientación {orientación_barco_eslora_3_string}.")
             hacer_tabla(tablero_jug,"Tabla del jugador")
             contador_eslora3= contador_eslora3+1
            else:
             print("No es posible introducir el barco donde ha especificado, vuelva intentarlo teniendo presente las siguientes instruciones: Para colocar los barcos manualmente debes tener presente que (1) los barcos no pueden salirse del tablero, (2) no pueden tener otro barco en las coordenadas colindantes y (3) no puede haber más de un barco en la misma posición.")
             continue
        except:
             print("Por favor, introduzca un caracter válido.")
                 
    while contador_eslora4<1:
        try:
            eslora=4
            orientación_barco_eslora_4=int(input("Posicionar barco eslora 3 horizontalmente (1) o verticalmente (2): "))
            if orientación_barco_eslora_4==1:
                    orientación_barco_eslora_4_string="horizontal"
            elif orientación_barco_eslora_4==2:
                    orientación_barco_eslora_4_string="vertical"  
            coord_x=int(input("Introduca la coordenada x inicial (barco eslora 4): "))
            coord_y=int(input("Introduca la coordenada y inicial (barco eslora 4): "))
            coord_x2,coord_y2,coord_x3,coord_y3,coord_x4,coord_y4=eleguir_coordenadas(orientación_barco_eslora_4,coord_x,coord_y,eslora)
            condicion1=condcionante_alrrededor(tablero_jug,coord_x,coord_y)
            condicion2=condcionante_alrrededor(tablero_jug,coord_x2,coord_y2)
            condicion3=condcionante_alrrededor(tablero_jug,coord_x3,coord_y3)
            condicion4=condcionante_alrrededor(tablero_jug,coord_x4,coord_y4)
            condicion_no_salir_var=condicion_no_salir_tabla(eslora,orientación_barco_eslora_4,coord_x,coord_y)
            if tablero_jug[coord_x][coord_y]==" " and tablero_jug[coord_x2][coord_x2]==" "and tablero_jug[coord_x3][coord_y3]==" " and tablero_jug[coord_x4][coord_y4]==" "and condicion1 and condicion2 and condicion3 and condicion4 and condicion_no_salir_var:
             tablero_jug[coord_x][coord_y]="O"
             tablero_jug[coord_x2][coord_y2]="O"
             tablero_jug[coord_x3][coord_y3]="O"
             tablero_jug[coord_x4][coord_y4]="O"
             limpiar_consola()
             print(f"Ha introducido un barco de 2 esloras en la posición inicial {coord_x,coord_y}, con orientación {orientación_barco_eslora_4_string}.")
             hacer_tabla(tablero_jug,"Tabla del jugador")
             contador_eslora4= contador_eslora4+1
            else:
              print("No es posible introducir el barco donde ha especificado, vuelva intentarlo teniendo presente las siguientes instruciones: Para colocar los barcos manualmente debes tener presente que (1) los barcos no pueden salirse del tablero, (2) no pueden tener otro barco en las coordenadas colindantes y (3) no puede haber más de un barco en la misma posición.")
              continue
        except:
         print("Por favor, introduzca un caracter válido.")

def comprobar_esloras_alrrededor_barco_hundido(my_array,x,y): #Recibe como parametro las coordenadas de una eslora hundida, y evalua si hay más esloras a su alrrededor, cambiando "X" por "!" en caso de que las haya.
    if len(my_array)-1==x and len(my_array)-1==y:
         condicion=(my_array[x][y-1]=="X") or (my_array[x-1][y-1]=="X") or (my_array[x-1][y]=="X")
         print("1")
         if my_array[x][y-1]=="X":
          my_array[x][y-1]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x,y-1)
          if my_array[x-1][y-1]=="X":
             my_array[x-1][y-1]="!"
             comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y-1)
          if my_array[x-1][y]=="X":
             my_array[x-1][y]="!"
             comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y)
         return condicion
    elif len(my_array)-1>x and len(my_array)-1==y and x!=0:
         condicion=(my_array[x-1][y]=="X")or (my_array[x-1][y-1]=="X")or(my_array[x][y-1]=="X")or(my_array[x+1][y]=="X")
         print("2")
         if my_array[x-1][y]=="X":
          my_array[x-1][y]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y)
         if my_array[x-1][y-1]=="X":
          my_array[x-1][y-1]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y-1)
         if my_array[x][y-1]=="X":
          my_array[x][y-1]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x,y-1)
         if my_array[x+1][y]=="X":
          my_array[x+11][y]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x+1,y) 
         return condicion 
    elif 0==x and len(my_array)-1==y:
         condicion= (my_array[x][y-1]=="X")or(my_array[x+1][y-1]=="X")or(my_array[x+1][y]=="X")
         if my_array[x][y-1]=="X":
          my_array[x][y-1]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x,y-1)
         if my_array[x+1][y]=="X":
          my_array[x+1][y]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x+1,y) 
         if my_array[x+1][y-1]=="X":
          my_array[x+1][y-1]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x+1,y-1) 
         print("3")
         return condicion
    elif len(my_array)-1==x and y< len(my_array)-1:
          condicion= (my_array[x][y+1]=="X")or(my_array[x-1][y]=="X")or(my_array[x-1][y+1]=="X")or(my_array[x][y-1]=="X")or(my_array[x-1][y-1]=="X")
          print(4)
          if my_array[x][y+1]=="X":
              my_array[x][y+1]="!"
              comprobar_esloras_alrrededor_barco_hundido(my_array,x,y+1)
          if my_array[x-1][y]=="X":
              my_array[x-1][y]="!"
              comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y)
          if my_array[x-1][y+1]=="X":
             my_array[x-1][y+1]="!"
             comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y+1)
          if my_array[x][y-1]=="X":
              my_array[x][y-1]="!"
              comprobar_esloras_alrrededor_barco_hundido(my_array,x,y-1)
          if my_array[x-1][y-1]=="X":
            my_array[x-1][y-1]="!"
            comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y-1)
    else:
      condicion= (my_array[x-1][y]=="X")or(my_array[x-1][y+1]=="X")or(my_array[x][y+1]=="X")or(my_array[x+1][y-1]=="X")or(my_array[x+1][y+1]=="X")or (my_array[x+1][y]=="X")or (my_array[x][y-1]=="X")or(my_array[x-1][y-1]=="X")
      print(5)
      if my_array[x-1][y]=="X":
          my_array[x-1][y]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y)
          
      if my_array[x-1][y+1]=="X":
          my_array[x-1][y+1]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y+1)
          
      if my_array[x][y+1]=="X":
              my_array[x][y+1]="!"
              comprobar_esloras_alrrededor_barco_hundido(my_array,x,y+1)
              
      if my_array[x+1][y-1]=="X":
          my_array[x+1][y-1]="!"
          comprobar_esloras_alrrededor_barco_hundido(my_array,x+1,y-1) 
          
      if my_array[x+1][y+1]=="X":
            my_array[x+1][y+1]="!"
            comprobar_esloras_alrrededor_barco_hundido(my_array,x+1,y+1)
            
      if my_array[x+1][y]=="X":
           my_array[x+1][y]="!"
           comprobar_esloras_alrrededor_barco_hundido(my_array,x+1,y)
           
      if my_array[x][y-1]=="X":
           my_array[x][y-1]="!"
           comprobar_esloras_alrrededor_barco_hundido(my_array,x,y-1)
           return condicion
      if my_array[x-1][y-1]=="X":
            my_array[x-1][y-1]="!"
            comprobar_esloras_alrrededor_barco_hundido(my_array,x-1,y-1)
              
      return condicion    
def sonido_disparo_acertado_play(): #Reproduce el sonido de acierto
  pygame.mixer.Sound.play(sonido_acertado)   
      
def sonido_disparo_fallado_play(): #Reproduce el sonido de fallo
  pygame.mixer.Sound.play(sonido_fallado)   
          
def disparo_usuario(tablero,tablero_oculto,esloras_vivas_maquina,tablerojug): #Disparo del usuario introduciendo coordenadas
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
            sonido_disparo_acertado_play()
            time.sleep(1)
            barco_hundido=comprobar_barco_hundido(tablero,coord_x,coord_y)
            if barco_hundido:
              tablero[coord_x, coord_y] = "!"
              tablero_oculto[coord_x, coord_y] = "!"
              comprobar_esloras_alrrededor_barco_hundido(tablero,coord_x,coord_y)
              print("Barco hundido!")
            limpiar_consola()
           elif tablero[coord_x, coord_y] == " ":
            tablero[coord_x, coord_y] = "-"
            tablero_oculto[coord_x, coord_y] = "-"
            limpiar_consola()
            print("Has fallado!")
            sonido_disparo_fallado_play()
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
                 
def disparo_maquina(tablero,esloras_vivas_jugador,tablero_oculto): #Disparo de la máquina con coordenadas aleatorias
        while True: 
                coord_x = np.random.randint(0, 10)
                coord_y = np.random.randint(0, 10)
                if tablero[coord_x, coord_y] == "O":
                 tablero[coord_x, coord_y] = "X"
                 esloras_vivas_jugador-=1
                 limpiar_consola()
                 print(f"La máquina ha acertado en las coordenadas {coord_x,coord_y}")
                 sonido_disparo_acertado_play()
                 time.sleep(1)
                 barco_hundido=comprobar_barco_hundido(tablero,coord_x,coord_y)
                 if barco_hundido:
                  tablero[coord_x, coord_y] = "!"
                  tablero_oculto[coord_x, coord_y] = "!"
                  comprobar_esloras_alrrededor_barco_hundido(tablero,coord_x,coord_y)
                  print("Barco hundido!")
                  time.sleep(1)
                elif tablero[coord_x, coord_y] == " ":
                 tablero[coord_x, coord_y] = "-"
                 limpiar_consola()
                 sonido_disparo_fallado_play()
                 print("La máquina ha fallado!, es tu turno!")
                 break
                elif tablero[coord_x, coord_y] == "X":
                 continue
                elif tablero[coord_x, coord_y] == "-":
                 continue
         
def bienvenida_y_dificultad(): #Pregunta la dificultad deseada
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
         
def preguntar_colocar_barcos_manual(): #Pregunta si desea colocar los barcos manuelmente
   try: 
     colocar_barcos_manual= int(input("Pulse 1 si desea un tablero aleatorio o 2 si prefiere introducir los barcos manualmente: "))
     if colocar_barcos_manual==1:
       return False
     elif colocar_barcos_manual==2:
       return True
     else:
       print("Por favor, introduzca un input válido")
       preguntar_colocar_barcos_manual()
   except:
     print("Por favor introduzca un input válido.")