import unittest

class pruebaOperacionesEnteros(unittest.TestCase):
    def setUp(self):
        self.assertEqual(True, False)

    def tearDown(self):
        self.assertEqual(True, False)

    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6
        # Do
        resultadoActual = self.operacion.MCD(numero1, numero2)
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)