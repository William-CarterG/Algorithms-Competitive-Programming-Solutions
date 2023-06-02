import sys
import io

#Problem 1

txt = """8
7
3"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def P1():
    lines = stdin.readlines()
    for line in lines:
        N = int(line[0])    #Number of bottles purchased
        if N < 1 or N > 200:
            #INPUT ERROR: It is not specified what to do so I'l just ignore it.
            pass
        else:                
            #Initialize the total N of bottles 
            total = N

            #We'll keep returning bottles until we can't <==> current number of bottles >= 3
            while N >= 3:
                #From the number 'N' of bottles we currently have, we'll be able to get 'N' // 3 New bottles from returniNg
                #the ones we've draNk already.
                total += N // 3

                #The new number of bottles we have is going to be: the empty bottes we couldn't return + the new bottles we got
                #from returning bottles
                N = N % 3  + N // 3

            #We can always borrow bottes from a friend or the storekeeper
            #However, we can only repay them if we have two bottles already (that way, we repay them with the bottle we get 
            #after returning the bottles).
            if N == 2:
                total += 1
                
            print(total)
    
P1()