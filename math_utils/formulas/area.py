from math import pi


def square(side):
    return side ** 2


def rectangle(length, width):
    return length * width


def parallelogram(base, height):
    return base * height


def triangle(base, height):
    return base * height / 2


def circle(radius, pi=pi):
    return pi * radius ** 2


def trapezoid(base1, base2, height):
    return ((base1 + base2) * height) / 2


def sphere(radius, pi=pi):
    return 4 * pi * radius ** 2
