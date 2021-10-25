from calc import Calc


def test_add():
    assert 13 == Calc.add(8, 5)


def test_sub():
    assert 13 == Calc.sub(18, 5)


def test_mul():
    assert 14 == Calc.mul(2, 7)


def test_div():
    assert 2 == Calc.div(10, 5)
