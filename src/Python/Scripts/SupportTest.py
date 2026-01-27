def Validate(actual, expected):
    """
    Asserts that actual == expected.
    """
    if actual != expected:
        message = f"Expected {expected!r}, but got {actual!r}"
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