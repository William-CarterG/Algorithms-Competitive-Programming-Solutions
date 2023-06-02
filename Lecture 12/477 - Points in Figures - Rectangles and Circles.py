import sys
import io

# Problem 2
txt = """r 8.5 17.0 25.5 -8.5
c 20.2 7.3 5.8
r 0.0 10.3 5.5 0.0
c -5.0 -5.0 3.7
r 2.5 12.5 12.5 2.5
c 5.0 15.0 7.2
*
2.0 2.0
4.7 5.3
6.9 11.2
20.0 20.0
17.6 3.2
-5.2 -7.8
9999.9 9999.9"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def contains(self, p):
        return p.x > self.p1.x and p.x < self.p2.x and p.y < self.p1.y and p.y > self.p2.y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def contains(self, p):
        return (p.x - self.center.x) ** 2 + (p.y - self.center.y) ** 2 < self.radius ** 2

def belongs(count, p, shapes):
    in_any = False
    for i, shape in enumerate(shapes):
        if shape.contains(p):
            print(f"Point {count} is contained in figure {i+1}")
            in_any = True
    if not in_any:
        print(f"Point {count} is not contained in any figure")

def P2():
    shapes = []
    flag = False
    count = 1
    for line in stdin.readlines():
        line = line.strip()
        i = 0                 
        if not flag:
            if line[0] == "r":
                p1_x, p1_y, p2_x, p2_y = map(float, line[2:].split())
                shapes.append(Rectangle(Point(p1_x, p1_y), Point(p2_x, p2_y)))
                i += 2
            elif line[0] == "c":
                p_x, p_y, radius = map(float, line[2:].split())
                shapes.append(Circle(Point(p_x, p_y), radius))
                i += 2
            else:
                i += 1
        else:
            p_x, p_y = map(float, line.split())
            if p_x == 9999.9 and p_y == 9999.9:
                break
            belongs(count, Point(p_x, p_y), shapes)
            count += 1

        if line == "*":
            flag = True

P2()
