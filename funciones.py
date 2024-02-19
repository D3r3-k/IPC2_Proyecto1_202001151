# OTROS
from xml.dom import minidom
import os
# LISTAS
from Listas.ListaPisos import ListaPisos
from Listas.ListaPatrones import ListaPatrones
from Listas.ListaAzulejos import ListaAzulejos
# CLASES
from Clases.Piso import Piso
from Clases.Patron import Patron
from Clases.Azulejo import Azulejo
# LISTAS
lista_pisos = ListaPisos()
# GLOBALS
piso_seleccionado = None
patron_seleccionado = None

# FUNCIONES
def limpiar():
    print("\033c", end="")


def menu_cargar_archivos():
    while True:
        try:
            limpiar()
            print("|=========[ <CARGAR ARCHIVOS> ]========|")
            print("| 1. Ver Disponibles                   |")
            print("| 2. Ingresar directorio               |")
            print("| 3. Regresar                          |")
            print("|========[ </CARGAR ARCHIVOS> ]========|")
            option = input("Ingrese una Opción: ")
            match option:
                case "1":
                    path = menu_seleccionar_archivo()
                    if path:
                        return path
                case "2":
                    path = input("Ingrese la ubicación del archivo: ")
                    return path
                case "3":
                    return
                case _:
                    input("\nOpción no valida!"
                          "\nPresione una tecla para continuar...\n\n")
        except Exception as error:
            input(f"\nError: {error}"
                  "\nPresione una tecla para continuar...\n\n")


def menu_seleccionar_archivo():
    limpiar()
    archivos = os.listdir("Archivos")
    print("|=========[ <DISPONIBLES> ]========|")
    for archivo, index in zip(archivos, range(len(archivos))):
        print(f"| {index+1}. {archivo} "
              f"{' ' * (30-len(str(index+1))-len(archivo))}|")
    print("|========[ </DISPONIBLES> ]========|")
    print("| Para regresar presione           |"
          "\n| cualquier cualquier tecla        |")
    print("|==================================|")
    try:
        option_file = int(input("Ingrese el número del archivo: "))
        match option_file:
            case index if index in range(1, len(archivos)+1):
                path = f"Archivos/{archivos[option_file-1]}"
                return path
            case _:
                input("\nOpción no valida!"
                      "\nPresione una tecla para continuar...")
    except Exception:
        return None


def menu_seleccionar_piso():
    limpiar()
    print("|==============[ <PISOS> ]============|")
    print("| 1. Mostrar gráficamente el patron   |")
    print("| 2. Ver Lista de pisos               |")
    print("| 3. Regresar                         |")
    print("|====================================|")
    option = input("Ingrese una Opción: ")
    match option:
        case "1":
            pass
        case "2":
            lista_pisos.imprimir()
        case "3":
            return
        case _:
            input("\nOpción no valida!"
                  "\nPresione una tecla para continuar...\n\n")


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
    input("\n[✓] El archivo se ha cargado correctamente!"
          "\nPresiona una tecla para continuar...")
