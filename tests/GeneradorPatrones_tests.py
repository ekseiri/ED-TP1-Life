# coding: utf8
from nose import with_setup
from nose.tools import *
from Life.GeneradorPatrones import *
from Life.tablero import Tablero


def setup():
    global t
    t = Tablero(5, 5)

    t._tablero = [[1, 0, 0, 0, 0],
                  [0, 0, 1, 1, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [1, 0, 0, 0, 0]]


def teardown():
    pass


@with_setup(setup)
def test_cantidad_de_vecinos_correcta():
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 0, 0), 0)
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 1, 2), 2)
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 1, 3), 2)
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 2, 2), 6)
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 2, 3), 4)
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 3, 1), 2)
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 3, 2), 3)
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 3, 3), 2)
    assert_equal(GeneradorPatrones.vecinos(t._tablero, 4, 0), 1)


@with_setup(setup)
def test_avance_correcto_del_patron():
    proximo = GeneradorPatrones.nextStep(t._tablero)
    assert_equal(proximo, [[0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0],
                           [0, 1, 0, 0, 1],
                           [0, 1, 1, 1, 0],
                           [0, 1, 1, 0, 0]])

    proximo = GeneradorPatrones.nextStep(proximo)
    assert_equal(proximo, [[0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0],
                           [0, 1, 0, 0, 1],
                           [1, 0, 0, 1, 0],
                           [0, 1, 0, 1, 0]])

    proximo = GeneradorPatrones.nextStep(proximo)
    assert_equal(proximo, [[0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0],
                           [0, 1, 0, 0, 1],
                           [1, 1, 0, 1, 1],
                           [0, 0, 1, 0, 0]])

    t2 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

    proximo = GeneradorPatrones.nextStep(t2)
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

    t3 = [[0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

    proximo = GeneradorPatrones.nextStep(t3)
    assert_equal(proximo, [[0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0],
                           [0, 0, 1, 1, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])
