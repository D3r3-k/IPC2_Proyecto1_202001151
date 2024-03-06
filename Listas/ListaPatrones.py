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

    def listar_patrones(self, columnas):
        self.ordenar()
        nodo_actual: Nodo = self.puntero
        index = 0
        print("| Lista de Patrones:")
        while nodo_actual != None:
            obj_nodo: Patron = nodo_actual.objeto
            print(f"| {index+1}. {obj_nodo.codigo}")
            obj_nodo.lista_azulejos.imprimir_patron(columnas)
            nodo_actual = nodo_actual.siguiente
            index += 1
        if self.puntero is None:
            input("\nNo hay patrones cargados"
                  "\nPresione una tecla para continuar...\n\n")


    def buscar(self, nombre: str):
        nodo_actual = self.puntero
        while nodo_actual:
            objeto_nodo: Patron = nodo_actual.objeto
            if objeto_nodo.nombre == nombre:
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
                objeto_nodo_actual: Patron = nodo_actual.objeto
                objeto_nodo_siguiente: Patron = nodo_siguiente.objeto
                if objeto_nodo_actual.codigo > objeto_nodo_siguiente.codigo:
                    nodo_actual.objeto, nodo_siguiente.objeto = nodo_siguiente.objeto, nodo_actual.objeto
                nodo_siguiente = nodo_siguiente.siguiente
            nodo_actual = nodo_actual.siguiente
        

    def __len__(self):
        nodo_actual = self.puntero
        contador = 0
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador