# Importa el módulo keyboard, asegúrate de instalarlo con "pip install keyboard"
import keyboard

# Constantes del juego de laberinto
LABERINTO = [
    "##########",
    "#....P...#",
    "#........#",
    "##########"
]

# Mensajes que se muestran en el juego
MENSAJE_BIENVENIDA = "Bienvenido al juego de aventura"
MENSAJE_INGRESO_NOMBRE = "Ingresa tu nombre: "
MENSAJE_COMIENZO = "¡Comencemos!"
MENSAJE_ESPERA = "¡Entendido! Puedes comenzar cuando estés listo."
MENSAJE_NO_VALIDO = "Respuesta no válida. Por favor, responde 'Si' o 'No'."
MENSAJE_FIN_JUEGO = "¡Buen juego, perdedor!"

# Función para imprimir el laberinto


def imprimir_laberinto(lab):
    for fila in lab:
        print(fila)

# Función para encontrar la posición inicial del jugador en el laberinto


def encontrar_posicion_inicial(lab):
    for i, fila in enumerate(lab):
        for j, celda in enumerate(fila):
            if celda == "P":
                return i, j
    return None


# Encuentra la posición inicial del jugador y asegúrate de que exista
initial_position = encontrar_posicion_inicial(LABERINTO)
if initial_position is None:
    print("No se pudo encontrar la posición inicial del jugador.")
    exit()

# Inicializa las coordenadas del jugador
fila_jugador, col_jugador = initial_position

# Función para mover al jugador en el laberinto


def mover_jugador(lab, fila, col, direccion):
    nueva_fila, nueva_col = fila, col

    if direccion == "arriba":
        nueva_fila -= 1
    elif direccion == "abajo":
        nueva_fila += 1
    elif direccion == "izquierda":
        nueva_col -= 1
    elif direccion == "derecha":
        nueva_col += 1

    if 0 <= nueva_fila < len(lab) and 0 <= nueva_col < len(lab[0]) and lab[nueva_fila][nueva_col] != "#":
        # Crea una copia del laberinto
        nuevo_laberinto = lab.copy()
        nuevo_laberinto[fila] = nuevo_laberinto[fila][:col] + \
            "." + nuevo_laberinto[fila][col + 1:]
        nuevo_laberinto[nueva_fila] = nuevo_laberinto[nueva_fila][:nueva_col] + \
            "P" + nuevo_laberinto[nueva_fila][nueva_col + 1:]
        return nuevo_laberinto, nueva_fila, nueva_col
    else:
        return lab, fila, col

# Función principal del juego


def main():
    print(MENSAJE_BIENVENIDA)
    nombre_jugador = input(MENSAJE_INGRESO_NOMBRE)
    print(f"¡Bienvenido, disfruta de esta gran aventura, {nombre_jugador}!")

    ready = input("¿Estás listo para empezar? (Si / No): ").lower()

    if ready == "si":
        print(MENSAJE_COMIENZO)
    elif ready == "no":
        print(MENSAJE_ESPERA)
    else:
        print(MENSAJE_NO_VALIDO)
        return

    # Encuentra la posición inicial del jugador nuevamente
    fila_jugador, col_jugador = encontrar_posicion_inicial(LABERINTO)
    imprimir_laberinto(LABERINTO)

    while True:
        direction_event = keyboard.read_event(suppress=True)
        if direction_event.event_type == keyboard.KEY_DOWN:
            direccion = None

            if direction_event.name == "up":
                direccion = "arriba"
            elif direction_event.name == "down":
                direccion = "abajo"
            elif direction_event.name == "left":
                direccion = "izquierda"
            elif direction_event.name == "right":
                direccion = "derecha"
            elif direction_event.name == "esc":
                print(MENSAJE_FIN_JUEGO)
                exit()

            if direccion:
                LABERINTO, fila_jugador, col_jugador = mover_jugador(
                    LABERINTO, fila_jugador, col_jugador, direccion)
                imprimir_laberinto(LABERINTO)


if __name__ == "__main__":
    main()
