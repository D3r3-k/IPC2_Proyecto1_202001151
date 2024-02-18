from Clases.Nodo import Nodo
from Clases.Patron import Patron

class ListaPatrones:
    def __init__(self):
        self.puntero: Nodo = None

    def insertar(self, objeto: Patron):
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
            objeto_nodo: Patron = nodo_actual.objeto
            print(f"    Código: {objeto_nodo.codigo}")
            print(f"    Lista de Azulejos:")
            objeto_nodo.lista_azulejos.imprimir()
            nodo_actual = nodo_actual.siguiente

    def eliminar(self, valor):
        pass

    def buscar(self, nombre: str):
        nodo_actual = self.puntero
        while nodo_actual:
            objeto_nodo: Patron = nodo_actual.objeto
            if objeto_nodo.nombre == nombre:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None

