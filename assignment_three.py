def area_of_rectangle(l,w):
    """
    Calculating the Area of a rectangle
    :param l: Length of rectangle
    :param w:
    :return:
    """
    a = l *w
    return a
def surface_area(l,w,h):
    """
    Calculating the surface area of a rectangular prism
    :param l: length of prism
    :param w: width of prism
    :param h: height of prism
    :return: the product of length, width, and height
    """
    sa = area_of_rectangle(l,w) * 2 + area_of_rectangle(w,h) * 2 + area_of_rectangle(l,h) * 2
    return sa

def instructions():
    print("This program calculates the surface area of a rectangular prism.")

def ask_width():
    print("Enter the width of the prism.")

def ask_length():
    print("Enter the length of the prism.")


def ask_height():
    print("Enter the height of the prism.")