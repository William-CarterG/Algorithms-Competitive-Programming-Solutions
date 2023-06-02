import sys
import io

#Problem 3

txt = """7
19
10
6
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def P3():
    cards = []  #define type
    for line in stdin.readlines():
        n = int(line.strip())

        #End conditon
        if n == 0:
            return

        elif n > 1000000 or n < 0:
            #INPUT ERROR: It is not specified what to do so I'l just ignore it.
            pass

        else:
            cards = list(range(1, n+1))
            #Loop until there is only one card left
            while len(cards) > 1:
                #Remove the top card
                cards.pop(0)
                #Move the new top card to the bottom
                cards.append(cards.pop(0))
            
            print(cards[0])

P3()