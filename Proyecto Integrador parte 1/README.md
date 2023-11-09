---------------------------------------------------------------------------------------------------------------------------

# Juego de Laberinto con Teclado

---------------------------------------------------------------------------------------------------------------------------
**Autor:** Karl Melendez  
**Fecha:** 11/03/2023  
**Proyecto:** Integrador parte 1  

---------------------------------------------------------------------------------------------------------------------------



## Introducción

El "Juego de Laberinto con Teclado" es un proyecto simple en Python que te permite mover un personaje a través de un laberinto 
utilizando las teclas de flecha. El juego incluye una opción para salir en cualquier momento utilizando la tecla **"Esc"**.

**Representación del Laberinto en Caracteres ASCII:** La "representación del laberinto en caracteres ASCII" se refiere a cómo se visualiza el
 laberinto en la pantalla. Usar caracteres ASCII significa usar caracteres simples, como # para las paredes, P para el jugador y . para los 
 espacios vacíos, para crear la cuadrícula del laberinto. En tu archivo maze_game.py, definirás esta representación del laberinto utilizando 
 cadenas de texto que formarán el diseño del laberinto.

**Paso 1: Crear el archivo `maze_game.py)`**Puede ser en VSC no olvides crear tu Folder primero en tu PC donde archivaras tus archivos local!
1. En la página de inicio de tu repositorio recién creado, haz clic en el botón "Add file" y selecciona "Create new file".
2. Llama al archivo `maze_game.py)`, que será el archivo principal de tu proyecto.
3. Escribe o copia el código inicial de tu juego en `maze_game.py)`. 

**---------------------------------Documentación y Comentarios------------------------------------** 
# Juego de Laberinto

## Descripción
Este módulo implementa un juego de laberinto en el que el jugador controla a un personaje que se mueve en un laberinto. Este es 
un juego simple de laberinto donde el jugador puede mover al personaje "P" dentro del laberinto utilizando las teclas del teclado. 
El juego está escrito en Python y utiliza el módulo `keyboard` para capturar las teclas presionadas.

## Requisitos Previos

Para ejecutar este juego, debes instalar el módulo `keyboard` utilizando el siguiente comando:

'pip install keyboard'

## Contenido del Repositorio

- `maze_game.py`: El código fuente del juego de laberinto.
- `readme.md`: Este archivo, proporcionando notas y explicaciones detalladas del código.
- `test_game.py`: Este archivo hacemos pruebas al codigo
- `LICENSE`: La licencia que rige el uso de este código.

## Constantes del Juego

El juego utiliza algunas constantes para definir el laberinto y los mensajes que se muestran. Estas constantes se almacenan al comienzo del archivo para facilitarsu modificación:

- `LABERINTO`: Una lista que representa el laberinto con "#" como paredes, "." como espacios vacíos y "P" como la posición inicial del jugador.
- `MENSAJE_BIENVENIDA`: Un mensaje de bienvenida que se muestra al inicio del juego.
- `MENSAJE_INGRESO_NOMBRE`: Un mensaje que solicita al jugador ingresar su nombre.
- `MENSAJE_COMIENZO`: El mensaje que se muestra si el jugador está listo para comenzar.
- `MENSAJE_ESPERA`: El mensaje que se muestra si el jugador no está listo para comenzar.
- `MENSAJE_NO_VALIDO`: Un mensaje que se muestra si la respuesta del jugador no es válida.
- `MENSAJE_FIN_JUEGO`: El mensaje que se muestra cuando el jugador decide salir del juego.

## Funciones del Juego

El código se divide en funciones para realizar diferentes tareas:

- `imprimir_laberinto(lab)`: Esta función imprime el laberinto en la consola.
- `encontrar_posicion_inicial(lab)`: Encuentra la posición inicial del jugador en el laberinto y devuelve una tupla con las coordenadas.
- `mover_jugador(lab, fila, col, direccion)`: Mueve al jugador en el laberinto según la dirección elegida. Actualiza la posición del jugador en el laberinto.

## Pasos a Seguir

Si eres nuevo en la programación y deseas aprender cómo funciona este juego, aquí tienes los pasos a seguir:

1. Asegúrate de tener Python instalado en tu computadora.
2. Instala el módulo `keyboard` utilizando `pip install keyboard`.
3. Descarga o clona este repositorio en tu computadora.
4. Abre el archivo `maze_game.py` en tu editor de código.
5. Lee los comentarios en el código para comprender cada parte del juego.
6. Ejecuta el juego utilizando `python maze_game.py`.
7. Sigue las instrucciones en la consola para jugar y mover al personaje en el laberinto.

**Detallado**
Este código implementa un juego de laberinto controlado por el teclado. Aquí te explico paso a paso lo que hace:

1. **Importación de módulos**:
   - Se importa el módulo `keyboard`, que se usa para detectar eventos de teclado. Asegúrate de haberlo instalado previamente con 
   "pip install keyboard".

2. **Definición de Constantes**:
   - Se definen constantes que se utilizarán en el juego:
     - `LABERINTO`: Representa el diseño del laberinto, donde "#" son las paredes y "P" es la posición inicial del jugador.
     - Mensajes para mostrar al jugador: 
     `MENSAJE_BIENVENIDA`, `MENSAJE_INGRESO_NOMBRE`, `MENSAJE_COMIENZO`, `MENSAJE_ESPERA`, `MENSAJE_NO_VALIDO`, `MENSAJE_FIN_JUEGO`.

3. **Función `imprimir_laberinto(lab)`**:
   - Esta función recibe el laberinto como argumento y lo imprime en la consola. Imprime cada fila del laberinto en una nueva línea.

4. **Función `encontrar_posicion_inicial(lab)`**:
   - Encuentra la posición inicial del jugador en el laberinto. Recorre cada celda del laberinto y busca la "P". Devuelve las coordenadas 
   `(fila, columna)` donde se encuentra el jugador o `None` si no lo encuentra.

5. **Inicialización del Juego**:
   - Se llama a `encontrar_posicion_inicial` para encontrar la posición inicial del jugador y se inicializan las coordenadas del jugador.

6. **Función `mover_jugador(lab, fila, col, direccion)`**:
   - Esta función mueve al jugador en el laberinto según la dirección proporcionada. Recibe el laberinto, las coordenadas actuales del jugador y la dirección.
   - Calcula las nuevas coordenadas `(nueva_fila, nueva_col)` en función de la dirección.
   - Verifica si el movimiento es válido (dentro de los límites del laberinto y sin chocar con una pared).
   - Si el movimiento es válido, crea una copia del laberinto con la nueva posición del jugador y devuelve el nuevo laberinto y 
   las coordenadas del jugador actualizadas. Si el movimiento no es válido, devuelve el laberinto y las coordenadas actuales sin cambios.

7. **Función `main()`**:
   - Inicia el juego y solicita al jugador su nombre.
   - Pregunta si el jugador está listo para comenzar y muestra mensajes según la respuesta.
   - Inicializa las coordenadas del jugador nuevamente.
   - Entra en un bucle principal que detecta eventos de teclado:
     - Lee eventos de teclado en busca de teclas presionadas (`keyboard.read_event()`).
     - Verifica si el evento es una tecla presionada (`KEY_DOWN`).
     - Según la tecla presionada, determina la dirección del movimiento (arriba, abajo, izquierda, derecha) o finaliza el juego si se presiona "Esc".
     - Llama a `mover_jugador` para actualizar la posición del jugador y el laberinto.
     - Imprime el laberinto actualizado en la consola.

8. **Ejecución del Juego**:
   - Se llama a la función `main()` para iniciar el juego.

Este código crea un juego de laberinto en el que el jugador controla un personaje que se mueve en un laberinto utilizando las teclas direccionales. 
La lógica del juego se desarrolla en el bucle principal, donde se detectan los eventos de teclado y se actualiza la posición del jugador en el laberinto. 
El juego continúa hasta que el jugador presiona "Esc" para salir.

¡Disfruta del juego y sigue aprendiendo programación!


**------------------Creamos pruebas unitarias en el proyecto para asegurar su funcionalibidad---------------------**


## Pruebas Unitarias

En este proyecto, hemos implementado pruebas unitarias para garantizar el correcto funcionamiento de las funciones clave del juego de laberinto. Utilizamos el módulo `unittest` de Python para organizar y ejecutar las pruebas.

### Estructura de las Pruebas

Hemos estructurado las pruebas en tres partes:

1. **Configuración de la prueba**: En esta sección, se establece el escenario de la prueba. Creamos un laberinto de prueba y configuramos las coordenadas iniciales del jugador.

2. **Ejecución de la función a probar**: Indicamos la función que estamos probando y la llamamos con los datos de prueba específicos.

3. **Verificación de los resultados**: Utilizamos `self.assertEqual` para verificar si las nuevas coordenadas generadas por la función son las esperadas.

### Ejemplos de Pruebas

Hemos realizado pruebas en las siguientes funciones del juego de laberinto:

- `test_mover_jugador_izquierda`: Esta prueba verifica el movimiento del jugador hacia la izquierda en el laberinto.

- `test_mover_jugador_derecha`: En esta prueba, comprobamos el movimiento del jugador hacia la derecha.

### Cómo Ejecutar las Pruebas

Puedes ejecutar las pruebas unitarias utilizando el siguiente comando:

**test_game.py**


**-----------------------------------------Version Control Git---------------------------------------------------**
sumiremos que ya has configurado tu repositorio en GitHub siguiendo los pasos mencionados. Asegúrate 
de tener Git instalado en tu sistema antes de seguir estos pasos:

1. Abre una terminal o símbolo del sistema. **(BASH)**

2. Navega al directorio donde se encuentra tu proyecto. Puedes usar el comando `cd` para cambiar de directorio.
**cd /ruta/al/proyecto**

3. Inicializa un repositorio Git en tu proyecto.
**git init**

4. Agrega todos los archivos y carpetas de tu proyecto al área de preparación de Git.
   **git add .**

El punto `.` significa que estás agregando todos los archivos y carpetas en el directorio actual.

5. Realiza tu primer commit para confirmar los cambios.
   **git commit -m "Primer commit"**

Puedes reemplazar `"Primer commit"` con un mensaje descriptivo que explique tu commit.

6. Vincula tu repositorio local de Git con tu repositorio en GitHub. Reemplaza con el nombre de tu repositorio.
**git remote add origin**  Enlace de tu repositorio https://github.com/<nombre_de_usuario>/<nombre_del_repositorio>.git
 

7. Empuja tus cambios al repositorio en GitHub.
   **git push -u origin master**
   
Esto subirá tus cambios al repositorio en GitHub. Debes proporcionar tus credenciales de GitHub cuando se te solicite.

¡Eso es! Tu proyecto debería estar ahora en tu repositorio de GitHub. Puedes acceder a él y compartirlo con otros. 
Asegúrate de mantener tu repositorio actualizado con nuevos commits a medida que continúas trabajando en tu proyecto.