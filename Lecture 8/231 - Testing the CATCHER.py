import sys
import io

# Problem 2
txt = """389
207
155
300
299
170
158
65
-1
23
34
21
-1
-1"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

def lds(h):
    m = [1] * len(h)
    maximum = 1
    for i in range(1, len(h)):
        for j in range(i):
            if h[i] < h[j] and m[i] <= m[j]:
                m[i] = m[j] + 1
                if maximum < m[i]:
                    maximum = m[i]
    return maximum


heights = []    # the heigts of incomming missiles
count = 0
for line in stdin.readlines():
    tmp = int(line)
    if tmp == -1 and not heights:
        break
    if tmp == -1:
        if count > 0:
            print()
        count += 1
        print(f"Test #{count}:")
        print(f"  maximum possible interceptions: {lds(heights)}")
        heights.clear()
    else:
        heights.append(tmp)
