# Mini Proyecto - Sistemas Inteligentes
# Cubo Rubik
<div align="center">
  <img src="./img/cubo.png" alt="Logo" width="130" height="130">
</div>
## Nombre del Autor:

- Jonatan Gerson Terceros Ortega

## Descripcion del Proyecto
- Este es un mini proyecto de la materia de sistemas inteligentes que consiste en desarrollar un programa capaz de resolver un cubo rubik, utilizando algoritmos de busqueda en espacio de estados.
- El Cubo Rubik es un rompecabezas cúbico que consta de piezas rotativas. El objetivo del juego es conseguir que cada una de las seis caras del cubo esté compuesta por nueve cuadrados del mismo color.

## Requerimientos del entorno de programación

- El unico requerimineto es tener instalado python.

## Manual de uso

### Formato de codificación para cargar el estado de un cubo desde el archivo de texto

- El formato para cargar el estado de un cubo  desde el archivo de texto es el siguiente:

                                    W,W,W,W,W,W,W,W,W
                                    Y,Y,Y,Y,Y,Y,Y,Y,Y
                                    O,O,O,O,O,O,O,O,O
                                    R,R,R,R,R,R,R,R,R
                                    B,B,B,B,B,B,B,B,B
                                    G,G,G,G,G,G,G,G,G
              
- Donde W (White) es Up, Y (Yellow) es Down, O (Orange) es Left, R (Red) es right, B(Blue) es Back y G (Green) es Front

### Instrucciones para ejecutar el programa

- Para ejecutar el programa lo unico que se debe hacer es clonar el repositorio:  https://github.com/jona-terceros/CuboRubik.git
- Abrir la terminal de Visual Studio Code y ejecutar: python Cubo.py
- El tiempo de ejecucion es inmediato ya que tengo solo estos movimientos U,U',D,D'.
- Opcional: si desea cambiar el estado del cubo rubik tendra que ingresar en state_cube.txt y hacerlo desde ahi.

## Diseño e implementación

### Breve descripción de modelo del problema

- El modelo del problema se basa en la resolucion del cubo rubik utilizando algun algoritmo de busqueda en espacio de estados. Se busca encontrar una secuencia de movimientos que permita llevar el cubo desde un estado inicial desordenado hasta un estado final donde cada una de las seis caras este compuesta por nueve cuadrados del mismo color, mi principal objetivo fue aplicar el algoritmo A* una técnica de búsqueda informada que garantiza encontrar la solución óptima explorando el espacio de búsqueda de manera eficiente, ademas de implementar las heuristicas: distancia manhattan de las piezas y la gestión de orientaciones de las caras para estimar el número mínimo de movimientos necesarios para resolver el cubo en su totalidad.

### Explicación y justificación de algoritmo(s), técnicas, heurísticas seleccionadas
- Para resolver este problema (cubo rubik) de busqueda en espacio de estados decidi utilizar el algoritmo visto en clase: A* o A estrella, Porque decidi usar este algoritmo? bueno decidi utilizarlo ya que como vimos en la clase es un  algoritmo de busqueda informada que encuentra la solucion optima  mientras este explora el espacio de busquedas de una manera mas eficiente y al investigar un poco mas por mi cuenta sobre este algoritmo vi que es mas flexible con ciertas heuristicas.
- Que heurisiticas decidi utilizar? Bueno decidi utilizar 2 heuristicas, una que es la distancia Manhattan de las piezas, ya que para cada pieza del cubo, la heuristica nos calcula la distancia de Manhattan entre la posicion actual del pieza y su posicion objetivo, y bueno como vimos en clase la distancia Manhattan es la suma de las diferencias en las coordenadas de fila y columna entre la posición actual y la posición objetivo, en esta distancia basicamente se calcula para todas la piezas del cubo y se suma para tener una estimacion de la cant total de movimientos que se necesitan realizar para llevar todas las piezas del cubo de Rubik desde sus posiciones actuales a sus posiciones objetivo, y la otra heuristica fue que maneje las orientaciones de de la caras, donde se toma en cuenta la orientación de las caras del cubo, donde  comparo la orientación actual de las caras con una orientacion objetivo en la que cada cara tenga un color específico en la posición correcta.

### En caso de usar modelos lingüísticos, incluir los prompts clave.
- Heuristica distancia Manhattan para resolver el cubo rubik.
- Algortimo A* Implementacion en Python.
## Trabajo Futuro
### Lista de tareas inconclusas y/o ideas para continuar con el proyecto
- Logre cargar el cubo rubik con la implementacion de un mensaje de error si los datos de un cubo son inválidos.
- Logre solamente hacer los movimiento U,U',D,D' ,luego me quede a media de la implementacion de F y F' y los demas movimientos no logre finalizar.
- Logre hacer ejecutar A* y asi obtener los pasos de la solucion hasta donde tengo implementado los movimientos y si funciona.
