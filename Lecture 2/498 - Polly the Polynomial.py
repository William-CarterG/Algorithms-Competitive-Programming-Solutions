import sys
import io

#Problem 6

txt = """-2
5 0 1 6
1 -1
7 6 -1"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def P6():
    lines = stdin.readlines()
    if(len(lines)//2):
        x_vals, coeffs = [],[]
        for i, line in enumerate(lines):
            if not (i%2):
                #Even index <==> coefficients
                coeffs =  list(map(int, line.split()))
                
            else:
                x_vals =  list(map(int, line.split()))
                for x in x_vals:
                    output = 0
                    for i, coeff in enumerate(coeffs):
                        #Calculate the polynomial equation
                        output += coeff * x ** (len(coeffs) - i - 1)
                    print(output)
    else:
        #INPUT ERROR: It is not specified what to do so I'l just ignore it.
        return
    
P6()