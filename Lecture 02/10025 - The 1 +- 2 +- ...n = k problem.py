import sys
import io
import math

#Problem 1

txt = """2
12
-3646397"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
#stdin = sys.stdin

def solve(k):
    k = abs(k)
    n = int((-1 + math.sqrt(1 + 8 * k)) / 2)
    while True:
        s = n * (n + 1) // 2
        if s >= k and (s - k) % 2 == 0:
            return n
        n += 1

def P2():
    lines = stdin.readlines()
    test_cases = int((lines[0].split())[0])
    for i in range(1, test_cases + 1):
        k = int((lines[i].split())[0])
        if abs(k) > 1000000000:
            #INPUT ERROR: It is not specified what to do so I'l just ignore it.
            pass
        else:
            n = solve(k)
            print(n)
            if i != test_cases:
                print()  #print a blank line between test cases

P2()