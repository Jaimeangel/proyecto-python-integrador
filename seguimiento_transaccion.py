from transaccion import Transaccion,Gasto,Ingreso
from pydantic import ValidationError
from typing import List
import pickle


class SeguimientoTransacciones:
    def __init__(self):
        self.lista_gastos: List[Gasto] = []
        self.lista_ingresos: List[Ingreso] = []
        self.cargar_datos()

    def agregarTransaccion(self, transaccion: Transaccion)-> None:
        if isinstance(transaccion, Gasto):
            self.lista_gastos.append(transaccion)
        elif isinstance(transaccion, Ingreso):
            self.lista_ingresos.append(transaccion)
        self.guardar_datos()

    def listarGastos(self)-> None:
        if len(self.lista_gastos) == 0:
            print(' ')
            print('No hay gastos registrados')
            print(' ')
        else:
            print(' ')
            print('--- Lista de gastos ---')
            for i, gasto in enumerate(self.lista_gastos, 1):
                print(f"| {i} | {gasto.fecha} | {gasto.monto} | {gasto.categoria} | {gasto.descripcion} |")
            print(' ')
    def listarIngresos(self)-> None:
        if len(self.lista_ingresos) == 0:
            print(' ')
            print('No hay ingresos registrados')
            print(' ')
        else:
            print(' ')
            print('--- Lista de ingresos ---')
            for i, ingreso in enumerate(self.lista_ingresos, 1):
                print(f"| {i} | {ingreso.fecha} | {ingreso.monto} | {ingreso.categoria} | {ingreso.descripcion} |")
            print(' ')
    def balance(self)-> None:
        ingresos = sum(ingreso.monto for ingreso in self.lista_ingresos)
        gastos = sum(gasto.monto for gasto in self.lista_gastos)
        capacidad_ahorro = ingresos - gastos
        print(' ')
        print('--- Presentamos tu balance general ---')
        print(f"Tus ingresos han sido: {ingresos}")
        print(f"Tus gastos han sido: {gastos}")
        print(f"Tu balance general es: {capacidad_ahorro}")
        print(' ')

    def guardar_datos(self)-> None:
        with open('datos_financieros.pkl', 'wb') as f:
            datos = {
                'lista_gastos': [gasto.model_dump() for gasto in self.lista_gastos],
                'lista_ingresos': [ingreso.model_dump() for ingreso in self.lista_ingresos]
            }
            pickle.dump(datos, f)

    def cargar_datos(self)-> None:
        try:
            with open('datos_financieros.pkl', 'rb') as f:
                datos = pickle.load(f)
                self.lista_gastos = [Gasto(**gasto) for gasto in datos['lista_gastos']]
                self.lista_ingresos = [Ingreso(**ingreso) for ingreso in datos['lista_ingresos']]
        except FileNotFoundError:
            pass
        except (EOFError, KeyError, ValidationError) as e:
            print(f"Error al cargar datos: {e}")