import sys
import io
import heapq


# Problem 6
# I found this one to be very difficult, so I solved it with a lot of research on the internet that
# explained to me how to solve it. 
txt = """1
4 6
0 1 1
1 2 1
2 3 1
3 0 1
0 2 5
1 3 5
3
1
2
3"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

HOME = 0

# First, we use Dijkstra's algorithm to find the shortest paths.
def dijkstras(storePos, N):
    global S, pathToCost, costAmongStores, costToNodeFromCurrent
    q = []
    costAmongStores = [[0] * S for _ in range(S)]
    costToNodeFromCurrent = [-1] * N

     # Here is the Dijsktra's algortihm implemented. The idea is to:
        # - Initialize priority queue and distance array
        # - Push the starting store node with cost 0 to the queue
        # - Process nodes in the priority queue until it's empty
        #   - Update the distance to each neighboring node if a shorter path is found
        #   - Push the updated nodes to the queue
        # - Store the shortest distances from the starting store to all other nodes
        # - Calculate the cost between each pair of stores and store it in costAmongStores
    for i in range(S - 1):
        costToNodeFromCurrent = [-1] * N
        heapq.heappush(q, (storePos[i], 0))

        while q:
            top = heapq.heappop(q)
            node, cost = top[0], top[1]

            if cost > costToNodeFromCurrent[node] and costToNodeFromCurrent[node] != -1:
                continue

            costToNodeFromCurrent[node] = cost

            for current in pathToCost[node]:
                nextNode, nextCost = current[0], current[1]

                if cost + nextCost < costToNodeFromCurrent[nextNode] or costToNodeFromCurrent[nextNode] == -1:
                    costToNodeFromCurrent[nextNode] = cost + nextCost
                    heapq.heappush(q, (nextNode, cost + nextCost))

        for j in range(i + 1, S):
            otherPos = storePos[j]
            costAmongStores[i][j] = costToNodeFromCurrent[otherPos]
            costAmongStores[j][i] = costToNodeFromCurrent[otherPos]


# Basically the travelling salesman problem.
# Recursive function to find the minimum cost path that visits all stores
def travel(currentNode, cost, travelledBits, best):
    global S, costAmongStores, HOME
    if travelledBits == (1 << S) - 1:
        # Base case: All stores visited, so we calculate cost.
        if cost + costAmongStores[currentNode][HOME] < best:
            best = cost + costAmongStores[currentNode][HOME]
        return best

    for i in range(1, S):
        # Recursive call for visiting next unvisited store
        bit = 1 << i
        if not (bit & travelledBits) and cost + costAmongStores[currentNode][i] < best:
            best = travel(i, cost + costAmongStores[currentNode][i], travelledBits | bit, best)
    return best

T = int(stdin.readline())
storePos = []

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    pathToCost = [[] for _ in range(N)]

    for _ in range(M):
        X, Y, D = map(int, stdin.readline().split())
        pathToCost[X].append((Y, D))
        pathToCost[Y].append((X, D))

    S = int(stdin.readline()) + 1
    storePos = [0] * S

    finished = 1
    for i in range(1, S):
        storePos[i] = int(stdin.readline())
        finished |= 1 << i

    dijkstras(storePos, N)

    bestCost = costAmongStores[S - 1][0]
    for i in range(S - 1):
        bestCost += costAmongStores[i][i + 1]

    # We found the base cost for visiting the stores and now we will use it to find the bestCost recursively.
    # After having searched for all nodes, we will have the minimumCost.
    bestCost = travel(0, 0, 1, bestCost)

    print(bestCost)
