import sys
from tablero import Tablero
from game import Game


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
    """Menu de load"""
    pass


def menu_pause():
    """Menu de save/load/continue/exit"""
    print ('1.- Continuar')
    print ('2.- Guardar Juego')
    print ('3.- Cargar Juego')
    print ('4.- Volver al menu principal')
    return input('\n' + 'Seleccion: ')


def save_menu():
    pass


def load_menu():
    pass


def main():
    key = ''

    while (key != '3'):
        key = menu_main()

        if (key == '1'):
            modo = menu_game_modes()

            if (modo == '1'):
                """Modo Normal"""
                tab_size = int(input('\n' + 'Tamaño del tablero: '))
                t = Tablero(tab_size, tab_size)
                random_place = input('\n' + 'Usar patron al azar? (s/n): ')

                if (random_place == 's'):
                    cell_alive = int(input('\n' + 'Cantidad '
                                           'de celdas vivas? '))
                    t.fill(cell_alive)

                else:
                    t.manual_fill()

            elif (modo == '2'):
                """Modo Vidas Estaticas"""
                tab_size = int(input('\n' + 'Tamaño del tablero: '))
                cell_alive = int(input('\n' + 'Cantidad de celdas vivas? '))
                t = Tablero(tab_size, tab_size)

            g = Game(int(modo), t)
            g.running = True

            while (g.running):
                print ('running')
                try:
                    g.run()

                except KeyboardInterrupt:
                    key = menu_pause()

                    if (key == '1'):
                        continue
                    elif (key == '2'):
                        save_menu()
                    elif (key == '3'):
                        load_menu()
                    elif (key == '4'):
                        g.running = False

        elif (key == '2'):
            menu_load()
        elif (key == '3'):
            sys.exit()


if __name__ == "__main__":
    main()
