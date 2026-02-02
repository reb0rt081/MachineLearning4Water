def Validate(actual, expected):
    """
    Asserts that actual == expected.
    """
    if actual != expected:
        message = f"Expected {expected!r}, but got {actual!r}"
        raise AssertionError(message)

def ValidateValue(actual, expected, tolerance=0.001):
    """
    Asserts that actual is within tolerance of expected.
    """
    if abs(actual - expected) >= tolerance:
        message = (
            f"Expected {expected!r} (tolerance {tolerance}), but got {actual!r} "
            f"(difference={abs(actual - expected)!r})"
        )
        raise AssertionError(message)

def ValidateType(actual, expected):
    """
    Asserts type and that actual == expected.
    """
    assert isinstance(actual, type(expected)), (
        f"Expected type {type(expected).__name__}, "
        f"got {type(actual).__name__}"
    )
    Validate(actual, expected)

def ValidateMatrix(matrix, trueMatrix, tolerance=0.001):
    """
    Asserts that every value in matrix matches trueMatrix within tolerance.
    """    

    # Normalize vectors to 2D
    if matrix and not isinstance(matrix[0], (list, tuple)):
        matrix = [matrix]
        trueMatrix = [trueMatrix]

    # Check dimensions
    if len(matrix) != len(trueMatrix):
        raise AssertionError("Row count mismatch")

    for i, (row, true_row) in enumerate(zip(matrix, trueMatrix)):
        if len(row) != len(true_row):
            raise AssertionError(f"Row {i} length mismatch")

        for j, (value, true_value) in enumerate(zip(row, true_row)):
            try:
                ValidateValue(value, true_value, tolerance)
            except AssertionError as e:
                raise AssertionError(f"Matrix[{i}][{j}] error: {e}") from None