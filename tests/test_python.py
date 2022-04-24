"""
Тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot.
"""

import math


def test_filter():
    assert tuple(filter(None, ())) == ()
    assert tuple(filter(None, (1,))) == (1,)
    assert tuple(filter(lambda x: x % 2 == 0, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))) == (0, 2, 4, 6, 8)


def test_map():
    assert tuple(map(lambda x: None, (1,))) == (None,)
    assert tuple(map(lambda x: x, (1, 2, 3))) == (1, 2, 3)


def test_sorted():
    lst = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

    assert tuple(sorted(lst)) == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert tuple(sorted(lst, reverse=True)) == lst
    assert tuple(sorted(lst, key=lambda x: -1 if x % 2 == 0 else 1)) == (8, 6, 4, 2, 0, 9, 7, 5, 3, 1)


def test_pi():
    assert round(math.pi, 2) == 3.14


def test_sqrt():
    assert math.sqrt(1) == 1.0
    assert math.sqrt(4) == 2.0


def test_pow():
    assert math.pow(1, 1) == 1.0
    assert math.pow(1, 2) == 1.0
    assert math.pow(2, 2) == 4.0


def test_hypot():
    assert math.hypot(1) == 1.0
    assert math.hypot(3, 4) == 5.0
    assert math.hypot(3, 4) == math.sqrt(3 ** 2 + 4 ** 2)
    assert math.hypot(1, 1, 1, 1) == 2.0
