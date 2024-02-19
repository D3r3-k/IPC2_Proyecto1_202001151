import os


def graficar():
    try:
        archivo = "render/nodos.dot"
        archivoDOT = open(archivo, "w")
        archivoDOT.write("digraph{\n")
        archivoDOT.write("rankdir = LR;\n")
        archivoDOT.write('node [fontname = "Arial Black"; fontsize = 14; margin = "0.2,0.1";];\n')
        archivoDOT.write('edge [color = "#008cff";];\n')
        archivoDOT.write("}\n")
        archivoDOT.close()
        os.system("dot.exe -Tpng "+archivo+" -o " +
                  archivo.replace(".dot", ".png"))

        print("     [✓] Gráfica creada!")
        input("     Presiona una tecla para continuar...")
    except:
        input("\n     [X] Hubo un error al crear la gráfica!"
              "\n     Presiona una tecla para continuar...")
