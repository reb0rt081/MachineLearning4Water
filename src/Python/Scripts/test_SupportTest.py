import SupportTest as ST


def test_Validate():
    ST.Validate(2, 2)
    ST.Validate("Hi", "Hi")
    ST.Validate(True, True)


def test_FailValidateValue():
    try:
        ST.Validate(4, 2)
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected failure for value mismatch")


def test_FailValidateString():
    try:
        ST.Validate("Hi", "Bye")
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected failure for value mismatch")


def test_FailValidateBool():
    try:
        ST.Validate(True, False)
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected failure for value mismatch")


def test_ValidateType():
    ST.ValidateType(2, 2)
    ST.ValidateType("Hi", "Hi")
    ST.ValidateType(True, True)


def test_FailValidateTypeValue():
    try:
        ST.ValidateType(4, 2)
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected failure for value mismatch")


def test_FailValidateTypeString():
    try:
        ST.ValidateType("Hi", "Bye")
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected failure for value mismatch")


def test_FailValidateTypeBool():
    try:
        ST.ValidateType(True, False)
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected failure for value mismatch")


def test_FailValidateType():
    try:
        ST.ValidateType(4, 4.0)
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected failure for type mismatch")
