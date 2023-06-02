import sys
import io
import math

# Problem 1
txt = """12
3 3
4 6
4 11
4 8
10 6
5 7
6 6
6 3
7 9
10 4
10 9
1 7
5
20 20
20 40
40 20
40 40
30 30
3
10 10
21 10
21 13
-1
5 5
20 12"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def counter_clockwise(p1, p2, p3):
    return (
        (p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p1.y * p2.x - p2.y * p3.x - p3.y * p1.x) > 0
    )

def convex_hull(point):
    point.sort(key=lambda point: (point.x, point.y))

    n = len(point)
    k = 0
    H = [Point(0, 0)] * (2 * n)

    for i in range(n):
        while k >= 2 and not counter_clockwise(H[k - 2], H[k - 1], point[i]):
            k -= 1
        H[k] = point[i]
        k += 1

    t = k
    for i in range(n - 2, -1, -1):
        while k > t and not counter_clockwise(H[k - 2], H[k - 1], point[i]):
            k -= 1
        H[k] = point[i]
        k += 1

    return H[:k - 1]

def point_inside_polygon(point, polygon):
    in_polygon = False
    n = len(polygon)

    for i in range(n):
        j = (i - 1 + n) % n
        if (
            (polygon[i].y <= point.y < polygon[j].y)
            or (polygon[j].y <= point.y < polygon[i].y)
        ):
            if (
                point.x - 1e-9 < (
                    (polygon[j].x - polygon[i].x) * (point.y - polygon[i].y) / (polygon[j].y - polygon[i].y)
                    + polygon[i].x
                )
            ):
                in_polygon ^= True

    return in_polygon

def affected_area(polygon):
    n = len(polygon)
    S = 0

    for i in range(1, n):
        S += polygon[i].x * (polygon[(i + 1) % n].y - polygon[i - 1].y)
    S += polygon[0].x * (polygon[1].y - polygon[n - 1].y)

    return S / 2.0

def P1():
    WORLD = []
    while True:
        N = int(stdin.readline())
        if N == -1:
            break
        
        kindgom = []
        for _ in range(N):
            x, y = map(int, stdin.readline().split()) # Power Station and houses locations.
            kindgom.append(Point(x, y))
        
        kingdom = convex_hull(kindgom)
        WORLD.append(kingdom)
    
    valid = [True] * len(WORLD)
    
    while True:
        try:
            x, y = map(int, stdin.readline().split())   # Missile landing location.
            for i in range(len(WORLD)):
                if not valid[i]:
                    continue
                if point_inside_polygon(Point(x, y), WORLD[i]):
                    valid[i] = False
                    break
        except ValueError:
            break
    
    S = 0.0
    for i in range(len(WORLD)):
        if not valid[i]:
            S += math.fabs(affected_area(WORLD[i]))
    
    print(f"{S:.2f}")

P1()