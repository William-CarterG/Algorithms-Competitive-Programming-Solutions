import sys
import io

# Problem 1
txt = """5 6
3 4 1 2 8 6
6 1 8 2 7 4
5 9 3 9 9 5
8 4 1 3 2 6
3 7 2 8 6 4
5 6
3 4 1 2 8 6
6 1 8 2 7 4
5 9 3 9 9 5
8 4 1 3 2 6
3 7 2 1 2 3
6 8 
9 1 9 9 1 1 1 1 
1 9 9 1 9 9 9 9 
9 9 1 9 9 1 1 1 
1 1 9 9 1 9 9 9 
9 9 9 1 9 9 9 9 
9 9 1 9 9 9 9 9 
6 7
1 9 9 1 9 9 9
9 1 1 9 9 9 9
9 9 9 9 1 1 1
9 9 9 1 9 9 9
9 9 1 9 9 9 9
9 1 9 9 1 1 1
5 4
9 1 9 9
1 9 9 9
9 9 9 9
1 1 1 1
9 9 1 9
5 6
-3 -4 -1 -2 -8 -6
-6 -1 -8 -2 -7 -4 
-5 -9 -3 -9 -9 -5
-8 -4 -1 -3 -2 -6 
-3 -7 -2 -8 -6 -4"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def tsp(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    dp = [[0] * n for _ in range(m)]
    path = [[100000000000000] * (n-1) for _ in range(m)]
    
    for i in range(m):
        dp[i][n-1] = matrix[i][n-1]
    
    for j in range(n-2, -1, -1):
        for i in range(m):
            path_up = matrix[i][j] + dp[(i-1+m)%m][j+1]
            path_mid = matrix[i][j] + dp[i][j+1]
            path_down = matrix[i][j] + dp[(i+1)%m][j+1]
            minimum_cost = min(path_up, min(path_mid, path_down))
            dp[i][j] = minimum_cost
            if minimum_cost == path_up:
                path[i][j] = min(path[i][j], (i-1+m)%m)
            if minimum_cost == path_mid:
                path[i][j] = min(path[i][j], i)
            if minimum_cost == path_down:
                path[i][j] = min(path[i][j], (i+1)%m)
    
    minimum_cost = 100000000000000
    idx = 0
    for i in range(m):
        if dp[i][0] < minimum_cost:
            minimum_cost = dp[i][0]
            idx = i
    
    rows = [idx+1]
    for i in range(n-1):
        rows.append(path[idx][i]+1)
        idx = path[idx][i]

    return rows, minimum_cost

def P1():
    while True:
        try:
            m, n = map(int, stdin.readline().split())
        except:
            break
        matrix = []
        for i in range(m):
            matrix.append(list(map(int, stdin.readline().split())))
      
        rows, minimum_cost = tsp(matrix)
        print(' '.join(str(x) for x in rows))
        print(minimum_cost)
P1()