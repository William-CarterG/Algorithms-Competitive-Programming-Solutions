import sys
import io

# Problem 2
txt = """PRATTATTATTIC
GGGGGGGGG
PRIME
BABBABABBABBA
ARPARPARPARPAR
*"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

def P2():
    for line in stdin.readlines():
        string = line.strip()
        if string == "*":
            break
        n = len(string)

        # represents the length of the longest common factoring of the two substrings of 'string'
        same = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for l in range(1, min(n - i, n - j) + 1):
                    if string[i + l - 1] == string[j + l - 1]:
                        same[i][j] = l
                    else:
                        break


        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        # the optimal solution for a substring can be found using the optimal solutions of its subproblems, 
        # which in turn can be computed recursively. The base cases are substrings of length 1 (just the character).
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = j - i + 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
                for k in range(1, l):
                    if l % k == 0:
                        all_same = True
                        for st in range(i, j+1, k):
                            if not same[i][st] >= k:
                                all_same = False
                                break
                        if all_same:
                            dp[i][j] = min(dp[i][j], dp[i][i+k-1])

        print(dp[0][n-1])

P2()