import sys
import io
import math

# Problem 3
txt = """2
4
5
0 3 1 2 9
7 3 4 9 9
1 7 5 5 3
2 3 4 2 5
1
6
0 1 2 3 4 5"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing).
stdin = sys.stdin

class Node:
    def __init__(self, y, x, cost):
        self.y = y
        self.x = x
        self.cost = cost

    # Special python methon 'less than'.
    def __lt__(self, other):
        return self.cost < other.cost

def dijkstra(n, m, maze):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cost = [[math.inf for _ in range(m)] for _ in range(n)]
    cost[0][0] = maze[0][0]
    visited[0][0] = True
    priority_queue = [Node(0, 0, cost[0][0])]

    # Here we use the Dijkstra algorithm to calculate iteratively the 
    # lower cost to reach any node on the maze.
    while priority_queue:
        curr = min(priority_queue)
        priority_queue.remove(curr)
        for direction_y, direction_x in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            new_y, new_x = curr.y + direction_y, curr.x + direction_x
            if 0 <= new_y < n and 0 <= new_x < m and not visited[new_y][new_x]:
                new_cost = curr.cost + maze[new_y][new_x]
                if new_cost < cost[new_y][new_x]:
                    cost[new_y][new_x] = new_cost
                    visited[new_y][new_x] = True
                    priority_queue.append(Node(new_y, new_x, new_cost))

    # After having calculated all the minimum costs, we just print 
    # the one for the lower right corner of the maze.
    return cost[n - 1][m - 1]

def P3():
    mazes = int(stdin.readline().strip())
    for _ in range(mazes):
        n = int(stdin.readline().strip())
        m = int(stdin.readline().strip())
        maze = [list(map(int, stdin.readline().split())) for _ in range(n)]
        print(str(dijkstra(n, m, maze)))

P3()