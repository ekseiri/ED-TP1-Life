from nose.tools import *
from Life.GeneradorPatrones import *
from Life.tablero import Tablero

t = []


def setUp():
    t = Tablero(5, 5, 8)

    t.tablero = [[1, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 0],
                 [1, 0, 0, 0, 0]]


def teardown():
    pass


def test_cantidad_de_vecinos_correcta():
    assert_equal(GeneradorPatrones.vecinos(t, 0, 0), 0)
    assert_equal(GeneradorPatrones.vecinos(t, 1, 2), 2)
    assert_equal(GeneradorPatrones.vecinos(t, 1, 3), 2)
    assert_equal(GeneradorPatrones.vecinos(t, 2, 3), 4)
    assert_equal(GeneradorPatrones.vecinos(t, 3, 1), 2)
    assert_equal(GeneradorPatrones.vecinos(t, 3, 2), 2)
    assert_equal(GeneradorPatrones.vecinos(t, 3, 3), 2)
    assert_equal(GeneradorPatrones.vecinos(t, 4, 0), 1)


def test_avance_correcto_del_patron():
    proximo = GeneradorPatrones.nextStep(t)
    assert_equal(proximo, [[0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0],
                           [0, 1, 1, 0, 1],
                           [0, 1, 1, 1, 0],
                           [0, 1, 1, 0, 0]])

    proximo = GeneradorPatrones.nextStep(proximo)
    assert_equal(proximo, [[0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 0],
                           [0, 0, 0, 0, 1],
                           [1, 0, 0, 0, 0],
                           [0, 1, 0, 1, 0]])

    proximo = GeneradorPatrones.nextStep(proximo)
    assert_equal(proximo, [[0, 0, 1, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])

    proximo = GeneradorPatrones.nextStep(proximo)
    assert_equal(proximo, [[0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])
