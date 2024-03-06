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

    def buscar(self, color: str):
        nodo_actual = self.puntero
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            if objeto_nodo.color == color:
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
    
    def buscar_por_coordenadas(self, fila: int, columna: int):
        nodo_actual = self.puntero
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            if objeto_nodo.fila == fila and objeto_nodo.columna == columna:
                return objeto_nodo
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
    
    def cambiar_siguiente(self):
        nodo_actual = self.puntero
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            if objeto_nodo.cambiado:
                nodo_actual = nodo_actual.siguiente
            else:
                objeto_nodo.cambiado = True
                break
    
    def cambiar_todos(self, parametro: bool):
        nodo_actual = self.puntero
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            objeto_nodo.cambiado = parametro
            nodo_actual = nodo_actual.siguiente

    def intercambiar(self, filas: int, columnas: int, precio_intercambio: int, precio_voltear: int, nueva_lista: 'ListaAzulejos'):
        # NUEVA LISTA SOLO SIRVE PARA REFERENCIA DE LOS AZULEJOS
        # Y PODER CREAR EL NUEVO PATRON
        self.cambiar_todos(False)
        precio_total = 0
        nodo_actual: 'ListaAzulejos' = self.puntero
        nodo_nuevo: 'ListaAzulejos' = nueva_lista.puntero
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            objeto_nuevo: Azulejo = nodo_nuevo.objeto
            # print(f"[{objeto_nodo.fila},{objeto_nodo.columna}] Color: {objeto_nodo.color}-{objeto_nodo.cambiado}   |   [{objeto_nuevo.fila},{objeto_nuevo.columna}] Color: {objeto_nuevo.color}-{objeto_nodo.cambiado}")

            if objeto_nodo.cambiado:
                pass
            else:
                if objeto_nodo.color == objeto_nuevo.color:
                    objeto_nodo.cambiado = True
                    # input(f"[{objeto_nodo.fila},{objeto_nodo.columna}] = [{objeto_nuevo.fila},{objeto_nuevo.columna}]")
                else:
                    if objeto_nodo.color == "B" and objeto_nuevo.color == "N":
                        objeto_nodo.cambiado = True
                        self.cambiar_siguiente()
                        precio_total += precio_intercambio
                        objeto_nodo.intercambiar(objeto_nuevo)
                        # input(f"Intercambio [{objeto_nodo.fila},{objeto_nodo.columna}] = [{objeto_nuevo.fila},{objeto_nuevo.columna}]")
                    elif objeto_nodo.color == "N" and objeto_nuevo.color == "B":
                        objeto_nodo.cambiado = True
                        self.cambiar_siguiente()
                        precio_total += precio_intercambio
                        objeto_nodo.intercambiar(objeto_nuevo)
                        # input(f"Intercambio [{objeto_nodo.fila},{objeto_nodo.columna}] = [{objeto_nuevo.fila},{objeto_nuevo.columna}]")
                    else:
                        precio_total += precio_voltear
                        objeto_nodo.voltear()
                        # input(f"Volteo [{objeto_nodo.fila},{objeto_nodo.columna}] = [{objeto_nuevo.fila},{objeto_nuevo.columna}]")
                        


            nodo_actual = nodo_actual.siguiente
            nodo_nuevo = nodo_nuevo.siguiente
        # input(f"Precio Total: {precio_total}")
        return precio_total
    
    def instrucciones(self, nueva_lista: 'ListaAzulejos'):
        self.cambiar_todos(False)
        nodo_actual: 'ListaAzulejos' = self.puntero
        nodo_nuevo: 'ListaAzulejos' = nueva_lista.puntero
        while nodo_actual:
            objeto_nodo: Azulejo = nodo_actual.objeto
            objeto_nuevo: Azulejo = nodo_nuevo.objeto
            if objeto_nodo.cambiado:
                pass
            else:
                if objeto_nodo.color == objeto_nuevo.color:
                    objeto_nodo.cambiado = True
                    # input(f"[{objeto_nodo.fila},{objeto_nodo.columna}] = [{objeto_nuevo.fila},{objeto_nuevo.columna}]")
                else:
                    if objeto_nodo.color == "B" and objeto_nuevo.color == "N":
                        objeto_nodo.cambiado = True
                        self.cambiar_siguiente()
                        objeto_nodo.intercambiar(objeto_nuevo)
                        input(f"Intercambiar [{objeto_nodo.fila},{objeto_nodo.columna}] = [{objeto_nuevo.fila},{objeto_nuevo.columna}]")
                    elif objeto_nodo.color == "N" and objeto_nuevo.color == "B":
                        objeto_nodo.cambiado = True
                        self.cambiar_siguiente()
                        objeto_nodo.intercambiar(objeto_nuevo)
                        input(f"Intercambiar [{objeto_nodo.fila},{objeto_nodo.columna}] = [{objeto_nuevo.fila},{objeto_nuevo.columna}]")
                    else:
                        objeto_nodo.voltear()
                        input(f"Voltear [{objeto_nodo.fila},{objeto_nodo.columna}] = [{objeto_nuevo.fila},{objeto_nuevo.columna}]")
            nodo_actual = nodo_actual.siguiente
            nodo_nuevo = nodo_nuevo.siguiente

