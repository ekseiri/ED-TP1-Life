# coding: utf8
import os


class Tools(object):

    def clear():
        if ('win32' not in str.lower(os.sys.platform)):
            print('')
            os.system('clear')
        else:
            print('')
            os.system('cls')

    def calccoord(ancho, coord):
        x = coord // ancho
        y = coord % ancho
        return (x, y)
