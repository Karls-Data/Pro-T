from maze_game import encontrar_posicion_inicial, mover_jugador
import sys
import unittest

# Replace with the actual path to the maze_game module
sys.path.append('/path/to/maze_game')


class TestLaberintoGame(unittest.TestCase):
    """Clase de pruebas para el juego de laberinto."""

    def test_encontrar_posicion_inicial(self):
        """Prueba la función encontrar_posicion_inicial."""
        laberinto = [
            "#############################",
            "#...P................########",
            "#.##....#######..####...####",
            "#.#......####.....##########",
            "#.##..###........############",
            "#.....######.......#.########",
            "#..#####......###############",
            "#.....#..####################",
            "##########"
        ]
        posicion = encontrar_posicion_inicial(laberinto)
        self.assertEqual(posicion, (1, 4))

    def test_mover_jugador_arriba(self):
        """Prueba el movimiento del jugador hacia arriba."""
        laberinto = [
            "#############################",
            "#...P................########",
            "#.##....#######..####...####",
            "#.#......####.....##########",
            "#.##..###........############",
            "#.....######.......#.########",
            "#..#####......###############",
            "#.....#..####################",
            "##########"
        ]
        nueva_laberinto, fila, col = mover_jugador(laberinto, 1, 4, "arriba")
        self.assertEqual(nueva_laberinto[1][5], ".")
        self.assertEqual(nueva_laberinto[0][4], "P")
        self.assertEqual(fila, 0)
        self.assertEqual(col, 4)

    def test_mover_jugador_derecha(self):
        """Prueba el movimiento del jugador hacia la derecha."""
        laberinto = [
            "#############################",
            "#...P................########",
            "#.##....#######..####...####",
            "#.#......####.....##########",
            "#.##..###........############",
            "#.....######.......#.########",
            "#..#####......###############",
            "#.....#..####################",
            "##########"
        ]
        nueva_laberinto, fila, col = mover_jugador(laberinto, 1, 4, "derecha")
        self.assertEqual(nueva_laberinto[1][4], ".")
        self.assertEqual(nueva_laberinto[1][5], "P")
        self.assertEqual(fila, 1)
        self.assertEqual(col, 5)


if __name__ == "__main__":
    unittest.main()


# conclusiones

"""
3 test fallo 1 el de mover jugador hace arriba: te lodejo para que te diviertas un rato
encontrar_posicion_inicial function revisa si esta correcta, funciona bien en el juego,  busca si la pocision inicial 'P' 
es el caso que talvez reconeze pared haceia arriba evitando el test_mover_jugador_arriba test case.
"""
