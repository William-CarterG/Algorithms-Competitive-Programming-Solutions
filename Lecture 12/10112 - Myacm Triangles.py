import sys
import io

# Problem 4
txt = """6
A 1 0
B 4 0
C 0 3
D 1 3
E 4 4
F 0 6
4
A 0 0
B 1 0
C 99 0
D 99 99
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

class Monument:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

def area(v1, v2, v3):
    return abs(0.5 * ((v3.y - v1.y) * (v2.x - v1.x) - (v2.y - v1.y) * (v3.x - v1.x)))

def contains_point(triangle, p):
    total_area = area(p, triangle.v1, triangle.v2) + area(p, triangle.v1, triangle.v3) + area(p, triangle.v2, triangle.v3)
    triangle_area = area(triangle.v1, triangle.v2, triangle.v3)
    difference = abs(total_area - triangle_area)
    return difference <= 1e-7

def P4():
    while True:
        n = int(stdin.readline())
        if n == 0:
            return
        
        monuments = []
        for _ in range(n):
            label, x, y = stdin.readline().split()
            monument = Monument(label, float(x), float(y))
            monuments.append(monument)
        
        labels = []
        max_area = 0.0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    area = area(monuments[i], monuments[j], monuments[k])
                    if area > max_area:
                        for l in range(n):
                            if l != i and l != j and l != k:
                                t = Triangle(monuments[i], monuments[j], monuments[k])
                                if contains_point(t, monuments[l]):
                                    break
                        else:
                            max_area = area
                            labels = [monuments[i].label, monuments[j].label, monuments[k].label]
        print("".join(labels))

P4()