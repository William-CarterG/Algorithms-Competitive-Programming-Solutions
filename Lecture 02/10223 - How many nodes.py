import sys
import io
import math 

#Problem 5

txt = """5
14
42"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def catalan(n):
    return math.factorial(2*n) // (math.factorial(n+1) * math.factorial(n))

def P5():
    for line in stdin.readlines():
        n = int(line.strip())   #maximum number of trees
        if n > 4294967295:
            #INPUT ERROR: It is not specified what to do so I'l just ignore it.
            pass
        else:
            #'Assuming that there are two types of steps,
            #Catalan numbers count the number of way to perform 2n steps'
            i = 0
            while catalan(i) < n:
                i += 1

            print(i)

P5()