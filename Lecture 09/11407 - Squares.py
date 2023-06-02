import sys
import io

# Problem 4
txt = """5
1
2
3
4
50"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

# The optimal substructure of this solution lies in the fact that the minimum number 
# of squared numbers required to sum up to a certain number can be obtained by adding 
# a squared number to the minimum number of perfect squares required to sum up to the 
# difference between that number and the perfect square (it's like a tongue twister). 
# But basically, we can apply this process recursively to obtain the solution for every possible N. 
def pre_calculate():
    pow2 = [i*i for i in range(1, 101)] # Contains all i**2 <= 100**2 (=10000)
    dp = [sys.maxsize] * (10**4 + 1)    # Max size for N = 10000
    dp[0] = 0
    for i in range(0, 10**4 + 1):
        for j in range(1, 101):
            u = pow2[j-1] + i
            if u > 10**4:
                break
            if dp[i]+1 < dp[u]:
                dp[u] = dp[i]+1
    return dp

def P5():
    dp = pre_calculate()    # As the process is the same for every number, and we have a relatively small max number, we can just precalculate the results.
    test_cases = int(stdin.readline())
    for _ in range(test_cases):
        n = int(stdin.readline().strip())
        print(dp[n])
        
P5()