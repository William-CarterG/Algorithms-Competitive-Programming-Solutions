import sys
import io

#Problem 5

txt = """6
3
6
7
8
9
10"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def find_etruscan_rows(number):
    rows = 0 #Etruscan rows we need
    warriors = 0
    while(True):
        rows += 1
        warriors += rows #Says how many warriors we can fit in 'rows' rows.

        # We can fit 'number' warriors in 'rows' rows
        if warriors == number:
            return rows
        
        # If we can fit more warriors than we are given ('warriors' > 'number'), 
        # then we can use one less row.
        elif warriors > number:
            return rows - 1

def P5():
    n = int(stdin.readline().strip())
    for _ in range(n):
        print(find_etruscan_rows(int(stdin.readline().strip())))

P5()