import sys
import io

# Problem 3
txt = """2
1
2"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

T = int(stdin.readline())

# We set the base cases, so we can precalculate the sequence for 'n'.
dp = [0] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 5

# This is the equation that allows to precalculate the number of ways to pack the cakes. It's deduced from the problem's statement
# but, basically, what is does is that it 'assumes' where the one-unit cakes may be. Another way to look at it, from the dp perspective
# is that the formula accounts for different possibilities when extending the cakes 'box' from smaller-sized boards to larger ones, 
# considering the arrangements of one-unit and L-shaped cakes in various positions on the board.
for i in range(3, 41):
    dp[i] = dp[i - 1] + 4 * dp[i - 2] + 2 * dp[i - 3]


# For each specific 'n', finds the result in the precalculated 'dp'.
for _ in range(T):
    n = int(stdin.readline())
    print(dp[n])
