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
            obj_nodo: Piso = nodo_actual.objeto
            print(f"Nombre: {obj_nodo.nombre}")
            print(f"Filas: {obj_nodo.filas}")
            print(f"Columnas: {obj_nodo.columnas}")
            print(f"Precio por Voltear: {obj_nodo.precio_voltear}")
            print(f"Precio por Intercambiar: {obj_nodo.precio_intercambiar}")
            print(f"Lista de Patrones:")
            obj_nodo.lista_patrones.ordenar()
            obj_nodo.lista_patrones.imprimir()
            nodo_actual = nodo_actual.siguiente
        if self.puntero is None:
            input("\nNo hay pisos cargados"
                  "\nPresione una tecla para continuar...\n\n")
        else:
            input("\nPresione una tecla para continuar...\n\n")
    
    def listar_pisos(self):
        self.ordenar()
        nodo_actual: Nodo = self.puntero
        index = 0
        while nodo_actual != None:
            obj_nodo: Piso = nodo_actual.objeto
            print(f"| {index+1}. {obj_nodo.nombre}" f"{' ' * (34-len(str(index+1))-len(obj_nodo.nombre))}|")
            nodo_actual = nodo_actual.siguiente
            index += 1
        if self.puntero is None:
            input("\nNo hay pisos cargados"
                  "\nPresione una tecla para continuar...\n\n")

    def eliminar(self, nombre_piso: str):
        nodo_actual: Nodo = self.puntero
        obj_nodo: Piso = nodo_actual.objeto
        nodo_anterior: Nodo = None
        while nodo_actual and obj_nodo.nombre != nombre_piso:
            if obj_nodo.nombre == nombre_piso:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
        if nodo_anterior is None:
            self.puntero = nodo_actual.siguiente
            nodo_actual = None
        elif nodo_actual and nodo_anterior:
            nodo_anterior.siguiente = nodo_actual.siguiente
            nodo_actual = None
        else:
            input("\nNo se encontró el piso"
                  "\nPresione una tecla para continuar...\n\n")

    def buscar(self, nombre: str):
        nodo_actual = self.puntero
        while nodo_actual:
            obj_nodo: Piso = nodo_actual.objeto
            if obj_nodo.nombre == nombre:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None

    def buscar_indice(self, index: int):
        nodo_actual = self.puntero
        contador = 0
        while nodo_actual:
            if contador == index:
                return nodo_actual
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return None

    def vaciar(self):
        self.puntero = None

    def ordenar(self):
        nodo_actual = self.puntero
        while nodo_actual:
            nodo_siguiente = nodo_actual.siguiente
            while nodo_siguiente:
                obj_nodo_actual: Piso = nodo_actual.objeto
                obj_nodo_siguiente: Piso = nodo_siguiente.objeto
                if obj_nodo_actual.nombre > obj_nodo_siguiente.nombre:
                    nodo_actual.objeto, nodo_siguiente.objeto = nodo_siguiente.objeto, nodo_actual.objeto
                nodo_siguiente = nodo_siguiente.siguiente
            nodo_actual = nodo_actual.siguiente

    def __len__(self):
        contador = 0
        nodo_actual = self.puntero
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador