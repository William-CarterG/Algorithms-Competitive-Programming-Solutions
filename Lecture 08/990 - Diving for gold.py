import sys
import io

# Problem 6
txt = """210 4
3
10 5
10 1
7 2"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

while True:
    try:
        t, constant_w = map(int, stdin.readline().split())
        n = int(stdin.readline().strip())   # number of treasures
    except:
        break

    W, V, D = [0], [0], [0] # W is result after multiplying the i-th item depth for the constant
    for i in range(1, n+1):
        d, v = map(int, stdin.readline().split())
        D.append(d)
        V.append(v)
        W.append(3 * d * constant_w)

    dp = [[0]*(t+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(t+1):
            if W[i] <= j:
                dp[i][j] = max(dp[i-1][j], V[i] + dp[i-1][j-W[i]])
            else:
                dp[i][j] = dp[i-1][j]

    recovered_treasures, k, max_gold = [], 0, 0
    i = n
    while i > 0:
        if dp[i][t] != dp[i-1][t]:
            recovered_treasures.append(i)
            t -= W[i]
            max_gold += V[i]
        i -= 1

    print(max_gold)
    print(len(recovered_treasures))
    for i in reversed(recovered_treasures):
        print(D[i], V[i])
