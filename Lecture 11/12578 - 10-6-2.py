import sys
import io
import math

# Problem 6
txt = """1
10"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

# As per the instructions...
PI = math.acos(-1.0)

test_cases = int(stdin.readline())
for _ in range(test_cases):
    # Reading a single float from stdin
    L = float(stdin.readline())

    redArea = PI * (L/5)**2  # PI * r**2, where r = L/5 (according to instructions).

    # Area rectangle = L* (3/5)*L => Remaining Area = Area Rectangle - redArea
    print("{:.2f} {:.2f}".format(redArea, L * (3/5)*L - redArea))   
