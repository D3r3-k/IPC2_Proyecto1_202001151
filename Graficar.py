import os


def graficar():
    try:
        archivo = "render/nodos.dot"
        archivoDOT = open(archivo, "w")
        archivoDOT.write("digraph{\n")
        archivoDOT.write("rankdir = LR;\n")
        archivoDOT.write(
            'node [fontname = "Arial Black"; fontsize = 14; margin = "0.2,0.1";];\n')
        archivoDOT.write('edge [color = "#008cff";];\n')

        listaActores = []
        for pelicula in lista_peliculas:
            nodo = ('"'+pelicula.titulo+'"[shape = record;color = red;style = diagonals;label ="' +
                    pelicula.titulo+'| {'+pelicula.anio+' | '+pelicula.genero+'}";margin = "0.3,0.2";fontsize = 10;];\n')
            archivoDOT.write(nodo)

            for actor in pelicula.actores:
                if actor not in listaActores:
                    listaActores.append(actor)

        for actor in listaActores:
            nodo = ('"'+actor+'"[shape = box;color = purple;label ="' +
                    actor+'";margin = "0.3,0.2";fontsize = 10;];\n')
            archivoDOT.write(nodo)

        for pelicula in lista_peliculas:
            for actorP in pelicula.actores:
                for actorL in listaActores:
                    if actorP == actorL:
                        nodo = ('"'+pelicula.titulo+'"'+'->'+'"'+actorP+'"\n')
                        archivoDOT.write(nodo)
        archivoDOT.write("}\n")
        archivoDOT.close()
        os.system("dot.exe -Tpng "+archivo+" -o " +
                  archivo.replace(".dot", ".png"))

        print("     [✓] Renderizacion completa!")
        input("     Presiona una tecla para continuar...")
    except:
        input("\n     [X] Hubo un error al graficar!"
              "\n     Presiona una tecla para continuar...")
