class Azulejo:
    def __init__(self, fila:int, columna:int, color: str, cambiado: bool = False):
        self.fila = fila
        self.columna = columna
        self.color = color
        self.cambiado = cambiado

    def intercambiar(self, otro: 'Azulejo'):
        self.color, otro.color = otro.color, self.color
        self.cambiado = True
        otro.cambiado = True

    def voltear(self):
        if self.color == "B":
            self.color = "N"
        elif self.color == "N":
            self.color = "B"
        self.cambiado = True