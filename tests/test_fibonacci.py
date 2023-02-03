import pytest
from algorithms import SlowFibonacci, MemoFibonacci, IterativeFibonacci


@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
])
def test_normal_recurssion(input, expected):
    fib_of = SlowFibonacci()
    assert fib_of(input) == expected


@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (50, 12586269025),
])
def test_memoized_recurssion(input, expected):
    fib_of = MemoFibonacci()
    assert fib_of(input) == expected


@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (50, 12586269025),
    (1000, 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875),
])
def test_iteration(input, expected):
    fib_of = IterativeFibonacci()
    assert fib_of(input) == expected
