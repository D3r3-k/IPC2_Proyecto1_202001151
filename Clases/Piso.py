from Listas.ListaPatrones import ListaPatrones
class Piso:
    def __init__(self, nombre: str, filas: int, columnas: int, precio_voltear: int, precio_intercambiar: int, lista_patrones: ListaPatrones):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.precio_voltear = precio_voltear
        self.precio_intercambiar = precio_intercambiar
        self.lista_patrones = lista_patrones
