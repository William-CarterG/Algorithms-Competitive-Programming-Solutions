import sys
import io

# Problem 5
txt = """1
3 6 7
1 7 5 4 8 3 9
1 4 3 5 6 2 8 9"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

# Basically, it uses dp to return the length of the 
# longest increasing subsequence of indices from 
# array b relative to array a.
def solve(n, p, q, a, b):
    a_seq = [-1] * (250*250)
    a_seq[a[0]] = 1
    for i in range(1, p):
        a_seq[a[i]] = a_seq[a[i - 1]] + 1
    
    sub_seq = [a_seq[b[0]]]
    for i in range(1, q):
        if a_seq[b[i]] < 0:
            continue
        b[i] = a_seq[b[i]]
        if sub_seq[-1] < b[i]:
            sub_seq.append(b[i])
            continue
        low_bound = 0
        high_bound = len(sub_seq) - 1
        pos = 0
        while low_bound <= high_bound:
            mid = (low_bound + high_bound) // 2
            if sub_seq[mid] < b[i]:
                pos = mid + 1
                low_bound = mid + 1
            else:
                high_bound = mid - 1
        if b[i] < sub_seq[pos]:
            sub_seq[pos] = b[i]
    
    return len(sub_seq)


def P5():
    cases = int(stdin.readline())
    i = 0
    for _ in range(cases):
        n, p, q = map(int, stdin.readline().split())
        p += 1  # prince will be of length p+1
        q += 1  # princess will be of length q+1
        prince = list(map(int, stdin.readline().split()))
        princess = list(map(int, stdin.readline().split()))
        result = solve(n, p, q, prince, princess)
        i += 1
        print("Case {}: {}".format(i, result))

P5()