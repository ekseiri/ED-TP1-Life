from nose import with_setup
from nose.tools import *
from Life.tablero import Tablero
from Life.GeneradorPatrones import *
from Life.Comparador import *

def setup():
    global t1
    global t2
    global comp

    comp = Comparador()
    t1 = Tablero(5, 5)
    t2 = Tablero(5, 5)

    t1._tablero = [[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]
 
    t2._tablero = [[0, 0, 0, 0, 0],
                   [0, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]


def teardown():
    pass


@with_setup(setup)
def test_estatico():
    assert_equal(comp.comparar(t1._tablero), False)
    assert_equal(comp.comparar(t1._tablero), 1)
    assert_equal(comp.comparar(t1._tablero), 1)
    assert_equal(comp.comparar(t2._tablero), False)
    assert_equal(comp.comparar(GeneradorPatrones.nextStep(t2._tablero)), False)
    assert_equal(comp.comparar(t2._tablero), 2)
    assert_equal(comp.comparar(GeneradorPatrones.nextStep(t2._tablero)), 2)