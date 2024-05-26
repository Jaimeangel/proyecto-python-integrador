from transaccion import Gasto, Ingreso
from seguimiento_transaccion import SeguimientoTransacciones
from validador import Validador

if __name__ == "__main__":
    transacciones = SeguimientoTransacciones()
    validaciones = Validador()
    
    list_gastos = {
        1: 'Alimentación',
        2: 'Cuentas y pagos',
        3: 'Casa',
        4: 'Transporte',
        5: 'Ropa',
        6: 'Salud e higiene',
        7: 'Diversión',
        8: 'Otros gastos'
    }
    
    list_ingresos = {
        1: 'Salario',
        2: 'Bonos',
        3: 'Inversiones',
        4: 'Freelance',
        5: 'Alquileres',
        6: 'Intereses',
        7: 'Otros ingresos',
    }

    menu = {
        1: 'Ingresar un gasto',
        2: 'Ingresar un ingreso',
        3: 'Ver ingresos',
        4: 'Ver gastos',
        5: 'Mi balance personal',
        6: 'Salir',
    }

    def ingresar_transaccion(tipo)-> None:
        while True:
            try:
                print(' ')
                monto = float(input('Ingresa un monto: '))
                print(' ')
                if not validaciones.isPositive(monto):
                    print(' ')
                    print('Ingrese un monto válido mayor a cero')
                    print(' ')
                else:
                    break
            except ValueError:
                print(' ')
                print('Debe ingresar un valor numérico')
                print(' ')
        
        while True:
            print(' ')
            descripcion = input('Ingresa una descripción: ')
            print(' ')
            if not validaciones.isEmpty(descripcion):
                print(' ')
                print('El campo está vacío, por favor ingrese una descripción')
                print(' ')
            else:
                break

        while True:
            print(' ')
            fecha = input('Ingresa la fecha (yyyy-mm-dd): ')
            print(' ')
            if not validaciones.validarFecha(fecha):
                print(' ')
                print('La fecha ingresada no es válida, ingrese una fecha en formato (yyyy-mm-dd) y en un año, mes y día existente')
                print(' ')
            else:
                break

        lista_categorias = list_gastos if tipo == 'gasto' else list_ingresos
        while True:
            print(' ')
            print(f'Categoría del {tipo} (Ingresa el número correspondiente)')
            print(' ')
            for key, value in lista_categorias.items():
                print(f"{key}: {value}")

            try:
                print(' ')
                categoria = int(input())
                print(' ')
                if categoria not in lista_categorias:
                    print(' ')
                    print(f"Número inválido, ingrese un número entre el rango de 1 y {len(lista_categorias)}")
                    print(' ')
                else:
                    break
            except ValueError:
                print(' ')
                print('Debe ingresar un valor numérico')
                print(' ')

        if tipo == 'gasto':
            transaccion = Gasto(monto=monto, fecha=fecha, descripcion=descripcion, categoria=lista_categorias[categoria])
        else:
            transaccion = Ingreso(monto=monto, fecha=fecha, descripcion=descripcion, categoria=lista_categorias[categoria])

        transacciones.agregarTransaccion(transaccion)
        print(' ')
        print(f'Transacción de {tipo} guardada')
        print(' ')

    while True:
        print(' ')
        print('Elije una de las opciones ingresando el número respectivo')
        print(' ')
        for key, value in menu.items():
            print(f"{key}: {value}")

        try:
            print(' ')
            opcion = int(input())
            if opcion == 1:
                ingresar_transaccion('gasto')
            elif opcion == 2:
                ingresar_transaccion('ingreso')
            elif opcion == 3:
                transacciones.listarIngresos()
            elif opcion == 4:
                transacciones.listarGastos()
            elif opcion == 5:
                transacciones.balance()
            elif opcion == 6:
                break
            else:
                print(' ')
                print('Opción no válida, ingrese un número del 1 al 6')
                print(' ')
        except ValueError:
            print(' ')
            print('Debe ingresar un valor numérico')
            print(' ')