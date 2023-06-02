import sys
import io

#Problem 6

txt = """2
4 3 0 0 0 23
25
100
1 0 1
1
6"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def find_b_sequence_n(d, k):
    b = 0
    n = 1
    while(b < k):
        #We'll add the 'n'th element of a n*d times to b. 
        b += n*d
        #If 'b' >= k, means that the 'k'th element of b will be found for n = "n".
        if b >= k:
            return n
        n += 1

def P6():
    cases = int(stdin.readline().strip())
    for _ in range(cases):
        coeff_list = [int(x) for x in stdin.readline().split()]   
        d = int(stdin.readline().strip())
        k = int(stdin.readline().strip())

        b_n = (find_b_sequence_n(d, k))  
        print(sum(coeff * (b_n ** exp) for exp, coeff in enumerate(coeff_list[1:])) )

P6()