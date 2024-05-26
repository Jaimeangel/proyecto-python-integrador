# Aplicación de Seguimiento de Gastos
Este documento proporciona una descripción detallada del código proporcionado. El código es un script de Python que permite a los usuarios gestionar sus transacciones financieras, incluyendo gastos e ingresos. Utiliza varias clases y métodos para validar entradas, registrar transacciones y mostrar balances.

El usuario puede hacer las siguientes acciones:
* ingresar un gasto.
* listar todos sus gastos.
* ingresar uu ingreso.
* listar todos los ingreos.
* ver su balance general y capacidad de ahorro.

## Ejecutar el programa
Para que el programa funcione correctamente es necesario seguir las siguientes recomendaciones:
* crear un entorno virtual
* instalar todas las dependencias necesarias del archivo requirements.txt

Asegurese de tener estas especificaciones antes de tratar de correr el programa.

Para ejectuar iniciar el programa debe ejecutar el siguiente script:
```
python main.py
```
Despues de iniciarse el codigo, puede seguir las instrucciones guiadas de la interfaz. 
# Documentacion codigo
## Persistencia de informacion con modulo pickle
Antes de comenzar la explicacion del codigo creado, es necesario comentar que para guardar la informacion de transacciones de gastos e ingresos creados, hacemos uso del modulo pickle. Cada vez que se cree alguna transaccion sera gaurdada en el archivo 'datos_financieros.pkl', el cual se creara si no existe. Cada vez que se vuelva a iniciar la aplicacion se restaurara la informacion contenida en el archivo.

la siguiente explicacion corresponde al script del archivo main.py
```
from transaccion import Gasto, Ingreso
from seguimiento_transaccion import SeguimientoTransacciones
from validador import Validador
```
Estas líneas importan las clases Gasto, Ingreso, SeguimientoTransacciones y Validador desde sus respectivos módulos. Estas clases son esenciales para la creación y manejo de transacciones y su validación. Posteriormente explicaremos todas las clases utilizdas.
## Inicialización
Para empezar el ciclo  del codigo tenemos un ciclo While, el cual repodruce el codigo que empezaremos a continuacion:
```
if __name__ == "__main__":
    transacciones = SeguimientoTransacciones()
    validaciones = Validador()
```
Este bloque inicializa las instancias de SeguimientoTransacciones y Validador. SeguimientoTransacciones se encarga de manejar todas las transacciones, mientras que Validador verifica la validez de las entradas del usuario.
## Listas de Categorías
```
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
```
Estas dos listas definen las categorías posibles para gastos e ingresos. Los usuarios seleccionan una categoría de estas listas cuando ingresan una nueva transacción.

## Menú de Opciones
```
menu = {
    1: 'Ingresar un gasto',
    2: 'Ingresar un ingreso',
    3: 'Ver ingresos',
    4: 'Ver gastos',
    5: 'Mi balance personal',
    6: 'Salir',
}
```
Este diccionario define el menú principal del programa, permitiendo al usuario elegir entre varias acciones.
## Función para Ingresar Transacciones
```
def ingresar_transaccion(tipo) -> None:
    # (El código de esta función se describe a continuación)
```
La función ingresar_transaccion maneja el proceso de ingreso de una nueva transacción, ya sea un gasto o un ingreso. Se detalla a continuación.
### Solicitar Monto
```
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
```
Este bloque solicita al usuario un monto y verifica que sea un número positivo.
### Solicitar Descripción
```
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
```
Este bloque solicita una descripción para la transacción y verifica que no esté vacía.
### Solicitar Fecha
```
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
```
Este bloque solicita la fecha de la transacción y verifica que esté en el formato correcto (yyyy-mm-dd).
### Solicitar Categoría
```
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
```
Este bloque permite al usuario seleccionar una categoría para la transacción. Las categorías disponibles dependen del tipo de transacción (gasto o ingreso).
### Crear y Guardar Transacción
```
if tipo == 'gasto':
    transaccion = Gasto(monto=monto, fecha=fecha, descripcion=descripcion, categoria=lista_categorias[categoria])
else:
    transaccion = Ingreso(monto=monto, fecha=fecha, descripcion=descripcion, categoria=lista_categorias[categoria])

transacciones.agregarTransaccion(transaccion)
print(' ')
print(f'Transacción de {tipo} guardada')
print(' ')
```
Este bloque crea una instancia de Gasto o Ingreso basada en la entrada del usuario y la guarda en transacciones.
## Ciclo Principal del Programa
```
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

```
Este bloque de código representa el ciclo principal del programa. Muestra el menú y maneja la selección del usuario, ejecutando la función correspondiente basada en la opción elegida.

# Clases utilizadas
## Clase Transaccion
```
from pydantic import BaseModel,Field
from typing import Literal

class Transaccion(BaseModel):
    monto: float = Field(..., gt=0, description="El monto debe ser mayor a cero")
    fecha: str = Field(..., description="La fecha de la transacción")
    descripcion: str = Field(..., max_length=255, description="Descripción de la transacción")
    categoria: str = Field(..., max_length=50, description="Categoría de la transacción")

    class Config:
        validate_assignment = True

class Gasto(Transaccion):
    tipo: Literal['gasto'] = 'gasto'

class Ingreso(Transaccion):
    tipo: Literal['ingreso'] = 'ingreso'
```
Se utilizan las siguientes importaciones:

* BaseModel y Field de pydantic: pydantic es una librería de Python que proporciona validación de datos basada en modelos. BaseModel es la clase base para crear modelos de datos y Field se usa para definir atributos con validaciones específicas.
* Literal de typing: se usa para restringir el valor de un atributo a una o más opciones específicas.

### Descripción
La clase Transaccion es un modelo base que representa una transacción financiera. Hereda de BaseModel de pydantic, lo que le proporciona validación de datos automática y otras funcionalidades útiles.
La clase Gasto e Ingreso hereda de Transaccion y añade un atributo específico para identificar el tipo de transacción como un gasto.
### Atributo Adicional
tipo (Literal['ingreso'] y Literal['gasto']): Este atributo se establece a 'ingreso' o 'gasto' de manera predeterminada y solo puede tener este valor. Se utiliza para identificar la transacción como un ingreso o gasto.

##  Clase SeguimientoTransacciones
La clase SeguimientoTransacciones es responsable de manejar una lista de transacciones financieras, incluyendo tanto ingresos como gastos. Proporciona métodos para agregar, listar y calcular el balance de las transacciones, así como para guardar y cargar los datos desde un archivo.

```
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
```

### Importaciones
* Transaccion, Gasto, Ingreso: Importa las clases que representan las transacciones.
* ValidationError: Importa la excepción que se usa para manejar errores de validación de datos con pydantic.
* List: Importa el tipo de lista desde typing para la anotación de tipos.
* pickle: Módulo estándar de Python para serialización y deserialización de objetos.

## Metodos de clase
* El constructor inicializa dos listas vacías, lista_gastos y lista_ingresos, y llama al método cargar_datos para cargar transacciones previamente guardadas desde un archivo.
* Método agregarTransaccion: Este método agrega una transacción a la lista correspondiente (lista_gastos o lista_ingresos) y guarda los datos actualizados en el archivo.
* Método listarGastos: Este método imprime una lista de todos los gastos registrados. Si no hay gastos, imprime un mensaje indicando que no hay registros.
* Método listarIngresos: Este método imprime una lista de todos los ingresos registrados. Si no hay ingresos, imprime un mensaje indicando que no hay registros.
* Método balance: Este método calcula y muestra el balance general, la diferencia entre los ingresos totales y los gastos totales.
* Método guardar_datos: Este método guarda las listas de transacciones en un archivo datos_financieros.pkl utilizando pickle. Utiliza el método model_dump de pydantic para convertir las instancias de Gasto e Ingreso en diccionarios.
* Método cargar_datos: Este método carga las listas de transacciones desde el archivo datos_financieros.pkl utilizando pickle. Si el archivo no se encuentra, no hace nada. Si hay otros errores durante la carga (como EOFError, KeyError, ValidationError), imprime un mensaje de error.

##  Clase Validator
La clase Validador proporciona varios métodos para validar diferentes tipos de datos. Estos métodos son útiles para asegurar que los datos ingresados por el usuario cumplan con ciertos criterios antes de ser procesados.

### Descripción 
* Se importa el módulo datetime para la validación de fechas.
* Método validarFecha: Este método valida si una cadena de texto corresponde a una fecha válida en el formato YYYY-MM-DD.
* Método isEmpty: Este método verifica si una cadena de texto está vacía después de eliminar los espacios en blanco.
* Método isNumber: Este método verifica si un dato es un número entero.
* Método isPositive: Este método verifica si un número es positivo.
* Método isMoney: Este método verifica si un dato es un número positivo, aplicando las validaciones de isNumber e isPositive.

# Testing
Se utiliza la librería unittest para probar la funcionalidad de la clase SeguimientoTransacciones que maneja transacciones financieras.

para ejecutar los test ejecute el siguiente comando:
```
python test.py
```
Codigo
```
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
```
### Descripción
* Método setUp: Configura el entorno inicial para cada prueba, creando una instancia de SeguimientoTransacciones.
* Método test_agregarTransaccion_gasto: Descripción: Verifica que un gasto se agrega correctamente a la lista de gastos.Se asegura de que la longitud de lista_gastos aumente en uno tras agregar un nuevo gasto.
* Método test_agregarTransaccion_ingreso: Verifica que un ingreso se agrega correctamente a la lista de ingresos.Se asegura de que la longitud de lista_ingresos aumente en uno tras agregar un nuevo ingreso.
* Método test_listarGastos: Verifica la funcionalidad del método listarGastos tanto cuando la lista de gastos está vacía como cuando tiene elementos. Llama al método listarGastos en ambos escenarios.
* Método test_listarIngresos : Verifica la funcionalidad del método listarIngresos tanto cuando la lista de ingresos está vacía como cuando tiene elementos. Llama al método listarIngresos en ambos escenarios.