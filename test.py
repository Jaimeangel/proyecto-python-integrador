import unittest
from seguimiento_transaccion import SeguimientoTransacciones
from transaccion import Gasto,Ingreso

class TestSeguimientoTransacciones(unittest.TestCase):
    def setUp(self):
        # Configura el estado inicial para las pruebas
        self.seguimiento = SeguimientoTransacciones()

    def test_agregarTransaccion_gasto(self):
        # Prueba agregar un gasto
        valor_esperado = len(self.seguimiento.lista_gastos) + 1

        gasto = Gasto(monto=100, fecha="2024-05-25", descripcion="Compra de alimentos", categoria="Alimentos")
        self.seguimiento.agregarTransaccion(gasto)
        self.assertEqual(len(self.seguimiento.lista_gastos), valor_esperado)

    def test_agregarTransaccion_ingreso(self):
        # Prueba agregar un ingreso
        valor_esperado = len(self.seguimiento.lista_ingresos) + 1
        
        ingreso = Ingreso(monto=500, fecha="2024-05-26", descripcion="Salario", categoria="Salario")
        self.seguimiento.agregarTransaccion(ingreso)
        self.assertEqual(len(self.seguimiento.lista_ingresos), valor_esperado)

    def test_listarGastos(self):
        # Prueba listar gastos cuando no hay gastos
        self.seguimiento.listarGastos() 

        # Prueba listar gastos cuando hay gastos
        gasto = Gasto(monto=100, fecha="2024-05-25", descripcion="Compra de alimentos", categoria="Alimentos")
        self.seguimiento.agregarTransaccion(gasto)
        self.seguimiento.listarGastos()  

    def test_listarIngresos(self):
        # Prueba listar ingresos cuando no hay ingresos
        self.seguimiento.listarIngresos()

        # Prueba listar ingresos cuando hay ingresos
        ingreso = Ingreso(monto=500, fecha="2024-05-26", descripcion="Salario", categoria="Salario")
        self.seguimiento.agregarTransaccion(ingreso)
        self.seguimiento.listarIngresos() 

if __name__ == '__main__':
    unittest.main()