import sys
import io
import math

#Problem 4

txt = """1 10 5 2.0
1 5 10.0 2
2 10 11 2
3 5 1 6
4 5.0 -1 6
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def P4():
    lines = stdin.readlines()
    for line in lines:
        line = list(map(float, line.split()))
        case = int(line[0])
        #End condition
        if line[0] == '0':
            return
        
        if case == 1:
            u, v, t = line[1:]
            a = (v - u)/t
            s = u*t + 0.5*a*t**2
            print(f"Case {case}: {s:.3f} {a:.3f}")

        elif case == 2:
            u, v, a = line[1:]
            s = (v**2 - u**2)/(2*a)
            t = (v - u)/a
            print(f"Case {case}: {s:.3f} {t:.3f}")

        elif case == 3:
            u, a, s = line[1:]
            v = math.sqrt(u**2 + 2*a*s)
            t = (v - u)/a
            print(f"Case {case}: {v:.3f} {t:.3f}")

        elif case == 4:
            v, a, s = line[1:]
            u = math.sqrt(v**2 - 2*a*s)
            t = (v - u)/a
            print(f"Case {case}: {u:.3f} {t:.3f}")

P4()