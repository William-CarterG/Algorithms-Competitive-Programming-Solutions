import sys
import io

# Problem 4
txt = """2
3 2
1 2
2 3
10 12
1 2
3 1
3 4
5 4
3 5
4 6
5 2
2 1
7 1
1 2
9 10
8 9"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

def unionFind(x, f):
    # Helps find the root parent (friend) of each friends pair.
    # That way, we find who has friends related to others.
    if f[x] != x:
        f[x] = unionFind(f[x], f)
    return f[x]

# Calculates the maximum number of friends in a group
# In other words, the largest network of friends in the 'f' list.
def max_friends(f):
    m = 0
    friends_map = {}
    for i in range(len(f)):
        root = unionFind(i, f)
        if root not in friends_map:
            friends_map[root] = 0
        friends_map[root] += 1
        m = max(m, friends_map[root])
    return m

def P4():
    test_cases = int(stdin.readline())
    for _ in range(test_cases):
        n, m = map(int, stdin.readline().split())
        f = list(range(n + 1))
        for _ in range(m):
            a, b = map(int, stdin.readline().split())
            f1, f2 = unionFind(a, f), unionFind(b, f)
            if f1 != f2:
                f[f1] = f2
        print(max_friends(f))

P4()
