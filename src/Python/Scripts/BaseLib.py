def Sum(a, b):
    """Returns the sum of two numbers."""
    return a + b


def DotProduct(v1, v2):
    """
    Returns the dot product of two vectors.
    Raises a ValueError if the vectors have different lengths.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors have different lengths")
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def MatrixSum(m1, m2):
    """
    Returns the element-wise sum of two matrices.
    Raises a ValueError if the matrices have different dimensions.
    """
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Matrices have different dimensions")

    result = []
    for i in range(len(m1)):
        temp_row = []
        for j in range(len(m1[i])):
            temp_row.append(m1[i][j] + m2[i][j])
        result.append(temp_row)
    return result


def MatrixMult(m1, m2):
    """
    Returns the product of two matrices.
    Raises a ValueError if the matrices cannot be multiplied.
    """
    if len(m1[0]) != len(m2):
        raise ValueError("Matrices have incompatible dimensions for multiplication")

    result = []
    for i in range(len(m1)):
        temp_row = []
        for j in range(len(m2[0])):
            pos_val = 0
            for k in range(len(m2)):
                pos_val += m1[i][k] * m2[k][j]
            temp_row.append(pos_val)
        result.append(temp_row)
    return result

"""
    TODO: Define methods matrix determinant, transpose and inverse.
"""
