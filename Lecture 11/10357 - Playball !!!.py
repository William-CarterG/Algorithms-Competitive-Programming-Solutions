import sys
import io
import math

# Problem 1
txt = """PLAYERS=9
0 0 3
16 16 2
30 0 4
36 24 4
0 30 3
24 36 5
24 75 7
75 24 6
60 60 7
BALLS=12
-1 3 1 21 3 14 5
-1 1 1 11 3 2 5
-3 4 0 8 5 11 2
-1 2 1 -4 1 6 7
-1 1 0 9 3 14 5
-2 4 1 32 3 12 5
-1 1 1 11 1 19 5
-4 5 0 18 5 20 5
-1 2 1 24 5 6 7
-1 1 0 9 3 4 1
-2 2 1 2 5 22 5
-1 6 1 10 5 13 5"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

global close_to_zero
close_to_zero = 1*(10**(-7))


class Point:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v

def dist(point):
    DX = dx - point.x
    DY = dy - point.y
    return math.sqrt(DX**2 + DY**2)

def minpos():
    if sols < 0.0 + close_to_zero:
        return math.ceil(disc)
    
    if disc < 0.0 + close_to_zero:
        return math.ceil(sols)
    
    if math.ceil(sols) - sols > math.ceil(disc) - disc:
        return math.ceil(sols)
    
    if math.ceil(sols) - sols == math.ceil(disc) - disc:
        return min(math.ceil(sols), math.ceil(disc))
    
    return math.ceil(disc)

line = (stdin.readline().strip().split('='))
n = int(line[1])
players = []
for _ in range(n):
    x, y, v = map(int, stdin.readline().strip().split())
    players.append(Point(x, y, v))

balls = int(stdin.readline().split('=')[1])
for i in range(1, balls+1):
    a, b, c, d, e, f, g = map(int, stdin.readline().split())

    disc = math.sqrt(b*b - 4*a*c)   # discriminant
    sols = (-disc - b) / (2.0 * a)
    disc = (disc - b) / (2.0 * a)

    t = minpos()
    dx = t * d + e
    dy = t * f + g

    if dx < 0 or dy < 0:
        print(f"Ball {i} was foul at ({dx},{dy})")
    else:
        caught = False
        for j in range(n):
            if dist(players[j]) / players[j].v < t + close_to_zero:
                print(f"Ball {i} was caught at ({dx},{dy})")
                caught = True
                break
        if not caught:
            print(f"Ball {i} was safe at ({dx},{dy})")
