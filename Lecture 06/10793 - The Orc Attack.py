import sys
import io
from collections import defaultdict

#Problem 5
# Solution heavily inspired by: https://github.com/lamphanviet/competitive-programming/blob/master/uva-online-judge/accepted-solutions/10793%20-%20The%20Orc%20Attack.cpp
txt = """2
7 11
1 7 2
2 7 2
3 7 2
5 7 2
6 7 1
1 6 1
2 6 1
3 6 1
4 6 1
5 6 1
7 6 1
6 1
1 2 3"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

INF = 1000000000000

def P5():
    T = int(stdin.readline().strip())
    for test_case in range(1, T+1):
        L, D = map(int, stdin.readline().split())
        c = [[0 if i==j else INF for j in range(L+1)] for i in range(L+1)]

        for i in range(D):
            u, v, cost = map(int, stdin.readline().split())
            c[u][v] = c[v][u] = min(c[u][v], cost)

        for k in range(1, L+1):
            for u in range(1, L+1):
                for v in range(1, L+1):
                    c[u][v] = min(c[u][v], c[u][k]+c[k][v])

            
        ans = INF
        for i in range(6, L+1):
            tmp = c[i][1]
            if tmp != INF:
                cost = c[i][1]
                for j in range(2, 6):
                    if c[i][j] != cost:
                        tmp = INF
                        break
            if tmp != INF:
                for j in range(6, L+1):
                    tmp = max(tmp, c[i][j])
            ans = min(ans, tmp)


        if ans == INF:
            ans = -1
        print("Map {}: {}".format(test_case, ans))

P5()
