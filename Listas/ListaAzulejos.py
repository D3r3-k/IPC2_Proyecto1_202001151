from Clases.Nodo import Nodo
from Clases.Azulejo import Azulejo


class ListaAzulejos:
    def __init__(self):
        self.puntero: Nodo = None

    def insertar(self, objeto: Azulejo):
        nuevo_nodo: Nodo = Nodo(objeto)
        if self.puntero is None:
            self.puntero = nuevo_nodo
        else:
            nodo_actual = self.puntero
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir(self):
        nodo_actual: Nodo = self.puntero
        texto = ""
        while nodo_actual != None:
            objeto_nodo: Azulejo = nodo_actual.objeto
            texto += f"[{objeto_nodo.color}]"
            nodo_actual = nodo_actual.siguiente
        print(f"        {texto}")

    def imprimir_patron(self, columnas):
        nodo_actual: Nodo = self.puntero
        contador = 0
        texto = "|   "
        while nodo_actual != None:
            objeto_nodo: Azulejo = nodo_actual.objeto
            if contador == columnas:
                texto += "\n|   "
                contador = 0
            texto += f"[{objeto_nodo.color}]"
            contador += 1
            nodo_actual = nodo_actual.siguiente
        print(texto)

    def eliminar(self, valor):
        pass

    def buscar(self, nombre: str):
        nodo_actual = self.puntero
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            if objeto_nodo.nombre == nombre:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None
    
    def buscar_por_indice(self, indice: int):
        nodo_actual = self.puntero
        contador = 0
        while nodo_actual:
            if contador == indice:
                return nodo_actual.objeto.color
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return None

    def __len__(self):
        nodo_actual = self.puntero
        contador = 0
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador
