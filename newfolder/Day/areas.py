# def square(length):
#     return f"The area of that square is {length * length}"
#
# def rect(length, height):
#     return f"The area of that rectangle is {length * height}"
#
# import math
# def circle(r):
#     return f"The area of that circle is {round(math.pi * r**2,2)}"

def multiply(x,y):
    """
    Accepts 2 numbers and returns them multiplied
    >>> multiply(34,55)
    1870

    """
    return x*y

def add(x,y):
    """
    takes 2 numbers and returns them added

    >>> add(23,50)
    73

    :param x:
    :param y:
    :return:
    """
    return x+y

def main():
    print(f"4*3 = {multiply(4,3)}")



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()