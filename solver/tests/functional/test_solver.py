import pytest
from solver.main import ArgumentException


def test_no_roots(solver):
    a, b, c = 2, 0, 1
    result = solver.solve(a, b, c)

    assert [] == result


def test_one_root(solver):
    a, b, c = 1, -2, 1
    result = solver.solve(a, b, c)
    root = -b/(2 * a)

    assert [root, root] == result


def test_two_roots(solver):
    a, b, c = 1, 0, -1
    result = solver.solve(a, b, c)

    assert [-1, 1] == sorted(result)


@pytest.mark.parametrize(
    ('a,b,c'),
    [
        (0, 1, 2),
        (1e-6, 1, 2),
    ]
)
def test_a_non_zero_raises_exception(a, b, c, solver):
    with pytest.raises(ArgumentException):
        solver.solve(a, b, c)


@pytest.mark.parametrize(
    ('a,b,c'),
    [
        (3, 1, '2'),
        (3, '1', '2'),
        ('3', '1', '2')
    ]
)
def test_non_numeric_coeffs_raise_exception(a, b, c, solver):
    with pytest.raises(ArgumentException):
        solver.solve(a, b, c)
