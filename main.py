from funciones import *

def main():
    salir = False
    while not salir:
        try:
            limpiar()
            print("|==============[ <MENU> ]=============|")
            print("| 1. Cargar Archivo                   |")
            print("| 2. Seleccionar Piso                 |")
            print("| 3. Ver Pisos                        |")
            print("| 4. Salir                            |")
            print("|=============[ </MENU> ]=============|")
            option = input("Ingrese una Opción: ")
            match option:
                case "1":
                    path = menu_cargar_archivos()
                    if path:
                        leerXML(path)
                case "2":
                    # menu_seleccionar_piso()
                    pass
                case "3":
                    lista_pisos.imprimir()
                case "4":
                    salir = True
                case _:
                    input("\nOpción no valida!"
                          "\nPresione una tecla para continuar...\n\n")
        except Exception as error:
            input(f"\nError: {error}"
                  "\nPresione una tecla para continuar...\n\n")


if __name__ == "__main__":
    limpiar()
    main()
