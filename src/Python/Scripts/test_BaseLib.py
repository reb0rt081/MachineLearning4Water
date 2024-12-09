# Test for module BaseLib.py:
# - Name of this module starts with test_
# - Name of the test method starts with test_
import BaseLib as BL # changed import


def test_Sum():
    assert BL.Sum(2, 3) == 5
    assert BL.Sum(-1, 1) == 0
    assert BL.Sum(0, 0) == 0

def test_DotProduct():
    v1 = [1,0,0]
    v2 = [0,1,0]
    assert BL.DotProduct(v1,v1) == 1
    assert BL.DotProduct(v1,v2) == 0

def test_MatrixSum():
    m1 = [[0,0],[0,0]]
    m2 = [[1,0],[0,1]]
    assert BL.MatrixSum(m1,m1) == [[0,0],[0,0]]
    assert BL.MatrixSum(m1,m2) == [[1,0],[0,1]]
    assert BL.MatrixSum(m2,m2) == [[2,0],[0,2]]

def test_MatrixMult():
    m1 = [[1,0],[0,1]]
    m2 = [[0,1],[1,0]]
    assert BL.MatrixMult(m1,m1) == [[1,0],[0,1]]
    assert BL.MatrixMult(m1,m2) == [[0,1],[1,0]]

def test_MatrixDeterminant():
    m1 = [[1,0],[0,1]]
    m2 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    m3 = [[5,2,9,5,5],[4,4,5,7,7],[1,7,1,3,7],[9,6,7,4,5],[8,6,5,1,9]]
    assert BL.MatrixDeterminant(m1) == 1
    assert BL.MatrixDeterminant(m2) == 1
    assert BL.MatrixDeterminant(m3) == -6154
    
