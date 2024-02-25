# OTROS
from xml.dom import minidom
import os
from Graficar import *
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
piso_seleccionado: Piso = None
patron_seleccionado: Patron = None



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
                    if os.path.exists(path):
                        return path
                    else:
                        input("\n[✗] El archivo no existe!"
                              "\nPresione una tecla para continuar...")
                case "3":
                    return
                case _:
                    input("\n[✗] Opción no valida!"
                          "\nPresione una tecla para continuar...\n\n")
        except Exception as error:
            input(f"\nError: {error}"
                  "\nPresione una tecla para continuar...\n\n")


def menu_seleccionar_archivo():
    while True:
        try:
            limpiar()
            archivos = os.listdir("Archivos")
            print("|=========[ <DISPONIBLES> ]========|")
            for archivo, index in zip(archivos, range(len(archivos))):
                print(f"| {index+1}. {archivo} "
                      f"{' ' * (30-len(str(index+1))-len(archivo))}|")
            print("|========[ </DISPONIBLES> ]========|")
            print("| Presione E para salir            |")
            print("|==================================|")
            option_file = input("Ingrese el número del archivo: ")
            if option_file.upper() == "E":
                return
            elif not option_file.isdigit():
                option_file = -1
            option_file = int(option_file)
            match option_file:
                case index if index in range(1, len(archivos)+1):
                    path = f"Archivos/{archivos[option_file-1]}"
                    return path
                case _:
                    input("\n[✗] Opción no valida!"
                          "\nPresione una tecla para continuar...")
        except Exception as error:
            input(f"\nError: {error}"
                  "\nPresione una tecla para continuar...\n\n")
            return None


def menu_seleccionar_piso():
    global piso_seleccionado
    global patron_seleccionado

    if piso_seleccionado and patron_seleccionado:
        while True:
            limpiar()
            print("|======[ <OPCIONES DE PATRON> ]=======|")
            print("| 1. Mostrar gráficamente el patron   |")
            print("| 2. Seleccionar un nuevo patron      |")
            print("| 3. Regresar                         |")
            print("|=====================================|")
            option = input("Ingrese una Opción: ")
            match option:
                case "1":
                    graficar_patron(piso_seleccionado, patron_seleccionado)
                    pass
                case "2":
                    menu_seleccionar_patron()
                    pass
                case "3":
                    return
                case _:
                    input("\n[✗] Opción no valida!"
                          "\nPresione una tecla para continuar...\n\n")
    else:
        while True:
            limpiar()
            print("|======[ <SELECCIONAR DE PISO> ]======|")
            lista_pisos.listar_pisos()
            if len(lista_pisos) > 0:
                print("|=====================================|")
                print("| Presione E para salir               |")
                print("|=====================================|")
                option_piso = input("Ingrese el número del piso: ")
            else:
                option_piso = "E"
            if option_piso.upper() == "E":
                return
            elif not option_piso.isdigit():
                option_piso = -1
            option_piso = int(option_piso)
            match option_piso:
                case index if index in range(1, len(lista_pisos)+1):
                    piso_seleccionado = lista_pisos.buscar_indice(option_piso-1).objeto
                    input(f"\n[✓] Piso seleccionado: {piso_seleccionado.nombre}")
                    menu_seleccionar_patron()
                    return
                case _:
                    input("\n[✗] Opción no valida!"
                          "\nPresione una tecla para continuar...\n\n")

def menu_seleccionar_patron():
    global piso_seleccionado
    global patron_seleccionado

    if piso_seleccionado:
        while True:
            limpiar()
            print("|==============[ <PATRONES> ]============|")
            piso_seleccionado.lista_patrones.listar_patrones(piso_seleccionado.columnas)
            if len(piso_seleccionado.lista_patrones) > 0:
                print("|========================================|")
                print("| Presione E para salir                  |")
                print("|========================================|")
                option_patron = input("Ingrese el número del patrón: ")
            else:
                option_patron = "E"
            if option_patron.upper() == "E":
                return
            elif not option_patron.isdigit():
                option_patron = -1
            option_patron = int(option_patron)
            match option_patron:
                case index if index in range(1, len(piso_seleccionado.lista_patrones)+1):
                    patron_seleccionado = piso_seleccionado.lista_patrones.buscar_indice(option_patron-1).objeto
                    input(f"\n[✓] Patrón seleccionado: {patron_seleccionado.codigo}")
                    return
                case _:
                    input("\n[✗] Opción no valida!"
                          "\nPresione una tecla para continuar...\n\n")
    else:
        input("\n[✗] No se ha seleccionado un piso!"
              "\nPresione una tecla para continuar...\n\n")

def cargar_xml(path):
    global lista_pisos
    global piso_seleccionado
    global patron_seleccionado
    
    lista_pisos.vaciar()
    piso_seleccionado = None
    patron_seleccionado = None

    xml = minidom.parse(path)
    pisos = xml.getElementsByTagName("piso")
    for piso in pisos:
        # Datos del piso
        _nombre = piso.getAttribute("nombre")
        _filas = int(piso.getElementsByTagName("R")[0].firstChild.data)
        _columnas = int(piso.getElementsByTagName("C")[0].firstChild.data)
        _precio_voltear = float(
            piso.getElementsByTagName("F")[0].firstChild.data)
        _precio_intercambiar = float(
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
