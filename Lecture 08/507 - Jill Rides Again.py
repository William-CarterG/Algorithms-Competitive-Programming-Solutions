import sys
import io

# Problem 3
txt = """3
3
-1
6
10
4
-5
4
-3
4
4
-4
4
-5
4
-2
-3
-4"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

import sys

def best_route(s):
    # Where the 'best' is defined by the maximum strech in a route, 
    # according to Jill's assesment.
    start = -1
    nicest_start, nicest_end = -1, -1
    nicer_end, nicest_route = 0, 0

    for i, v in enumerate(s):
        nicer_end += v
        if nicer_end < 0:
            nicer_end = 0
            start = -1
        else:
            if start == -1:
                start = i
            if nicest_route <= nicer_end:
                nicest_route = nicer_end
                if i + 1 - start > nicest_end - nicest_start:
                    nicest_start = start
                    nicest_end = i + 1

    return nicest_start, nicest_end

def P3():
    b = stdin.readline().strip()
    if not b:
        return
    b = int(b)
    for i in range(1, b + 1):
        r = int(stdin.readline().strip())
        s = []
        for _ in range(r-1):
            s.append(int(stdin.readline().strip()))

        nicer_start, nicer_end = best_route(s)
        if nicer_start == -1:
            print(f"Route {i} has no nice parts\n")
        else:
            print(f"The nicest part of route {i} is between stops {nicer_start + 1} and {nicer_end + 1}\n")

P3()
