from queue import Queue
import sys 
import io
from collections import defaultdict

#Problem 2
txt = """3
1 2 0
2 2 0
3 1 2 0
0
3 1 2 3
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
#stdin = sys.stdin

while True:
    n = (stdin.readline().strip())
    if not n or n == '0':
        break

    n = int(n)
    L = [[] for _ in range(n)]
    for i in range(1, n+1):
        nums = list(map(int, stdin.readline().split()))
        nums = nums[:-1]
        if len(nums):
            for j in range(1, n+1):
                if j in nums[1:]:
                    L[i-1].append(j-1)
                else:
                    L[i-1].append(i)
        else:
            for j in range(1, n+1):
                L[i-1].append(-1)
    print(L)
    line = stdin.readline().split()
    line = list(map(int, stdin.readline().split()))
    m = line[0]
    line = line[1:]
    print(m, line)
    for i in range(m):
        v = int(line[i]) - 1
        
        visited = [False] * n
        Q = Queue()
        Q.put(v)
        visited[v] = True
        
        while not Q.empty():
            aux = Q.get()
            for j in L[aux]:
                if aux != i:
                    if not visited[j]:
                        visited[j] = True
                        Q.put(j)
        for j in L[aux]:
            if j == v+1:
                visited[v] = True
        cont = n - sum(visited)
        print(cont, end="")
        for j in range(n):
            if not visited[j]:
                print(" " + str(j+1), end="")
        print()
    