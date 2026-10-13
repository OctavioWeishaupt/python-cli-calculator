"""Arithmetic operations for the calculator."""


from math import isfinite


def _validate_result(num):
    """Check that a result is a valid real number and return it.

    Args:
        num: The result of an arithmetic operation.

    Returns:
        The same number, if it is valid.

    Raises:
        ValueError: If the result is a complex number.
        OverflowError: If the result is infinite or not a number.
    """
    if isinstance(num, complex):
        raise ValueError
    if not isfinite(num):
        raise OverflowError
    return num

def add(a, b):
    """Return the sum of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.

    Raises:
        OverflowError: If the result is infinite.
    """
    result = a + b
    return _validate_result(result)


def subtract(a, b):
    """Return the difference between two numbers.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The result of a minus b.

    Raises:
        OverflowError: If the result is infinite.
    """
    result = a - b
    return _validate_result(result)


def multiply(a, b):
    """Return the product of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.

    Raises:
        OverflowError: If the result is infinite.
    """
    result = a * b
    return _validate_result(result)


def divide(a, b):
    """Return the quotient of two numbers.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
        OverflowError: If the result is infinite.
    """
    result = a / b
    return _validate_result(result)


def power(a, b):
    """Return a number raised to a power.

    Args:
        a: The base.
        b: The exponent.

    Returns:
        The result of a raised to the power of b.

    Raises:
        ZeroDivisionError: If a is zero and b is negative.
        OverflowError: If the result is too large or infinite.
        ValueError: If the result is a complex number.
    """
    result = a ** b
    return _validate_result(result)
