### Halley Deme
## Date Last Modified : 09/30/2021
# This Program asks a user for three parameters and finds the surface area of a rectangular prism, using those parameters.


def area_of_rectangle(l,w):
    """
    Calculating the Area of a rectangle
    :param l: Length of rectangle
    :param w:width of rectangle.
    :return:area of rectangle
    """
    a = int(l) * int(w)
    return a

def instructions():
    """
    Tells users instructions.

    """
    print("This program calculates the surface area of a rectangular prism.")

def ask_width():
    """
    Asking user for width
    :return: width of prism
    """
    w = input("Enter the width of the prism.")
    return(w)

def ask_length():
    """
    Asking user for width
    :return: width of prism
    """
    l = input("Enter the length of the prism.")
    return(l)


def ask_height():
    """
    Asking user for height
    :return: height of prism
    """
    h = input("Enter the height of the prism.")
    return h

def surface_area(l,w,h):
    """
    Calculating the surface area of a rectangular prism
    :param l: length of prism
    :param w: width of prism
    :param h: height of prism
    :return: the product of length, width, and height
    """
    # This is the formula for surface area of a rectangular prism.
    sa = area_of_rectangle(l,w) * 2 + area_of_rectangle(w,h) * 2 + area_of_rectangle(l,h) * 2
    return sa

def main():
    instructions()
    w = ask_width()
    l = ask_length()
    h = ask_height()
    print("The surface area is:", surface_area(w,l,h))

if __name__ == '__main__':
    main()
