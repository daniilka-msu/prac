class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = tuple(p1)
        self.p2 = tuple(p2)
        self.p3 = tuple(p3)

    def __abs__(self):
        def distance(p, q):
            return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5

        lengths = [distance(self.p1, self.p2), distance(self.p2, self.p3), distance(self.p3, self.p1)]
        if 2 * max(lengths) < sum(lengths):
            return 0.5 * abs((self.p2[0] - self.p1[0]) * (self.p3[1] - self.p1[1]) - (self.p3[0] - self.p1[0]) * (self.p2[1] - self.p1[1]))
        return 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __bool__(self):
        return abs(self) > 0

    def __contains__(self, other):
        def cross_product(a, b, c):
            return (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])

        def is_inside(pt, v1, v2, v3):
            b1 = cross_product(pt, v1, v2) <= 0.0
            b2 = cross_product(pt, v2, v3) <= 0.0
            b3 = cross_product(pt, v3, v1) <= 0.0
            return (b1 == b2) and (b2 == b3)

        if not other:
            return True
        if not self:
            return True
        return (is_inside(other.p1, self.p1, self.p2, self.p3) and
                is_inside(other.p2, self.p1, self.p2, self.p3) and
                is_inside(other.p3, self.p1, self.p2, self.p3))

    def __and__(self, other):
        def counter_clockwise(A, B, C):
            return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

        def do_intersect(A, B, C, D):
            return counter_clockwise(A, C, D) != counter_clockwise(B, C, D) and counter_clockwise(A, B, C) != counter_clockwise(A, B, D)

        if not other or not self:
            return False

        edges_self = [(self.p1, self.p2), (self.p2, self.p3), (self.p3, self.p1)]
        edges_other = [(other.p1, other.p2), (other.p2, other.p3), (other.p3, other.p1)]

        for edge_self in edges_self:
            for edge_other in edges_other:
                if do_intersect(edge_self[0], edge_self[1], edge_other[0], edge_other[1]):
                    return True

        return self in other or other in self


import sys

exec(sys.stdin.read())

