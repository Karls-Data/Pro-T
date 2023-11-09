
# 1-Configuración de la prueba: Aquí se establece el escenario de la prueba. Se crea un laberinto de prueba y se inicializan las coordenadas del jugador.

# 2-Ejecución de la función a probar: Esta sección indica qué función se está probando y cómo se llama con los datos de prueba.

# 3-Verificación de los resultados: Aquí se utiliza self.assertEqual para verificar si las nuevas coordenadas generadas por la función son las esperada

"""
Estamos utilizando el módulo unittest para realizar pruebas unitarias en dos 
funciones del juego de laberinto: mover_jugador_izquierda y mover_jugador_derecha.
"""
import unittest


# Importa las funciones que deseas probar

from maze_game import encontrar_posicion_inicial, mover_jugador


# Define una clase que hereda de unittest.TestCase

class TestLaberintoGame(unittest.TestCase):

    def test_mover_jugador_izquierda(self):
        # Configuración de la prueba
        laberinto = [
            "##########",
            "#....P...#",
            "#........#",
            "##########"
        ]
        fila_jugador, col_jugador = 1, 4

        # Ejecución de la función a probar
        nueva_fila, nueva_col = mover_jugador(
            laberinto, fila_jugador, col_jugador, "izquierda")

        # Verificación de los resultados
        self.assertEqual((nueva_fila, nueva_col), (1, 3))

    def test_mover_jugador_derecha(self):
        # Configuración de la prueba
        laberinto = [
            "##########",
            "#....P...#",
            "#........#",
            "##########"
        ]
        fila_jugador, col_jugador = 1, 4

        # Ejecución de la función a probar
        nueva_fila, nueva_col = mover_jugador(
            laberinto, fila_jugador, col_jugador, "derecha")

        # Verificación de los resultados
        self.assertEqual((nueva_fila, nueva_col), (1, 5))
