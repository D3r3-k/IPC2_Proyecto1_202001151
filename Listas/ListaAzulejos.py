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
        print(f"{texto}")

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

    def cantidad_azulejos(self, color: str):
        nodo_actual = self.puntero
        contador = 0
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            if objeto_nodo.color == color:
                contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador

    def __len__(self):
        nodo_actual = self.puntero
        contador = 0
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador

    def voltear(self, indice: int):
        nodo_actual = self.puntero
        contador = 0
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            if indice == contador:
                return objeto_nodo.voltear()
            nodo_actual = nodo_actual.siguiente
            contador += 1
        return None
    
    def intercambiar(self, indice: int, nuevo_color: str):
        nodo_actual = self.puntero
        contador = 0
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            if indice == contador:
                return objeto_nodo.intercambiar(nuevo_color)
            nodo_actual = nodo_actual.siguiente
            contador += 1
        return None

    def intercambiar_azulejos(self, nuevo_patron, precio_voltear: int, precio_intercambiar: int):
        total = 0
        indice = 0
        n_azulejo_actual: ListaAzulejos = nuevo_patron.buscar_por_indice(indice)
        v_azulejo_actual: ListaAzulejos = self.buscar_por_indice(indice)
        while n_azulejo_actual and v_azulejo_actual:
            if n_azulejo_actual != v_azulejo_actual:
                input(f"indice: {indice} - Intercambiando {n_azulejo_actual} por {v_azulejo_actual}")
                if precio_voltear < precio_intercambiar:
                    input(f"indice: {indice} - Volteando {v_azulejo_actual}")
                    self.voltear(indice)
                    total += precio_voltear
                else:
                    input(f"indice: {indice} - Intercambiando {n_azulejo_actual} por {v_azulejo_actual}")
                    self.intercambiar(indice, n_azulejo_actual)
                    total += precio_intercambiar
            indice += 1
            n_azulejo_actual = nuevo_patron.buscar_por_indice(indice)
            v_azulejo_actual = self.buscar_por_indice(indice)
        return total