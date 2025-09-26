import pytest
from example import add, factorial, Stats


def test_add():
    assert add(1, 2) == 3.0
    assert add(1.5, 2) == 3.5


def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_stats_mean_variance():
    s = Stats([1, 2, 3, 4])
    assert s.mean() == pytest.approx(2.5)
    assert s.variance() == pytest.approx(1.25)


def test_stats_empty():
    s = Stats([])
    assert s.mean() == 0.0
    assert s.variance() == 0.0
