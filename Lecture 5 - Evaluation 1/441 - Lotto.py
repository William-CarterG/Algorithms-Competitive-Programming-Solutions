import sys
import io

#Problem 4

txt = """7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def P4():
    while(True):
        S = list(map(int, stdin.readline().split()))
        if S == [0]:
            break
        k = S[0]
        S = S[1:]
       

        # As recommended by user stevenhalim in udebug, I'll just solve it
        # using 6 nested loops.
        S.sort()
        for i in range(k-5):
            for j in range(i+1, k-4):
                for m in range(j+1, k-3):
                    for n in range(m+1, k-2):
                        for p in range(n+1, k-1):
                            for q in range(p+1, k):
                                print(S[i], S[j], S[m], S[n], S[p], S[q])
        print()

P4()