import sys
import io

# Problem 4
txt = """11
26"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

coins = [1, 5, 10, 25, 50]

while True:
    try:
        cents = int(stdin.readline())
    except:
        break
    
    # We use a dynamic programming solution
    dp = [0] * (cents + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, cents+1):
            dp[j] += dp[j-coin]
    print(dp[cents])
