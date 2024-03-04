class Azulejo:
    def __init__(self, color: str):
        self.color = color

    def voltear(self):
        if self.color == "B":
            self.color = "N"
        else:
            self.color = "B"

    def intercambiar(self, nuevo_color: str):
        self.color = nuevo_color