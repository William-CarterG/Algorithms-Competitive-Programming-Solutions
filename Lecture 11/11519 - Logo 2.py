import sys
import io
import math

# Problem 4
txt = """7
5
fd 100
lt 120
fd ?
lt 120
fd 100
6
fd 3
rt 90
fd 4
rt 90
rt ?
fd 5
3
fd 100
lt ?
fd 100
4
fd 100
lt 180
rt ?
fd 100
7
fd 100
rt 90
fd 100
rt 90
bk ?
rt 90
fd 100
5
fd 100
lt 120
fd 100
lt ?
fd 100
5
fd 100
lt 120
fd 100
rt ?
fd 100"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

def rad(deg):
    return deg * math.pi / 180.0

def check(id):
    global x, y, angle
    if direction[id] == 'f':
        x += value[id] * math.cos(angle)
        y += value[id] * math.sin(angle)
    elif direction[id] == 'b':
        x -= value[id] * math.cos(angle)
        y -= value[id] * math.sin(angle)
    elif direction[id] == 'l':
        angle += rad(value[id])
    elif direction[id] == 'r':
        angle -= rad(value[id])

def makePoint():
    global x, y, angle
    angle = x = y = 0.0
    for i in range(n):
        check(i)

test_cases = int(stdin.readline())
for _ in range(test_cases):
    n = int(stdin.readline())
    direction = [None] * n
    value = [None] * n
    for i in range(n):
        command = stdin.readline().split()
        direction[i] = command[0][0]
        if command[1] == '?':
            missing_id = i
        else:
            value[i] = int(command[1])

    if direction[missing_id] == 'f' or direction[missing_id] == 'b':
        value[missing_id] = 0
        makePoint()
        result = round(math.hypot(x, y))
        value[missing_id] = result
        makePoint()
        d1 = math.hypot(x, y)
        value[missing_id] = -result
        makePoint()
        d2 = math.hypot(x, y)
        if d1 > d2:
            result *= -1
    else:
        result = 0
        while result < 360:
            value[missing_id] = result
            makePoint()
            if abs(x) < 0.01 and abs(y) < 0.01:
                break
            result += 1

    print(result)
