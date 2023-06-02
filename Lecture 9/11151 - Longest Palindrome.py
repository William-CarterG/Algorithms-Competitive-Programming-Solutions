import sys
import io

# Problem 3
txt = """2
ADAM
MADAM"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

def P3():
    t = int(stdin.readline())
    for _ in range(t):
        string = stdin.readline().strip()
        n = len(string)
        dp = [0] * (n+1)
        max = 0
        # We can use dynamic programming to solve the problem efficiently by breaking 
        # it down into smaller subproblems and re-using the results of these subproblems 
        # to solve the larger problem.
        for k in range(n):
            tmp_max = 0 # maximum value of dp encountered so far(for each iteration)
            for i in range(n-1, -1, -1):
                # Loop through 'string' from the start and from the end and if characters are equal, update variables accordingly.
                if string[i] == string[k]:
                    if dp[i] <= tmp_max:
                        dp[i] = tmp_max + 1
                    else:
                        tmp_max = dp[i]
                    if dp[i] > max:
                        max = dp[i]
                elif dp[i] > tmp_max:
                    tmp_max = dp[i]
        print(max)

P3()
