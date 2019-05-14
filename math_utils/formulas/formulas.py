from math import sqrt


def distance2d(x1, y1, x2, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def slope_of_line(x1, y1, x2, y2):
    return (y2 - y1) / (x1 - x2)


def distance(rate, time):
    return rate * time
