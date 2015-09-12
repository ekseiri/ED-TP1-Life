import sys


def menu_main():
    """Menu principal"""

    print ('Menu')
    print ('1.- Nuevo Juego')
    print ('2.- Cargar')
    print ('3.- Salir')
    return input('\n' + 'Seleccion: ')


def menu_game_modes():
    """Menu de seleccion de modo de juego"""

    print ('Modos de Juego')
    print ('1.- Normal')
    print ('2.- Vidas Estaticas')
    print ('3.- Volver')
    return input('\n' + 'Seleccion: ')


def menu_load():
    """Menu de carga de un juego empezado"""

    pass


def main():
    key = ''

    while (key != '3'):
        key = menu_main()

        if (key == '1'):
            modo = menu_game_modes()

            if (modo == '1'):
                """Modo Normal"""
                pass
            elif (modo == '2'):
                """Modo Vidas Estaticas"""
                pass

        elif (key == '2'):
            menu_load()
        elif (key == '3'):
            sys.exit()


if __name__ == "__main__":
    main()
