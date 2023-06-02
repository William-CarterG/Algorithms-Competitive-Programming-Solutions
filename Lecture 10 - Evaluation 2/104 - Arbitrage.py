import sys
import io

# Problem 1
txt = """3
1.2 .89
.88 5.1
1.1 0.15"""

stdin = io.StringIO(txt)

# Actual use (Comment the below line for testing)
# stdin = sys.stdin


N = 21
d = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
path = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]


def FloydWarshall(n):
    for k in range(2, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                path[i][j][k] = path[i][j][1]  # Initialize path with the same value as for the first step

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j][1] = lines[i - 1][j - 1]  # Initialize d with the provided exchange rates

    for step in range(2, n + 1):
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if d[i][k][step - 1] * d[k][j][1] > d[i][j][step]:
                        d[i][j][step] = d[i][k][step - 1] * d[k][j][1]
                        path[i][j][step] = k

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if d[i][j][n] > 1.01 and i == j:
                s = []
                curr_step = n
                while curr_step > 1:
                    s.append(path[i][j][curr_step])
                    j = path[i][j][curr_step]
                    curr_step -= 1
                s.append(i)
                s.append(i)
                print(' '.join(str(x) for x in s))
                return

    print("no arbitrage sequence exists")


def P1():
    while True:
        n = stdin.readline()
        if not n:
            return
        n = int(n)

        global lines
        lines = [[None] * n for _ in range(n)]
        for i in range(n):
            line = list(map(float, stdin.readline().strip().split()))
            for j in range(n):
                if i == j:
                    lines[i][j] = 1
                else:
                    lines[i][j] = line.pop(0)

                path[i][j][1] = i

        FloydWarshall(n)


P1()
