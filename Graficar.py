import graphviz

def graficar():
    try:
        print("Graficando...")
        dot = graphviz.Digraph(filename="archivo.dot", format="pdf", directory="renders")
        dot.render(view=True)
    except Exception as error:
        print(f"Error: {error}")
        input("Presione una tecla para continuar...")
        return