import sys
import io
import math

# Problem 5
txt = """9
10 10 20 20
10 10 20 20
10 10 20 20
10 10 20 15
10 10 20 25
10 10 20 20
10 10 20 15
10 10 20 20
10 10 20 20
10 10 20 25
10 10 20 20
15 15 25 25
10 10 20 20
20 20 30 30
10 10 20 20
5 5 9 9
10 10 20 20
15 5 16 26"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

class guardRegion:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

N = int(stdin.readline())
cases = 0

for cases in range(N):   
    a = guardRegion()
    b = guardRegion()
    c = guardRegion()
    d = guardRegion()

    a.x, a.y, b.x, b.y = map(int, stdin.readline().split()) # Guard one region.
    c.x, c.y, d.x, d.y = map(int, stdin.readline().split()) # Guard two region.

    i = max(a.x, c.x)
    j = max(a.y, c.y)
    k = min(b.x, d.x)
    l = min(b.y, d.y)

    guard_1 = (b.x - a.x) * (b.y - a.y)
    guard_2 = (d.x - c.x) * (d.y - c.y)
    both_guards = (i - k) * (j - l)
    farmers_land = 100*100

    print("Night {}: ".format(cases+1), end="")
    if i >= k or j >= l:
        # The regions of the guards do not intersect.
        print("0 {} {}\n".format(guard_1 + guard_2, farmers_land - (guard_1 + guard_2)), end="")
    else:
        # The regions of the guards intersect.
        print("{} {} {}\n".format(both_guards, (guard_1 - both_guards) + (guard_2 - both_guards), farmers_land - (guard_1 + guard_2 - both_guards)), end="")

