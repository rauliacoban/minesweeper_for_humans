from settings import *


def valid(coords):
    return coords[0] >= 0 and coords[1] >= 0 and coords[0] < CELL_HEIGHT and coords[1] < CELL_WIDTH


def add_coords(a, b): return (a[0] + b[0], a[1] + b[1])
