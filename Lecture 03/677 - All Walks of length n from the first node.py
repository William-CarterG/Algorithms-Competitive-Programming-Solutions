import sys
import io

#Problem 3

txt = """5 2
0 1 0 1 0
1 0 1 0 0
0 1 0 1 1
1 0 1 0 1
0 0 1 1 0
-9999
5 3
0 1 0 1 0
1 0 1 0 0
0 1 0 1 1
1 0 1 0 1
0 0 1 1 0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

#To find A_n, we would always multiply An for A, on the right side
def multiply_A(An, A):
    C = [[0] * len(An[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(An[0])):
            for k in range(len(An)):
                C[i][j] += A[i][k] * An[k][j]

            #Has path or doesn't has path <==> 1 or 0
            if(C[i][j] > 1):
                C[i][j] = 1

    return C


def calculate_walks(adj_matrix, walks, nodes):
    #Matrix An which contains walks of length 'walks'
    A_n = adj_matrix
    for _ in range(walks - 1):
        A_n = multiply_A(A_n, adj_matrix)

    all_walks = set()
    for j in range(nodes):
        if A_n[1][j]:
            first_node_walks = set(check_neighbors(1, j, [], walks, adj_matrix))
            all_walks.update(first_node_walks)

    if not all_walks:
        print(f"no walk of length {walks}")
    else:
        sorted_walks = sorted(list(all_walks))

    for walk in sorted_walks:
        if not walk[0]:
            #Nodes actually start from 1 in the graph
            print(tuple(map(lambda x: x+1, walk)))


def check_neighbors(curr, destination, path, walks, adj_matrix):
    if len(path) == walks:
        return [tuple(path)]
    
    walks_to_destintion = []
    for i, val in enumerate(adj_matrix[curr]):
        if val and i not in path:
            i_node_walk = check_neighbors(i, destination, path + [i], walks, adj_matrix)   
            walks_to_destintion.extend(i_node_walk)
    return walks_to_destintion


def P3():
    while True:
        nodes, walks = map(int, stdin.readline().split())
        adj_matrix = []
        for _ in range(nodes):
            line = list(map(int, stdin.readline().split()))
            adj_matrix.append(line)

        calculate_walks(adj_matrix, walks+1, nodes)
        # Should find -9999 to keep going, but I though it was better this way.
        if stdin.readline().split():
            print()
        else:
            return
        
P3()