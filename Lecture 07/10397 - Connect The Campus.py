import sys
import io
import math

# Problem 4
txt = """4
103 104
104 100
104 103
100 100
1
4 2
4
103 104
104 100
104 103
100 100
1
4 2"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing).
stdin = sys.stdin

class Building:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(b1, b2):
    return math.sqrt((b1.x - b2.x) ** 2 + (b1.y - b2.y) ** 2)


# Here we use Prim's algorithm because we are interested in finding 
# the tree that minimizes the total weights of the edges of the tree, 
# which is a type of problem this algorithm is very good at solving.
def prim(n, campus):
    total = 0
    low = [1000000000] * n
    low[0] = 0
    visited = {0: True}
    for i in range(n):
        min_p = 0
        min_d = 1000000000
        for j in range(n):
            if not visited.get(j) and min_d > low[j]:
                min_p = j
                min_d = low[j]
        visited[min_p] = True
        total += low[min_p]
        for j in range(n):
            low[j] = min(low[j], campus[min_p][j])
    return total


while True:
    line = stdin.readline().strip()
    if not line:
        break
    n = int(line)
    buildings = []
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        buildings.append(Building(x, y))

    campus = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            campus[i][j] = distance(buildings[i], buildings[j])

    c = int(stdin.readline().strip()) # cables already installed
    for _ in range(c):
        x, y = map(int, stdin.readline().split())
        campus[x-1][y-1] = 0
        campus[y-1][x-1] = 0

    print(f'{prim(n, campus):.2f}')



