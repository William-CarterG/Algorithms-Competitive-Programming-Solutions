import sys
import io

#Problem 4
# Solution heavily inspired by: https://github.com/Diusrex/UVA-Solutions/blob/master/10687%20Monitoring%20the%20Amazon.cpp
txt = """4 
1 0 0 1 -1 0 0 -1
8 
1 0 1 1 0 1 -1 1 -1 0 -1 -1 0 -1 1 -1
6 
0 3 0 4 1 3 -1 3 -1 -4 -2 -5
0"""

stdin = io.StringIO(txt)
#Actual use (Comment the below line for testing)
stdin = sys.stdin

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

def square(num):
    return num * num

def find_closest_for_all(points, n, two_neighbors):
    n = len(points)
    for i in range(n):
        two_neighbors[i][0], two_neighbors[i][1] = -1, -1
        first_distance, second_distance = 1000000000000, 1000000000000
        
        for j in range(n):
            if i != j:
                sq_distance = (points[i].x - points[j].x)**2 +(points[i].y - points[j].y)**2
                if two_neighbors[i][0] == -1 or first_distance > sq_distance:
                    two_neighbors[i][1] = two_neighbors[i][0]
                    second_distance = first_distance
                    
                    two_neighbors[i][0] = j
                    first_distance = sq_distance
                elif two_neighbors[i][1] == -1 or second_distance > sq_distance:
                    two_neighbors[i][1] = j
                    second_distance = sq_distance

def dfs(node, two_neighbors, reached):
    if node == -1 or reached[node]:
        return 0
    reached[node] = True
    return 1 + dfs(two_neighbors[node][0], two_neighbors, reached) + dfs(two_neighbors[node][1], two_neighbors, reached)


while True:
    n = int(stdin.readline().strip())
    if n == 0:
        break
    data = list(map(int, stdin.readline().split()))

    points= []
    for i in range(0, len(data), 2):
        points.append(Point(data[i], data[i+1]))

    station = points[0]
    points.sort(key=lambda p: (p.x, p.y))
    two_neighbors = [[-1, -1] for _ in range(n)]
    find_closest_for_all(points, n, two_neighbors)

    reached = [False] * n
    valid = False
    for i in range(n):
        if station.x == points[i].x and station.y == points[i].y:
            valid = (dfs(i, two_neighbors, reached) == n)

    if valid:
        print("All stations are reachable.")
    else:
        print("There are stations that are unreachable.")
