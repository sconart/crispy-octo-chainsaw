import pytest
from .compute_product import compute_product
import sys

sys.setrecursionlimit(1500)


@pytest.mark.parametrize(
    "m, n, expected",
    [
        (5, 0, 0),
        (0, 5, 0),
        (3, 4, 12),
        (-3, 4, -12),
        (3, -4, -12),
        (-3, -4, 12),
        (1, 1000, 1000),
    ],
)
def test_compute_product(m, n, expected):
    assert compute_product(m, n) == expected
