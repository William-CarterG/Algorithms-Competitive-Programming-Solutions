from collections import deque
import sys
import io

# Problem 6
txt = """4 4
3 5
2 2
1 2 3
1 3 3
2 4 1
3 4 3
4 4
3 2
2 2
1 2 3
1 3 3
2 4 1
3 4 3
0 0"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

from queue import Queue


# Aims to find an augmenting path in the graph, keeping track of the path found.
def find_path(cost, flow, machines):
    global path
    path = [0] * (machines + 1)
    path[1] = machines + 1
    q = deque()
    q.append(1)

    while q:
        u = q.popleft()

        for m in range(1, machines + 1):
            if not path[m] and flow[u][m] < cost[u][m]:
                path[m] = u
                if m == machines:
                    return True
                q.append(m)

    return False

# Flow works sort of as te cost of the wires + the machine as we traverse through the graph.
def inc_flow(cost, flow, machines):
    delta = sys.maxsize
    m = machines
    # Construct the path from the cerver to the target machine.
    while m != 1:
        u = path[m]
        delta = min(delta, cost[u][m] - flow[u][m])
        m = u

    m = machines

    # Updates the flow according to the cost found
    while m != 1:
        u = path[m]
        flow[u][m] += delta
        flow[m][u] -= delta
        m = u

def P6():
    while True:
        machines, wires = map(int, stdin.readline().split())
        if machines == 0 and wires == 0:
            break

        cost = [[0] * (machines + machines + 3) for _ in range(machines + machines + 3)]
        flow = [[0] * (machines + machines + 3) for _ in range(machines + machines + 3)]

        # Boss computer's and central server are not destroyable = Inifinte cost
        cost[1][machines + 1] = cost[machines][machines + machines] = sys.maxsize
        for _ in range(2, machines):
            i, c = map(int, stdin.readline().split())
            cost[i][i + machines] = c

        for _ in range(wires):
            j, k, c = map(int, stdin.readline().split())
            cost[j + machines][k] = c
            cost[k + machines][j] = c

        
        # To make sure we are working with the graph bidirectionally
        machines += machines

        # Finds augmenting paths using the find_path() function and 
        # updates the flow accordingly using inc_flow(). 
        while find_path(cost, flow, machines):
            inc_flow(cost, flow, machines)

        min_cost = 0
        for m in range(1, machines + 1):
            if flow[1][m] > 0:
                min_cost += flow[1][m]

        print(min_cost)

P6()
