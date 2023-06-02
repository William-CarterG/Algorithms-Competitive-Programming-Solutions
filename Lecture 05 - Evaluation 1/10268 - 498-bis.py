import sys
import io

#Problem 3

txt = """7
1 -1
2
1 1 1"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def P3():
    while(True):
        x = (stdin.readline().strip())
        if not x:
            break
        x = int(x)
        coeffs = list(map(int, stdin.readline().split()))
        n = len(coeffs)
        print(sum(coeffs[i]*(n-i-1)*(x**(n-i-2)) for i in range(n-1)))

P3()