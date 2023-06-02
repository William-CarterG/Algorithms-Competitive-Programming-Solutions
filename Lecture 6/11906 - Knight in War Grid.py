import sys
import io
from collections import defaultdict

# I used this code as reference https://github.com/Diusrex/UVA-Solutions/blob/master/11906%20Knight%20in%20War%20Grid.cpp
# Problem 6
txt = """2
3 3 2 1
0
4 4 1 2
2
3 3
1 1"""

stdin = io.StringIO(txt)

# Actual use (Comment the below line for testing)
stdin = sys.stdin

R = 0
C = 0
M = 0
N = 0
passable = []
visited = []

# Function that returns true if a cell is valid to move into
def Valid(r, c):
    return r >= 0 and r < R and c >= 0 and c < C and passable[r][c]

# Function that explores the board using knight 
# movements in a certain direction and returns the number of valid cells.
def TryShifts(r, c, rMultiple, cMultiple):
    count = 0
    for i in range(4):
        newR = r + rMultiple * [1, 1, -1, -1][i]
        newC = c + cMultiple * [1, -1, 1, -1][i]
        if Valid(newR, newC):
            count += 1
            if not visited[newR][newC]:
                dfs(newR, newC)
    return count

# Function that performs a depth-first search to explore the board and 
# count the number of cells that can be visited with even and odd 
# numbers of moves.
def dfs(r, c):
    global countOdd, countEven
    visited[r][c] = True
    
    # If the knight can move only in one direction, try to move to valid adjacent cells
    if M == N:
        count = TryShifts(r, c, M, M)
    # If the knight can only move in one direction, try to move to valid adjacent cells in that direction
    elif M == 0 or N == 0:
        count = 0
        nonZero = max(M, N)
        for i in range(4):
            newR = r + nonZero * [1, -1, 0, 0][i]
            newC = c + nonZero * [0, 0, 1, -1][i]
            if Valid(newR, newC):
                count += 1
                if not visited[newR][newC]:
                    dfs(newR, newC)
    # Otherwise, try to move to valid adjacent cells in both directions
    else:
        count = TryShifts(r, c, M, N) + TryShifts(r, c, N, M)
    
    if count % 2 == 1:
        countOdd += 1
    else:
        countEven += 1

T = int(stdin.readline().strip())
for t in range(1, T+1):
    R, C, M, N = map(int, stdin.readline().split())
    
    passable = [[True] * C for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    
    W = int(stdin.readline().strip())
    for _ in range(W):
        r, c = map(int, stdin.readline().split())
        passable[r][c] = False
    
    countEven = 0
    countOdd = 0
    
    dfs(0, 0)
    
    print(f"Case {t}: {countEven} {countOdd}")
