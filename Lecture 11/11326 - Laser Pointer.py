import sys
import io
import math

# Problem 3
txt = """2
10 5 45
12 12 75"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

test_cases = int(stdin.readline())

for _ in range(test_cases):
    L, W, angleGrad = map(int, stdin.readline().split())

    angle = 2 * math.acos(0) * angleGrad / 180.0

    if angle == 0:
        # A == B
        print("1.000")
    else:
        x = W / math.tan(angle) # Length of segment (in the horizontal direction) based on the angle.
        k = 1

        # In a way, how long does it take x to reach L.
        while x * k <= L:
            k += 1

        y = L - (k - 1) * x # Remaining length (beyond the covered segments).

        if k % 2 == 0:
            h = W - y * math.tan(angle)
        else:
            h = y * math.tan(angle)

        s = y / math.cos(angle) # Length of the segment in the vertical direction

        # Length of the laser beam's path on the diagonal * additional lengths of the laser beam's path beyond the first segment.
        output = W / math.sin(angle) * (k - 1)  
        output += s # With this, total length of the laser beam's path is calculated.

        # Hypotenuse of triangle with sides h and L.
        output /= math.sqrt(h * h + L * L)

        # Dividing the total length of the laser beam's path by this hypotenuse (laser beam on the way back) provides a 
        # normalized value that represents the ratio A/B.
        print("{:.3f}".format(output))

