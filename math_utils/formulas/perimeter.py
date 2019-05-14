from math import pi


def square(side):
    return side * 4


def rectangle(length, width):
    return length * 2 + width * 2


def triangle(side1, side2, side3):
    return side1 + side2 + side3


def perimeter(*args):
    if len(args) == 1:
        args = args[0]
    result = 0
    for x in args:
        result += x
    return result


def circle(diameter, pi=pi):
    return pi * diameter
