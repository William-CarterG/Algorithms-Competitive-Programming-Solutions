import sys
import io
from collections import defaultdict

#Problem 2
txt = """3
1 2 0
2 2 0
3 1 2 0
0
3 1 2 3
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
#stdin = sys.stdin

def find_for_neighbor(neighbor, graph):
    tmp = set()
    for vertex in graph[neighbor]:
        # Explore the neighbors of the original neighbor, and add them to set.
        tmp.add(vertex)
    return tmp

def find_reachable(graph, vertex_id, n, reachable):
    tmp = set()
    for neighbor in graph[vertex_id]:
        # Add neighbors as reachable
        tmp.add(neighbor)

    for neighbor in tmp:
        # Explore 'neighbor' neighbors and add them to reachable (if not there already)
        reachable = tmp.union(find_for_neighbor(neighbor, graph))
    return reachable

def P2():
    while True:
        # Read first line of graph for N
        N = (stdin.readline().strip())
        if not N or N == '0':
            return
        N = int(N)
        graph = defaultdict(lambda: [])
        ids = []
        lines= []
        # Save id of vertex
        while True:
            line = list(map(int, stdin.readline().split()))
            if not line[0]:
                break
            line = line[:-1]
            ids.append(line[0])
            lines.append(line)

        # Create graph with id of vertex and possible directions
        for i in range(0, N+1):
            if i in ids:
                for l in lines:
                    if l[0] == i:
                        graph[i] = l[1:]
            else:
                graph[i]

        # Find requested lines
        line = stdin.readline().split()
        for vertex_id in line[1:]:
            output = ""
            reachable = set()
            reachable = (find_reachable(graph, int(vertex_id), N, set()))
            output += str(N - len(reachable)) + " "
            for i in range(1, N+1):
                if i not in reachable:
                    output += str(i) + " "
            print(output)

P2()

