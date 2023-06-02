import sys
import io
import math
from collections import defaultdict

# Problem 2
txt = """5
1 1 4 2
2 3 3 1
1 -2.0 8 4
1 4 8 2
3 3 6 -2.0
3
0 0 1 1
1 0 2 1
2 0 3 1
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

close_to_zero = 1e-7

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        if math.isclose(p1.x, p2.x, rel_tol=close_to_zero):
            self.a = 1.0
            self.b = 0.0
            self.c = -p1.x
        else:
            self.a = -(p1.y - p2.y) / (p1.x - p2.x)
            self.b = 1.0
            self.c = -(self.a * p1.x) - p1.y

class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.l = Line(a, b)

    def contains(self, p):
        return (
            p.x >= min(self.a.x, self.b.x) - close_to_zero
            and p.x <= max(self.a.x, self.b.x) + close_to_zero
            and p.y >= min(self.a.y, self.b.y) - close_to_zero
            and p.y <= max(self.a.y, self.b.y) + close_to_zero
        )

def are_parallel(l1, l2):
    return (
        math.isclose(l1.a, l2.a, rel_tol=close_to_zero)
        and math.isclose(l1.b, l2.b, rel_tol=close_to_zero)
    )

def are_same(l1, l2):
    return are_parallel(l1, l2) and math.isclose(l1.c, l2.c, rel_tol=close_to_zero)

def are_intersect(l1, l2, p):
    if are_parallel(l1, l2):
        return False
    p.x = (l2.b * l1.c - l1.b * l2.c) / (l2.a * l1.b - l1.a * l2.b)
    if math.isclose(l1.b, 0.0, rel_tol=close_to_zero):
        p.y = -(l2.a * p.x + l2.c)
    else:
        p.y = -(l1.a * p.x + l1.c)
    return True

def are_touch(s1, s2):
    if are_same(s1.l, s2.l):
        return True
    p = Point(0, 0)
    if are_intersect(s1.l, s2.l, p) and s1.contains(p) and s2.contains(p):
        return True
    return False

def P2():
    while True:
        n = int(stdin.readline().split()[0])
        if n == 0:
            break

        segments = []
        for _ in range(n):
            x1, y1, x2, y2 = map(float, stdin.readline().split())
            segments.append(Segment(Point(x1, y1), Point(x2, y2)))
            

        unique_segments = []
        for i in range(n):
            is_unique = True
            for j in range(i - 1, -1, -1):
                if are_touch(segments[i], segments[j]):
                    is_unique = False
                    break
            if not is_unique:
                unique_segments.append(i + 1)
        
        if len(unique_segments) == 0:
            for i in range(n):
                unique_segments.append(i + 1)

        unique_segments.sort()
        print("Top sticks:", end=" ")
        print(*unique_segments, sep=", ", end=".\n")

P2()
