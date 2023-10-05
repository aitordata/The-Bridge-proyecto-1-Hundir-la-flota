![Hundir la flota](./img/hundir-la-flota-juego-de-mesa.jpg)
![Bridge](./img/bridge.png)

# Proyecto 1: Hundir la flota

## Resumen

#### El presente programa es una versión simplificada del juego **Hundir la flota**. Hay dos jugadores: el usuario y la máquina. El juego consiste en hundir todos los barcos del adversario, gana el primero en conseguirlo.

## Aspectos clave del programa

- #### Los barcos se colocaran aleatoriamente en el tablero (10x10).
- #### Los disparos se realizan introduciendo las coordenadas **x** e **y**
- #### Si se acierta el disparo, se dispara de nuevo.
- #### Se podrá eleguir entre tres niveles de dificultad, la cual está proporcionalmente relacionada con la cantidad de disparos que realiza la máquina por cada turno del usuario.

## Posibles estados del tablero

#### A lo largo de la partida el usuario verá dos tablas: la suya y la de la máquina (oculta). Cada posición de la tabla puede tener diferentes estados, repesentados por difentes caracteres:

- ### "S": Tablero en modo oculto
- ### " ": Agua
- ### "-": Disparo realizado en Agua
- ### "O": Eslora de barco
- ### "X": Disparo realizado en eslora
- ### "!": Barco hundido
