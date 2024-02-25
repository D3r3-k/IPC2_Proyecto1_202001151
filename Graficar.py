import graphviz
from Clases.Piso import Piso
from Clases.Patron import Patron
from Clases.Azulejo import Azulejo


def graficar_patron(Piso: Piso, Patron: Patron):
    try:
        print("Graficando...")
        dot = graphviz.Digraph(filename=f"render.dot", format="pdf", directory="renders")
        dot.attr(label=f"Piso: {Piso.nombre} - Patron: {Patron.codigo}", fontname="arial", fontsize="14", labelloc="t", nodesep="0.1", ranksep="0.1")
        indice = 0
        for fila in range(Piso.filas):
            for columna in range(Piso.columnas):
                if Patron.lista_azulejos.buscar_por_indice(indice) == "B":
                    dot.node(f"{fila}{columna}", shape="square", label=f"{Patron.lista_azulejos.buscar_por_indice(indice)}", fillcolor="white", style="filled")
                elif Patron.lista_azulejos.buscar_por_indice(indice) == "N":
                    dot.node(f"{fila}{columna}", shape="square", label=f"{Patron.lista_azulejos.buscar_por_indice(indice)}", fillcolor="black", style="filled", fontcolor="white", color="white")
                indice += 1

        for fila in range(Piso.filas - 1):
            for columna in range(Piso.columnas):
                dot.edge(f"{fila}{columna}", f"{fila+1}{columna}", style="invis")
        dot.render(view=True)
    except Exception as error:
        print(f"Error: {error}")
        input("Presione una tecla para continuar...")
        return