import sys
import io

# Problem 6
txt = """2
5
3
0 1
1 2
3 4
2
1
0 1"""

stdin = io.StringIO(txt)

# Actual use (Comment the below line for testing).
stdin = sys.stdin

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)


def P6():
    test_cases = int(stdin.readline())
    for _ in range(test_cases):
        m = int(stdin.readline().strip())
        r = int(stdin.readline().strip())
        graph = [[] for _ in range(m)]
        visited = [False] * m

        # Check for connected roads
        for _ in range(r):
            start, destination = map(int, stdin.readline().split())
            graph[start].append(destination)
            graph[destination].append(start)
        output = 0

        # We find the number of connected components
        for node in range(m):
            if not visited[node]:
                dfs(node, visited, graph)
                output += 1
        print(output - 1)

P6()
