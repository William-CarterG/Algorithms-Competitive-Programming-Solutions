import sys
import io

# Problem 4
txt = """bkbjxcoor ihgmvgrnj
fnrrqgntemmiwnrtrijk tsogp
#"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
#stdin = sys.stdin

def print_modification(i, j, a, b, arg):
    if i == 0 and j == 0:
        return
    if arg[i][j] == 1:
        print_modification(i - 1, j - 1, a, b, arg)
    elif arg[i][j] == 2:
        print_modification(i - 1, j, a, b, arg)
        print(f"D{a[i - 1]}{j + 1:02d}", end="")
    elif arg[i][j] == 3:
        print_modification(i, j - 1, a, b, arg)
        print(f"I{b[j - 1]}{j:02d}", end="")
    else:
        print_modification(i - 1, j - 1, a, b, arg)
        print(f"C{b[j - 1]}{j:02d}", end="")


while True:
    s = stdin.readline().strip()
    if s == "#":
        break
    s = s.split()
    a = s[0]
    b = s[1]

    dp = [[sys.maxsize] * (len(b) + 1) for _ in range(len(a) + 1)]
    arg = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    dp[0][0] = 0

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i > 0 and j > 0:
                if a[i - 1] == b[j - 1] and dp[i][j] > dp[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    arg[i][j] = 1
                if dp[i][j] > dp[i - 1][j] + 1:
                    dp[i][j] = dp[i - 1][j] + 1
                    arg[i][j] = 2
                if dp[i][j] > dp[i][j - 1] + 1:
                    dp[i][j] = dp[i][j - 1] + 1
                    arg[i][j] = 3
                if dp[i][j] > dp[i - 1][j - 1] + 1:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    arg[i][j] = 4

    print_modification(len(a), len(b), a, b, arg)
    print("E")

