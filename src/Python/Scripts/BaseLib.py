def Sum(a, b):
    """Returns the sum of two numbers."""
    return a + b


def DotProduct(v1: list[float], v2: list[float])->list[float]:
    """
    Returns the dot product of two vectors.
    Raises a ValueError if the vectors have different lengths.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors have different lengths")
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def MatrixSum(m1: list[list[float]], m2:list[list[float]])->list[list[float]]:
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


def MatrixMult(m1:list[list[float]], m2: list[list[float]])->list[list[float]]:
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


def determinante(matriz: list[list[float]])->list[list[float]]:
    """
    Calcula el determinante de una matriz utilizando la expansión por cofactores.
    """
    # determinante de una matriz 1x1
    if len(matriz) == 1:
        return matriz[0][0]
    
    # determinante de una matriz 2x2
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    # Expansión por cofactores para matrices de mayor tamaño (Submatrices eliminando filas y columnas)
    det = 0
    for col in range(len(matriz)):  # Iteración por columnas
        # Crear la submatriz al eliminar la primera fila y la columna `col`
        submatriz = []
        for fila in matriz[1:]:  # Iteramos por las filas a partir de la segunda
            submatriz.append(fila[:col] + fila[col+1:])
        
        # Sumar o restar según el signo alternante de la posición
        det += (-1) ** col * matriz[0][col] * determinante(submatriz)  # Llamada recursiva
    
    return det

def transpuesta(matriz:list[list[float]])->list[list[float]]:
    """
    Calcula la transpuesta de una matriz.
    """
    
    result = []
    for i in range(len(matriz[0])):  # Recorremos las columnas
        columna = []
        for j in range(len(matriz)):  # Recorremos las filas
            columna.append(matriz[j][i])
        result.append(columna)
    return result

def inversa(matriz:list[list[float]])->list[list[float]]:
    """
    Calcula la inversa de una matriz utilizando el determinante y la matriz adjunta.
    """
    det = determinante(matriz)
    
    # Si el determinante es 0, la matriz no tiene inversa
    if det == 0:
        raise ValueError("La matriz no tiene inversa, el determinante es 0")
    
    # Para una matriz 2x2, la fórmula es sencilla
    if len(matriz) == 2:
        return [
            [matriz[1][1] / det, -matriz[0][1] / det],
            [-matriz[1][0] / det, matriz[0][0] / det]
        ]
    
    # Para matrices de mayor tamaño, calculamos la matriz adjunta
    adjunta = []
    for i in range(len(matriz)):  # Iteración por las filas
        fila_adjacente = []
        for j in range(len(matriz)):  # Iteración por las columnas
            # Crear la submatriz eliminando la fila `i` y la columna `j`
            submatriz = []
            for k in range(len(matriz)):  # Iteramos por las filas y columnas
                if k != i:  # Evitar la fila i
                    fila_submatriz = []
                    for l in range(len(matriz[k])):  # Iteramos por las columnas
                        if l != j:  # Evitar la columna j
                            fila_submatriz.append(matriz[k][l])
                    submatriz.append(fila_submatriz)
            
            # Cofactor
            cofactor = (-1) ** (i + j) * determinante(submatriz)
            fila_adjacente.append(cofactor)
        adjunta.append(fila_adjacente)
    
    # La matriz inversa es la transpuesta de la adjunta dividida por el determinante
    adjunta_transpuesta = transpuesta(adjunta)
    return [[elemento / det for elemento in fila] for fila in adjunta_transpuesta]

"""
    TODO: Define methods matrix determinant, transpose and inverse.
"""
