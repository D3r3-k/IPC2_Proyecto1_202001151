# LISTAS
from Listas.ListaPisos import ListaPisos
from Listas.ListaPatrones import ListaPatrones
from Listas.ListaAzulejos import ListaAzulejos
# CLASES
from Clases.Piso import Piso
from Clases.Patron import Patron
from Clases.Azulejo import Azulejo
# OTROS
from xml.dom import minidom
import os


def leerXML(path):
    xml = minidom.parse(path)
    pisos = xml.getElementsByTagName("piso")
    for piso in pisos:
        # Datos del piso
        _nombre = piso.getAttribute("nombre")
        _filas = int(piso.getElementsByTagName("R")[0].firstChild.data)
        _columnas = int(piso.getElementsByTagName("C")[0].firstChild.data)
        _precio_voltear = int(
            piso.getElementsByTagName("F")[0].firstChild.data)
        _precio_intercambiar = int(
            piso.getElementsByTagName("S")[0].firstChild.data)
        _lista_patrones = ListaPatrones()

        patrones_tag = piso.getElementsByTagName("patrones")[0]
        patrones = patrones_tag.getElementsByTagName("patron")
        for patron in patrones:
            # Datos de los patrones
            _codigo = str(patron.getAttribute("codigo")).strip()
            azulejos = str(patron.firstChild.data).strip()

            _lista_azulejos = ListaAzulejos()
            for char in azulejos:
                # Datos de los azulejos
                _azulejo = Azulejo(char)
                _lista_azulejos.insertar(_azulejo)
            nuevo_patron = Patron(_codigo, _lista_azulejos)
            _lista_patrones.insertar(nuevo_patron)
        nuevo_piso = Piso(_nombre,
                          _filas,
                          _columnas,
                          _precio_voltear,
                          _precio_intercambiar,
                          _lista_patrones)
        lista_pisos.insertar(nuevo_piso)
    print("Datos cargados con éxito")


def mostrarMenu():
    salir = False
    while not salir:
        print("\n"*2)
        print("|==============[ <MENU> ]=============|")
        print("| 1. Cargar datos                     |")
        print("| 2. Seleccionar Piso                 |")
        print("| 3. Ver Pisos                        |")
        print("| 4. Salir                            |")
        print("|=============[ </MENU> ]=============|")
        option = input("Ingrese una Opción: ")
        match option:
            case "1":
                path = menu_cargar_archivos()
                if not os.path.exists(path):
                    raise FileNotFoundError(f"No se encontró el archivo {path}")
                leerXML(path)
                input("Presione enter para continuar...\n\n")
            case "2":
                print("Mostrando datos")
            case "3":
                lista_pisos.imprimir()
            case "4":
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
                print(f"| {index+1}. {archivo} {' ' *
                                                (30-len(str(index+1))-len(archivo))}|")
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


def menu_seleccionar_piso():
    print("\n"*2)
    print("|==============[ <PISOS> ]============|")
    print("| 1. Mostrar gráficamente el patron   |")
    print("| 2. Ver Lista de pisos               |")
    print("| 3. Ver Lista de patrones            |")
    print("| 4. Regresar                         |")
    print("|=============[ </PISOS> ]============|")
    option = input("Ingrese una Opción: ")
    match option:
        case "1":
            pass
        case "2":
            pass
        case "3":
            return
        case _:
            print("Opción no valida")


def main():
    try:
        mostrarMenu()
    except Exception as error:
        print(f"Error: {error}")
        input("Presione enter para continuar...")


if __name__ == "__main__":
    patron_actual = None
    lista_pisos = ListaPisos()
    main()
