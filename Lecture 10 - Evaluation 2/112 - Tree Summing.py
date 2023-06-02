import sys
import io

# Problem 2
txt = """22 (5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))
20 (5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))
10 (3(2 (4 () () )(8 () () ) )(1 (6 () () )(4 () () ) ) )
5 ()"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
#stdin = sys.stdin

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def buildTree(line):
    if len(line) == 0:
        return None

    l, r = 0, 0
    count = 0
    value = 0

    if len(line) == 1:
        value = int(line)
        return Node(value)

    for idx, v in enumerate(line):
        if l == 0 and v == '(':
            l = idx
        if v == '(':
            count += 1
        elif v == ')':
            count -= 1
        if r == 0 and l != 0 and count == 0:
            r = idx

    
    left = buildTree(line[l + 1:r])
    right = buildTree(line[r + 2:len(line) - 1])
    value = int(line[:l])
    print(value)
    return Node(value, left, right)



def dfs(sum, node, ssf):
    if node is None:
        return False

    if ssf + node.value > sum:
        return False

    if ssf + node.value == sum and node.left is None and node.right is None:
        return True

    return dfs(sum, node.left, ssf + node.value) or dfs(sum, node.right, ssf + node.value)

def solve(sum, target, char_list):
    global ans
    flag = 0
    leaf = 0
    token = 0
    neg = 1

    while char_list[0] == ' ' or char_list[0] == '\n':
        char_list.pop(0)
    
    if char_list[0] == '(':
        token = 0
        flag = 0
        neg = 1
        
        while True:
            char = char_list.pop(0)
            
            if '0' <= char <= '9':
                token = token * 10 + int(char)
                flag = 1
            else:
                if char == '-':
                    neg = -1
                else:
                    break
          
        token *= neg
        
        while char_list[0] == ' ' or char_list[0] == '\n':
            char_list.pop(0)
        
        if flag == 0:
            return 0
        
        left = solve(sum + token, target, char_list)
        
        while char_list[0] != '(':
            char_list.pop(0)
            
        right = solve(sum + token, target, char_list)
        
        while char_list[0] != ')':
            char_list.pop(0)
        
        if left == 0 and right == 0:
            if sum + token == target:
                ans = 1
        
        return 1


def P2():
    while True:
        line = stdin.readline().strip()
        if not line:
            break
        line = line.split()
        target = int(line[0])
        line = "".join(line[1:])
        char_list = [char for char in line]
        ans = 0
        solve(0, target, char_list)
        if ans == 1:
            print("yes")
        else:
            print("no")

    
ans = 0
def P2():
    while True:
        line = stdin.readline().strip()
        if not line:
            break
        line = line.split()
        target = int(line[0])
        line = "".join(line[1:])
        char_list = [char for char in line]
        ans = solve(0, target, char_list)
        if ans == 1:
            print("yes")
        else:
            print("no")
        
P2()