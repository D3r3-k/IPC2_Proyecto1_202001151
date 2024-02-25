from funciones import *

def main():
    global piso_seleccionado
    global patron_seleccionado
    while True:
        try:
            limpiar()
            print("|==============[ <MENU> ]=============|")
            print("| 1. Cargar Archivo                   |")
            print("| 2. Opciones de Pisos                |")
            print("| 3. Ver Pisos                        |")
            print("| 4. Salir                            |")
            print("|=============[ </MENU> ]=============|")
            option = input("Ingrese una Opción: ")
            match option:
                case "1":
                    path = menu_cargar_archivos()
                    if path:
                        cargar_xml(path)
                case "2":
                    menu_seleccionar_piso()
                    pass
                case "3":
                    lista_pisos.ordenar()
                    lista_pisos.imprimir()
                case "4":
                    break
                case _:
                    input("\n[✗] Opción no valida!"
                          "\nPresione una tecla para continuar...\n\n")
        except Exception as error:
            input(f"\nError: {error}"
                  "\nPresione una tecla para continuar...\n\n")


if __name__ == "__main__":
    limpiar()
    main()
