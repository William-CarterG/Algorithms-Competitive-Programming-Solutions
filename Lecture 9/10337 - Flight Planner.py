import sys
import io

# Problem 1
txt = """2


400
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 9 9 1
1 -9 -9 1




1000
9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9
7 7 7 7 7 7 7 7 7 7
-5 -5 -5 -5 -5 -5 -5 -5 -5 -5
-7 -3 -7 -7 -7 -7 -7 -7 -7 -7
-9 -9 -9 -9 -9 -9 -9 -9 -9 -9"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

level = 10
def solve(steps, airspace):
    dp = [[sys.maxsize] * level for _ in range(steps + 1)]
    dp[0][0] = 0
    for i in range(steps):
        for j, cell in enumerate(dp[i]):
            wind = airspace[i + 1][j]
            if j + 1 < level:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], cell + 60 - wind)
            if j > 0:
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1], cell + 20 - wind)
            dp[i + 1][j] = min(dp[i + 1][j], cell + 30 - wind)
    return dp[steps][0]


def P1():
    n = int(stdin.readline().strip())
    test_case = 0
    while True:
        if test_case > 0:
            print() 

        x = (stdin.readline().strip())
        # This accounts for "Test cases are separated by one or more blank lines."
        while True: 
            if not x and test_case == n:
                return
            elif not x:
                x = (stdin.readline().strip())
            else:
                break
 
        x = int(x)
        steps = x // 100
        airspace = [[0] * level for _ in range(steps + 1)]
        for i in range(level):
            row = list(map(int, stdin.readline().split()))
            for j, value in enumerate(row):
                airspace[j + 1][level - i - 1] = value
        result = solve(steps, airspace)
        test_case += 1
        print(result)

P1()
