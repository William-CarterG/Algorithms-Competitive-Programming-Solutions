import sys
import io

#Problem 5

txt = """8 6
4 4
0 0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
#stdin = sys.stdin

# This solution was greatly inspired by a 'Geeks for Geeks' article called
# "Ways to place K bishops on an N×N chessboard so that no two attack"
# https://www.geeksforgeeks.org/ways-to-place-k-bishops-on-an-nxn-chessboard-so-that-no-two-attack/


def squares_in_diagonal(i):
    if ((i & 1) == 1):
        return int(i / 4) * 2 + 1
    else:
        return int((i - 1) / 4) * 2 + 2
 

def count_bishop_placements(n, k):
    # This solution uses dynamic programming
    # We haven't seen it in the course so far, so I'll try to explain the solution as I understood it.

    # The dp[i][j] variable represents the number of ways to place j bishops on the ith diagonal of an n x n chessboard.
    # We create dp and need to acount for j = {0, k+1 (between 0 and k bishops in a diagonal)}
    # and for i = {0, 2*n -1 (there are 2*n-1 diagonals in total)}.
    dp = [[0 for i in range(k + 1)]
             for i in range(n * 2)]
   
    # Base scenarios
    # Since j=0, there are 0 bishops to place on any diagonal
    for i in range(n * 2):
        dp[i][0] = 1
    # Number of ways to place 1 bishop on a 1x1 chessboard. 
    dp[1][1] = 1


    # Calculates the number of ways
    for i in range(2, n * 2, 1):
        for j in range(1, k + 1, 1):
            # This is where it gets tricky...

            # This is used to calculate the number of squares in diagonal i. 
            total_squares = squares_in_diagonal(i)

            # Here we calculate the number of ways to place j bishops on the ith diagonal
            # We either don't place a bishop on the diagonal (dp[i-2][j]) 
            # or we place a bishop on the diagonal (j - 1) and then choosing a free square on the diagonal for it to occupy. 
            dp[i][j] = (dp[i - 2][j]) + (dp[i - 2][j - 1] * (total_squares - j + 1))
 

    # Lastly, for the answer we need to take into account all possible numbers of bishops placed on 
    # either black diagonals (j bishops) or white diagonals (k-j bishops). Thus, we multiply the results 
    # for each scenario (as they are independent), taking into account that the black diagonals (for the n*n chessboard)
    # are 2n-1 and the white ones are 2n-2.
    ans = 0
    for j in range(0, k + 1, 1):
        ans += (dp[n * 2 - 1][j] * dp[n * 2 - 2][k - j])
 
    return ans

    
def P5():
    while True:
        line = stdin.readline().strip()
        n, k = map(int, line.split())
        if n == 0 and k == 0:
            break

        elif n < 1 or n > 8 or k < 0 or k > n**2:
            # INPUT ERROR: I'll just skip this line
            continue
        print(count_bishop_placements(n, k))

P5()
