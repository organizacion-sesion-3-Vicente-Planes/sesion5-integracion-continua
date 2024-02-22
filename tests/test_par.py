# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.par import par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:
    def test_par(self):
        # Prueba con un número par
        self.assertTrue(par(2))
        # Prueba con un número impar
        self.assertFalse(par(3))
        # Prueba con cero, que es par
        self.assertTrue(par(0))
        # Prueba con un número negativo par
        self.assertTrue(par(-4))
        # Prueba con un número negativo impar
        self.assertFalse(par(-5))
