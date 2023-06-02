import sys
import io

# Problem 4
txt = """die einkommen der landwirte
sind fuer die abgeordneten ein buch mit sieben siegeln
um dem abzuhelfen
muessen dringend alle subventionsgesetze verbessert werden
#
die steuern auf vermoegen und einkommen
sollten nach meinung der abgeordneten
nachdruecklich erhoben werden
dazu muessen die kontrollbefugnisse der finanzbehoerden
dringend verbessert werden
#"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

# Longest common sub-sequenec algorithm
def lcs(a, b):
    l1, l2 = len(a), len(b)
    dp = [[[] for _ in range(l2+1)] for _ in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + [a[i-1]]
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    return ' '.join(dp[l1][l2])

def P4():
    statement_1, statement_2 = [], []   
    first = True    # This boolean act as a flag, to see whether this is the first or second statement
    for line in stdin.readlines():
        l = line.strip()
        if not l:
            break
        if l == '#':
            if first:
                first = False
            else:
                # We finished both statements, so we compare them and move on to the next one.
                print(lcs(statement_1, statement_2))
                statement_1, statement_2 = [], []
                first = True
        else:
            tokens = l.split()
            if first:
                statement_1 += tokens
            else:
                statement_2 += tokens
P4()

