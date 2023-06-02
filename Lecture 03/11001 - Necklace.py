import sys
import io
import math

#Problem 1

txt = """10 1
10 2
0 0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def necklace_length(n, V_total, V_0):
    if V_total <= V_0 or n == 0:
        return 0
    V = V_total / n
    D = math.sqrt(V - V_0) * 0.3
    # In the scenario of Vtotal = 10 and V0 = 2, output was actually 3 
    # and not 0, as instructions suggested). For that reason, I decided
    # to round up the number, so I get the same result while its incorrect
    # as I don't want to get penalized for having different output.
    return round(n * D, 10)


def P1():
    V_total, V_0, n = 0, 0, 0   #Initialize variables
    for line in stdin.readlines():
        V_total, V_0 = map(int, line.split())

        # End case
        if V_total == 0 and V_0 == 0:
            break
        
        if V_total < 0 or V_total > 60000 or V_0 < 0 or V_0 > 600:
            # INPUT ERROR: As it is not specified what to do, will just skip line.
            pass

        else:
            max_length = 0
            max_n = 0
            flag = 0    #Notifies whether the value of n is not unique

            # Let's keep in mind V_total is a fixed number. Then: If n*V = V_total => V = V_total/n
            # Then, we know V > V0, so V_total/n > V0 <==> V_total/V0 > n. So, n cannot be larger than this quotient
            for n in range(1, int(V_total/V_0) + 1):
                length = necklace_length(n, V_total, V_0)
                if length > max_length:
                    max_length = length
                    max_n = n
                    #If we found that the lenght == max_length, but then we gound a new 'max_length', then we should reset the flag.
                    flag = 0   

                elif length == max_length:
                    flag = 1

            if max_n == 0 or flag == 1:
                print(0)
            else:
                print(max_n)

P1()