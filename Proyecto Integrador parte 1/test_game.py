
# 1-Configuración de la prueba: Aquí se establece el escenario de la prueba. Se crea un laberinto de prueba y se inicializan las coordenadas del jugador.

# 2-Ejecución de la función a probar: Esta sección indica qué función se está probando y cómo se llama con los datos de prueba.

# 3-Verificación de los resultados: Aquí se utiliza self.assertEqual para verificar si las nuevas coordenadas generadas por la función son las esperada

"""
Este módulo contiene pruebas unitarias para el módulo maze_game. Prueba las funciones mover_jugador_izquierda y mover_jugador_derecha.
"""
import unittest
from maze_game import mover_jugador


class TestLaberintoGame(unittest.TestCase):
    def setUp(self):
        # Configuración común para las pruebas, como el laberinto y las coordenadas iniciales.
        self.laberinto = [
            "##########",
            "#....P...#",
            "#........#",
            "##########"
        ]
        self.fila_jugador = 1
        self.col_jugador = 4

    def test_mover_jugador_izquierda(self):
        """
        Prueba la función mover_jugador cuando el jugador se mueve hacia la izquierda.
        """
        # Ejecución de la función a probar
        nueva_fila, nueva_col = mover_jugador(
            self.laberinto, self.fila_jugador, self.col_jugador, "izquierda")

        # Verificación de los resultados
        self.assertEqual((nueva_fila, nueva_col), (1, 3))

    def test_mover_jugador_derecha(self):
        """
        Prueba la función mover_jugador cuando el jugador se mueve hacia la derecha.
        """
        # Ejecución de la función a probar
        nueva_fila, nueva_col = mover_jugador(
            self.laberinto, self.fila_jugador, self.col_jugador, "derecha")

        # Verificación de los resultados
        self.assertEqual((nueva_fila, nueva_col), (1, 5))


if __name__ == '__main__':
    unittest.main()
