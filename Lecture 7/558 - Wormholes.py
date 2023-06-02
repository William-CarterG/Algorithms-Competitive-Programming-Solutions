import sys
import io

# Problem 1
txt = """2
3 3
0 1 1000
1 2 15
2 1 -42
4 4
0 1 10
1 2 20
2 3 30
3 0 -60"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

class Wormhole:
    def __init__(self, y, t):
        self.y = y  # The final destination star
        self.t = t    # The cost (in time) to make the travel


def P1():
    T = int(stdin.readline().strip())    # Test cases
    
    for _ in range(T):
        N, M = map(int, stdin.readline().split())   # Receive n, m as instructed
        
        wormholes = [[] for _ in range(N)]  # Holds all possible wormholes between the stars
        distances = [10000000000000] * N
        
        for i in range(N):
            wormholes[i].clear()
            distances[i] = 10000000000000   # Just a really big number
        
        # To read lines this way proves very useful when n != m
        while M > 0:
            x, y, t = map(int, stdin.readline().split())
            wormholes[x].append(Wormhole(y, t))
            M -= 1
        
        for t in range(N - 1):
            for j in range(N):
                for m in range(len(wormholes[j])):
                    distances[wormholes[j][m].y] = min(distances[wormholes[j][m].y], distances[j] + wormholes[j][m].t)
        
        flag = False    # Signals whether there is a wormhole that will shorten the distance between two stars
        
        for j in range(N):
            for m in range(len(wormholes[j])):
                if distances[wormholes[j][m].y] > distances[j] + wormholes[j][m].t:
                    flag = True
                    break
            if flag:
                break
        
        print("possible" if flag else "not possible")

P1()