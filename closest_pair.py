"""
identify among all pairs of points that pair which has the smallest distance
"""
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


if __name__ == '__main__':
    p1 = Point(1, 7)
    p2 = Point(4, 1)
    p3 = Point(4, 4)
    p4 = Point(6, 6)
    p5 = Point(5, 8)
    p6 = Point(8, 6)
