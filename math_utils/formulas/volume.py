from math import pi


def cube(side):
    return side ** 3


def rectangular_container(length, width, height):
    return length * width * height


def square_pyramid(base_length, height):
    return ((base_length ** 2) * height) / 2


def cylinder(radius, height, pi=pi):
    return pi * height * radius ** 2


def cone(radius, height, pi=pi):
    return (height * pi * radius ** 2) / 3


def sphere(radius, pi=pi):
    return (4 / 3) * pi * radius ** 2


def right_circular_cylinder(radius, height, pi=pi):
    return pi * height * radius ** 2
