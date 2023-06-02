import sys
import io

#Problem 1
txt = """3 4
ONE 1500 2 2 0 3 1 5
TWO 2000 4 3 1 4 0 5 5 10
THREE 3000 1 1 1 9
ONE 24
THREE 7
TWO 206
TWO 339"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin


def physical_address(name, base, element_size, dimensions, lower_bounds, upper_bounds, indices):
    #Calculate constants
    c = [0] * (dimensions + 1)
    c[dimensions] = element_size
    for d in range(dimensions - 1, 0, -1):
        c[d] = c[d + 1] * (upper_bounds[d] - lower_bounds[d] + 1)

    c[0] = base
    for d in range(1, dimensions + 1):
        c[0] -= c[d] * lower_bounds[d - 1]

    #Calculate address
    address = c[0]
    for d in range(dimensions):
        address += c[d + 1] * indices[d]

    return f"{name}[{', '.join(map(str, indices))}] = {address}"

def P1():
    #Read input
    lines = stdin.readlines()
    #Solution only works for one set of array/references. 
    #<==> Only first line contains N, R
    n, r = map(int, lines[0].split())
    
    arrays = []
    for i in range(1, n+1):
        array_data = lines[i].split()

        name = array_data[0]
        if(len(array_data[0]) > 10):
            #Name must have at max 10 characters
            name = array_data[0][:9]
        
        base = int(array_data[1])
        if(base <= 0):
            #INPUT ERROR: Base address must be a positive integer
            return print(0, 0)
    
        element_size = int(array_data[2])   #size in bytes
        if(element_size <= 0):
            #INPUT ERROR: Size must be a positive integer
            return print(0, 0)
        
        d = int(array_data[3])  #dimensions ; 1 <= d <= 10
        if(d < 1 or d > 10):
            #INPUT ERROR: dimensions out of range
            return print(0, 0)
        
        lower_bounds = [int(x) for x in array_data[4::2]]
        upper_bounds = [int(x) for x in array_data[5::2]]

        arrays.append([name, base, element_size, d, lower_bounds, upper_bounds])

    
    references = []
    for i in range(n+1, n+r+1):
        reference_data = lines[i].split()
        name = reference_data[0]
        indices = [int(x) for x in reference_data[1:][0]]
        references.append([name, indices])

    
    #Calculate physical addresses
    for reference_data in references:
        for array_data in arrays:
            if array_data[0] == reference_data[0]:
                print(physical_address(reference_data[0], *array_data[1:], reference_data[1]))
                break
    
P1()