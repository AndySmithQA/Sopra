import sys

def multiply(x, z):
    """
    Accepts two numeric parameters and return product.
    >>> multiply(4, 3)
    12

    :param x (int|float): Integer or float
    :param z (int|float): Integer or float
    :return (int|float): Numeric product of x and z
    """
    return x * z

def add(x, z):
    """
    Accepts two numeric parameters, adds them and returns sum.
    >>> add(4,3)
    7

    :param x (int|float): Integer or float
    :param z (int|float): Integer or float
    :return (int|float): Numeric of x summed with z
    """
    return x + z

def divide(x, z):
    """
    Accepts two numeric parameters, divides first by the second and returns result.
    >>> divide(4, 3)
    '1.333'
    >>> divide(4, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero

    :param x (int|float): Integer or float
    :param z (int|float): Integer or float
    :return (str): f-string of x divided by z to 3 decimal places.
    """
    return f"{x/z:.3f}"

def main():
    """ Single Line docstrings are ideal if the function is self explanatory """
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 / 3 = {divide(4, 3)}")
    #print(f"4 / 3 = {divide(4, 0)}")

    print(multiply.__doc__)
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
    sys.exit(0)