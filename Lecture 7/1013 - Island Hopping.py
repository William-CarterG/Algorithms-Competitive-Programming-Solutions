import sys
import io
import math

# Problem 2
txt = """7
11 12 2500
14 17 1500
9 9 750
7 15 600
19 16 500
8 18 400
15 21 250
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
#stdin = sys.stdin

class Edge:
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m

    def __lt__(self, other):
        return self.m < other.m

def find_parent(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x], parent)
    return parent[x]

# Performs the union operation in Kruskal's algorithm.
def joint(x, y, parent, population, population2):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    if x == y:
        return 0
    
    if population[x] > population[y]:
        parent[y] = x
        population[x] += population[y]
        population2[x] += population2[y]
    else:
        parent[x] = y
        population[y] += population[x]
        population2[y] += population2[x]
    return 1

# Basically, what we do is find Minimum Spanning Tree (MST) of the given graph, 
# and calculate the average edge population of the MST.
def kruskal(n, X, Y, M):
    parent = list(range(n))

    # Stores the total population of the connected component represented 
    # by the root of the corresponding node's disjoint-set tree.
    population = [1] * n 

    # Stores the population of each individual node in the component.
    population2 = M.copy()
    E = []
    for i in range(n):
        for j in range(i + 1, n):
            v = math.hypot(X[i] - X[j], Y[i] - Y[j])
            E.append(Edge(i, j, v))

    E.sort()
    div = sum(M)

    count = 0
    for i in range(len(E)):
        u = E[i].x
        v = E[i].y
        if find_parent(u, parent) != find_parent(v, parent):
            if find_parent(u, parent) == find_parent(0, parent):
                count += population2[find_parent(v, parent)] * E[i].v
            if find_parent(v, parent) == find_parent(0, parent):
                count += population2[find_parent(u, parent)] * E[i].v
            joint(u, v, parent, population, population2)

    return count / div

def P2():
    cases = 0
    while True:
        n = stdin.readline().strip()
        if n == '0':
            break
        n = int(n)
        X, Y, M = [], [], []
        for _ in range(n):
            x, y, m = map(float, stdin.readline().split())
            X.append(x)
            Y.append(y)
            M.append(m)

        ret = kruskal(n, X, Y, M)
        cases += 1
        print(f"Island Group: {cases} Average {ret:.2f}")

P2()
