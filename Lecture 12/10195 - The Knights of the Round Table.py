import sys
import io
import math

# Problem 5
txt = """0.0 0.0 0.0
1.0 1.0 1.0
1.0 1.0 0.0
1.0 0.0 1.0
0.0 1.0 1.0
3.1416 3.1416 3.1416
1000000.0 1000000.0 1000000.0
1000000.0 500000.0 500000.0
0.1 0.1 0.1
3 4 5
30 40 50
300 400 500
3000 4000 5000
30000 40000 50000
300000 400000 500000"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

def P5():
    for line in stdin.readlines():
        a, b, c = map(float, line.split())
        if a + b + c == 0:
            r = 0
        else:
            s = (a + b + c) / 2
            r = math.sqrt(s * (s - a) * (s - b) * (s - c)) / s
        print(f"The radius of the round table is: {r:.3f}")

P5()
