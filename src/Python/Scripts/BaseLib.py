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


def MatrixDeterminant(matrix):
    """
    Calculates the determinant using the cofactor expansion.
    """
    
    if len(matrix) == 1:
        return matrix[0][0]
    
    
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    
    det = 0
    for col in range(len(matrix)):  
        submatrix=[]
        for fila in matrix[1:]:  
            submatrix.append(fila[:col] + fila[col+1:])
        
        
        det += (-1) ** col * matrix[0][col] * MatrixDeterminant(submatrix)  
    return det

def MatrixTranspose(matrix):
    """
    calculates the transposed matrix
    """
    
    result = []
    for i in range(len(matrix[0])):  
        columna = []
        for j in range(len(matrix)):  
            columna.append(matrix[j][i])
        result.append(columna)
    return result

def MatrixInverse(matrix):
    """
    calculates the inverse matrix with determinant and transpose matrix functions    """
    det = MatrixDeterminant(matrix)
    
    
    if det == 0:
        raise ValueError("null determinant")
    
    
    if len(matrix) == 2:
        return [
            [matrix[1][1] / det, -matrix[0][1] / det],
            [-matrix[1][0] / det, matrix[0][0] / det]
        ]
    
    
    adj = []
    for i in range(len(matrix)):  
        adj_row = []
        for j in range(len(matrix)):  
            
            
            submatrix = []
            for k in range(len(matrix)):  
                if k != i:  
                    submatrix_row = []
                    for l in range(len(matrix[k])):
                        if l != j:  
                            submatrix_row.append(matrix[k][l])
                    submatrix.append(submatrix_row)
            
            # Cofactor
            cofactor = (-1) ** (i + j) * MatrixDeterminant(submatrix)
            adj_row.append(cofactor)
        adj.append(adj_row)
    
    
    transpose_adj = MatrixTranspose(adj)
    return [[element / det for element in row] for row in transpose_adj]

"""
    TODO: Define methods matrix determinant, transpose and inverse.
"""
