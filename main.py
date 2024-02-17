from xml.dom import minidom
import os

# PASOS PARA EL PROYECTO
# - leer el archivo XML
# - Guardar en listas:
#   - Pisos
#   - Patrones
#   - Azulejos


def leerXML(path):
    xml = minidom.parse(path)
    pisos = xml.getElementsByTagName("piso")
    index = 0
    print("=====================================")
    for piso in pisos:
        print(piso.getAttribute("nombre"))
        print("R: ", int(piso.getElementsByTagName("R")[0].firstChild.data))
        print("C: ", int(piso.getElementsByTagName("C")[0].firstChild.data))
        print("F: ", int(piso.getElementsByTagName("F")[0].firstChild.data))
        print("S: ", int(piso.getElementsByTagName("S")[0].firstChild.data))
        patrones_tag = piso.getElementsByTagName("patrones")[0]
        patrones = patrones_tag.getElementsByTagName("patron")
        for patron in patrones:
            print(" Código: ", str(patron.getAttribute("codigo")).strip())
            print(" Patron: ", str(patron.firstChild.data).strip())
        index += 1
        if index < len(pisos):
            print("=====================================")


def mostrarMenu():
    salir = False
    while not salir:
        print("\n"*2)
        print("|==============[ <MENU> ]=============|")
        print("| 1. Cargar datos                     |")
        print("| 2. Ver Pisos                        |")
        print("| 3. Seleccionar Piso                 |")
        print("| 3. Seleccionar Patron               |")
        print("| 5. Salir                            |")
        print("|=============[ </MENU> ]=============|")
        option = input("Ingrese una Opción: ")
        match option:
            case "1":
                path = menu_cargar_archivos()
                if path:
                    leerXML(path)
                    input("Presione enter para continuar...")
            case "2":
                print("Mostrando datos")
            case "5":
                salir = True
            case _:
                print("Opción no valida")


def menu_cargar_archivos():
    print("\n"*2)
    print("|=========[ <CARGAR ARCHIVOS> ]========|")
    print("| 1. Ver Disponibles                   |")
    print("| 2. Ingresar directorio               |")
    print("| 3. Regresar                          |")
    print("|========[ </CARGAR ARCHIVOS> ]========|")
    option = input("Ingrese una Opción: ")
    match option:
        case "1":
            archivos = os.listdir("Archivos")
            print("\n"*2)
            print("|=========[ <DISPONIBLES> ]========|")
            for archivo, index in zip(archivos, range(len(archivos))):
                print(f"| {index+1}. {archivo} {' '*(30-len(str(index+1))-len(archivo))}|")
            print("|========[ </DISPONIBLES> ]========|")
            index = input("Ingrese el número del archivo: ")
            path = "Archivos/"+archivos[int(index)-1]
            return path            
        case "2":
            path = input("Ingrese la ubicación del archivo: ")
            return path
        case "3":
            return
        case _:
            print("Opción no valida")


def main():
    mostrarMenu()


if __name__ == "__main__":
    main()
