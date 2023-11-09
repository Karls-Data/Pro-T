

"""Este módulo contiene el juego de laberinto con teclado."""

import keyboard

# Resto del código


def imprimir_laberinto(lab):
    """
    Imprime el laberinto en la consola.

    Args:
        lab (list): El laberinto representado como una lista de cadenas.
    """
    for fila in lab:
        print(fila)


def encontrar_posicion_inicial(lab):
    """
    Encuentra la posición inicial del jugador en el laberinto.

    Args:
        lab (list): El laberinto representado como una lista de cadenas.

    Returns:
        tuple or None: Una tupla con la posición inicial (fila, columna) del jugador o None si no se encuentra.
    """

    for fila in range(len(lab)):
        for col in range(len(lab[fila])):
            if lab[fila][col] == "P":
                return fila, col
    return None


def mover_jugador(lab, fila, col, dir):
    """
    Mueve al jugador en el laberinto según la dirección elegida.

    Args:
        lab (list): El laberinto representado como una lista de cadenas.
        fila (int): La fila actual del jugador.
        col (int): La columna actual del jugador.
        dir (str): La dirección de movimiento ("arriba", "abajo", "izquierda" o "derecha").

    Returns:
        tuple: Una tupla con la nueva posición (fila, columna) del jugador.
    """
    nueva_fila, nueva_col = fila, col

    if dir == "arriba":
        nueva_fila -= 1
    elif dir == "abajo":
        nueva_fila += 1
    elif dir == "izquierda":
        nueva_col -= 1
    elif dir == "derecha":
        nueva_col += 1

    if 0 <= nueva_fila < len(lab) and 0 <= nueva_col < len(lab[0]) and lab[nueva_fila][nueva_col] != "#":
        lab[fila] = lab[fila][:col] + "." + lab[fila][col + 1:]
        lab[nueva_fila] = lab[nueva_fila][:nueva_col] + \
            "P" + lab[nueva_fila][nueva_col + 1:]
        return nueva_fila, nueva_col
    else:
        return fila, col


print("Bienvenido al juego de aventura")

nombre_jugador = input("Ingresa tu nombre: ")
print(f"¡Bienvenido, disfruta de esta gran aventura, {nombre_jugador}!")

ready = input("¿Estás listo para empezar? (Si / No): ").lower()

if ready == "si":
    print("¡Comencemos!")
elif ready == "no":
    print("¡Entendido! Puedes comenzar cuando estés listo.")
else:
    print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")

laberinto = [
    "##########",
    "#....P...#",
    "#........#",
    "##########"
]

fila_jugador, col_jugador = encontrar_posicion_inicial(laberinto)

while True:
    imprimir_laberinto(laberinto)
    direccion = None

    # Usar keyboard para obtener la dirección
    while direccion not in ["arriba", "abajo", "izquierda", "derecha", "esc"]:
        event = keyboard.read_event(suppress=True)

        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "up":
                direccion = "arriba"
            elif event.name == "down":
                direccion = "abajo"
            elif event.name == "left":
                direccion = "izquierda"
            elif event.name == "right":
                direccion = "derecha"
            elif event.name == "esc":
                print("¡Buen juego, perdedor!")
                exit()

    fila_jugador, col_jugador = mover_jugador(
        laberinto, fila_jugador, col_jugador, direccion)

    if laberinto[fila_jugador][col_jugador] == ".":
        print("¡Lo siento, perdiste!")
        break
    elif laberinto[fila_jugador][col_jugador] == "#":
        print("¡Felicitaciones, ganaste!")
        break
