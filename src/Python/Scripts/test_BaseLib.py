# Test for module BaseLib.py:
# - Name of this module starts with test_
# - Name of the test method starts with test_
from BaseLib import Sum

def test_Sum():
    assert Sum(2, 3) == 5
    assert Sum(-1, 1) == 0
    assert Sum(0, 0) == 0