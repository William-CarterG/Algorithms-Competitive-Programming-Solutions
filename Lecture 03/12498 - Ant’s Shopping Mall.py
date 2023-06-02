import sys
import io

#Problem 2

txt = """3
2 4
1010
0101
3 3
111
111
111
3 5
01111
11110
11011"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

#Used the folowwing hint in 'udebug.com' (by user 'Morass' to solve the problem: 
# "For each [X,Y] node, precalculate closest left/right 0 {including itself}.
# For each column, iterate through it, and sum min(L/R) for each node.
# Find minimum of such sums.
# Complexity O(N*M)
# Good Luck!"

def find_closest_zeros(mall, R, C):
    left_zeros = [[0] * C for _ in range(R)]
    right_zeros = [[0] * C for _ in range(R)]

    for r in range(R):
        # calculate closest left zero for each cell
        closest_left_zero = -1
        for c in range(C):
            if mall[r][c] == '0':
                closest_left_zero = c
            left_zeros[r][c] = closest_left_zero

        # calculate closest right zero for each cell
        closest_right_zero = C
        for c in range(C - 1, -1, -1):
            if mall[r][c] == '0':
                closest_right_zero = c
            right_zeros[r][c] = closest_right_zero

    return left_zeros, right_zeros


def min_shop_movement(mall, R, C):
    left_zeros, right_zeros = find_closest_zeros(mall, R, C)
    min_movement = 2**63 - 1
    # Iterate over each column and calculate the min movement
    for c in range(C):
        movement = 0
        for r in range(R):
            if mall[r][c] == '1':
                # If there is a shop, calculate the min movement required to move it
                left_distance = c - left_zeros[r][c] if left_zeros[r][c] != -1 else 2**63 - 1
                right_distance = right_zeros[r][c] - c if right_zeros[r][c] != C else 2**63 - 1
                movement += min(left_distance, right_distance)
        min_movement = min(min_movement, movement)

    if min_movement == 2**63 - 1:
        return -1  
    else:
        return min_movement


def P2():
    T = int(stdin.readline().strip())
    for _ in range(T):
        R, C = map(int, stdin.readline().split())
        mall = []
        for _ in range(R):
            row = stdin.readline().split()[0]
            mall.append(row)

        print(min_shop_movement(mall, R, C))

P2()
