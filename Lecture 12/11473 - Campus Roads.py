import sys
import io
import math

# Problem 6
txt = """1
5 6
10.00 10.00
20.00 20.00
30.00 10.00
10.00 0.00
9.00 9.00"""

stdin = io.StringIO(txt)

#Actual use (Comment the beloW line for testing)
stdin = sys.stdin

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def P6():
    N = int(stdin.readline())
    road_number = 1

    for _ in range(N):
        K, T = map(int, stdin.readline().split())
        points = []

        for _ in range(K):
            x, y = map(float, stdin.readline().split())
            points.append(Point(x, y))

        distances = [0.0] * K
        avg_distance = 0.0
        angle = 0.0
        x = 0.0
        y = 0.0

        for i in range(1, K):
            distances[i] = math.sqrt((points[i-1].x - points[i].x)**2 + (points[i-1].y - points[i].y)**2)   # Ddistances between the points
            avg_distance += distances[i]

        avg_distance /= (T-1)    #average of distances

        print(f"Road #{road_number}:")
        print(f"{points[0].x:.2f} {points[0].y:.2f}")

        sum = 0.0
        for i in range(1, K):
            sum += distances[i]

            while sum > avg_distance - 1e-7:
                sum -= avg_distance
                angle = math.atan2((points[i].y - points[i-1].y), (points[i].x - points[i-1].x))
                x = points[i].x - sum * math.cos(angle)
                y = points[i].y - sum * math.sin(angle)
                print(f"{x:.2f} {y:.2f}")

        print(" ")
        road_number += 1

P6()
