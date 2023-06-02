import itertools

def is_valid_path(path):
    """
    Check if a given path is a valid path for Santa's house.
    """
    # Start at the lower left corner (1)
    current_vertex = 1
    # Check that we visit each vertex exactly once
    for vertex in path:
        if vertex == current_vertex:
            return False # Cannot visit the same vertex twice
        if vertex == 2 and current_vertex not in [1, 3]:
            return False # Can only go to vertex 2 from vertices 1 or 3
        if vertex == 4 and current_vertex != 3:
            return False # Can only go to vertex 4 from vertex 3
        if vertex == 5 and current_vertex != 2:
            return False # Can only go to vertex 5 from vertex 2
        current_vertex = vertex
    # Check that we end at the top of the house (vertex 5)
    return current_vertex == 5

# Generate all possible paths of length 8 (there are 5 vertices and we start at the lower left corner)
possible_paths = itertools.product(range(1, 6), repeat=8)

# Check each path to see if it is a valid path for Santa's house
valid_paths = []
for path in possible_paths:
    if is_valid_path(path):
        valid_paths.append(path)

# Print the valid paths in increasing order
for path in sorted(valid_paths):
    print(''.join(str(vertex) for vertex in path))

# Print the number of valid paths found
print(len(valid_paths))
