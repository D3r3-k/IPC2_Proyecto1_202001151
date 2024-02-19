from Clases.Nodo import Nodo
from Clases.Piso import Piso


class ListaPisos:
    def __init__(self):
        self.puntero: Nodo = None

    def insertar(self, objeto: Piso):
        nuevo_nodo = Nodo(objeto)
        if self.puntero is None:
            self.puntero = nuevo_nodo
        else:
            nodo_actual = self.puntero
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir(self):
        nodo_actual: Nodo = self.puntero
        while nodo_actual != None:
            objeto_nodo: Piso = nodo_actual.objeto
            print(f"Nombre: {objeto_nodo.nombre}")
            print(f"Filas: {objeto_nodo.filas}")
            print(f"Columnas: {objeto_nodo.columnas}")
            print(f"Precio por Voltear: {objeto_nodo.precio_voltear}")
            print(f"Precio por Intercambiar: {objeto_nodo.precio_intercambiar}")
            print(f"Lista de Patrones:")
            objeto_nodo.lista_patrones.imprimir()
            print("=====================================")            
            nodo_actual = nodo_actual.siguiente
        if self.puntero is None:
            input("\nNo hay pisos cargados"
                  "\nPresione una tecla para continuar...\n\n")
        else:
            input("\nPresione una tecla para continuar...\n\n")

    def eliminar(self, valor):
        pass

    def buscar(self, nombre: str):
        nodo_actual = self.puntero
        while nodo_actual:
            objeto_nodo: Piso = nodo_actual.objeto
            if objeto_nodo.nombre == nombre:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None
