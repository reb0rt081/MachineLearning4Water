# BaseLib.py
from BaseLib.py import Sum

def test_Sum():
    assert Sum(2, 3) == 5
    assert Sum(-1, 1) == 0
    assert Sum(0, 0) == 0