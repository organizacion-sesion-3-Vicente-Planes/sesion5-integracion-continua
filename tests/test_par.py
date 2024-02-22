# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.par import par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:
    def test_par(self):
        # Prueba con un número par
        assert par(2) == True
        # Prueba con un número impar
        assert par(3) == False
        # Prueba con cero, que es par
        assert par(0) == True
        # Prueba con un número negativo par
        assert par(-4) == True
        # Prueba con un número negativo impar
        assert par(-5) == False
