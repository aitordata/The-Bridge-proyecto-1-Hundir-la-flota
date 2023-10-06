import numpy as np
from tabulate import tabulate
import os
import platform

my_array=np.array([[" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "," "," "],
               ]  
)

def limpiar_consola():
    sistema_operativo = platform.system()
    if sistema_operativo == 'Windows':
        os.system('cls')
    else:
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





def colocar_barcos_manual(tablero_jug):
    contador_eslora1=0
    contador_eslora2=0
    contador_eslora3=0
    contador_eslora4=0
    print("Debe introducir las coordenadas (x,y) de la posición inicial del barco, y, en caso de tener más de una eslora, especificar si desea que el barco se coloque horizontalmente (hacia la izquierda) o verticalmente (hacia arriba) a partir de las coordenadas iniciales. Para colocar los barcos manualmente debes tener presente que (1) los barcos no pueden salirse del tablero, (2) no pueden tener otro barco en las coordenadas colindantes y (3) no puede haber más de un barco en la misma posición.")
  
   # while contador_eslora1<4:
       # try:
           # coord_x=int(input("Introduca la coordenada x inicial (barco eslora 1): "))
            #coord_y=int(input("Introduca la coordenada y inicial (barco eslora 1): "))
            #condicion= condcionante_alrrededor(tablero_jug,coord_x,coord_y)
          #  if tablero_jug[coord_x][coord_y]==" " and condicion:
             #   tablero_jug[coord_x][coord_y]="O"
              #  limpiar_consola()
              #  print(f"Ha introducido un barco de 1 eslora en la posición ({coord_x,coord_y})")
              #  hacer_tabla(tablero_jug,"Tabla del jugador")
              #  contador_eslora1= contador_eslora1+1
            #else:
             #   print("No es posible introducir el barco donde ha especificado, vuelva intentarlo teniendo presente las siguientes instruciones: Para colocar los barcos manualmente debes tener presente que (1) los barcos no pueden salirse del tablero, (2) no pueden tener otro barco en las coordenadas colindantes y (3) no puede haber más de un barco en la misma posición.")
              #  continue
       # except:
         #  print("Por favor, introduzca un caracter válido.")
            
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
        
        
colocar_barcos_manual(my_array)
print(my_array)
     