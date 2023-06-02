import sys
import io

#Problem 1
txt = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
"""

stdin = io.StringIO(txt)
#Actual use (Comment the below line for testing)
#stdin = sys.stdin


def check_for_scent(position, orientation, scents):
    tmp = []
    if len(scents) != 0:
        tmp = position
        if orientation == 'N':
            tmp[1] -= 1
        elif orientation == 'S':
            tmp[1] += 1
        elif orientation == 'W':
            tmp[0] += 1
        elif orientation == 'E':
            tmp[0] -= 1
    for scent in scents:
        if tmp == scent:
            return True
    return False
def P1():
    cardinal_directions = {'N': ['W', 'E'], 'E': ['N', 'S'], 'S': ['E', 'W'], 'W':
    ['S', 'N']}
    map_size = stdin.readline().split()
    scents = []
    width = int(map_size[0])
    height = int(map_size[1])
    while(True):
        robot_data = stdin.readline().split()
        if not robot_data:
            return
        robot_data = {"coordinates": [int(robot_data[0]), int(robot_data[1])],
        "orientation": robot_data[2]}
        robot_instructions = stdin.readline().split()[0]
        for instruction in robot_instructions:
            flag = False
            # Instruction is executed
            if instruction == 'R':
                robot_data["orientation"] = cardinal_directions[robot_data["orientation"]][1]
            elif instruction == 'L':
                robot_data["orientation"] = cardinal_directions[robot_data["orientation"]][0]
            elif instruction == 'F':
                if robot_data["orientation"] == 'N':
                    robot_data["coordinates"][1] = robot_data["coordinates"][1] + 1
                    if robot_data["coordinates"][1] > height and check_for_scent(robot_data["coordinates"], robot_data["orientation"], scents):
                        robot_data["coordinates"][1] = robot_data["coordinates"][1]
                    elif robot_data["coordinates"][1] > height and not check_for_scent(robot_data["coordinates"],robot_data["orientation"], scents):
                        robot_data["coordinates"][1] = robot_data["coordinates"][1]- 1
                        print(f'{robot_data["coordinates"][0]} {robot_data["coordinates"][1]} {robot_data["orientation"]} LOST')
                        scents.append(robot_data["coordinates"])
                        flag = True
                        break
                elif robot_data["orientation"] == 'S':
                    robot_data["coordinates"][1] = robot_data["coordinates"][1] - 1
                    if robot_data["coordinates"][1] < 0 and check_for_scent(robot_data["coordinates"],robot_data["orientation"], scents):
                        robot_data["coordinates"][1] = robot_data["coordinates"][1]
                    elif robot_data["coordinates"][1] < 0 and not check_for_scent(robot_data["coordinates"],robot_data["orientation"], scents):
                        robot_data["coordinates"][1] = robot_data["coordinates"][1] + 1
                        print(f'{robot_data["coordinates"][0]} {robot_data["coordinates"][1]} {robot_data["orientation"]} LOST')
                        scents.append(robot_data["coordinates"])
                        flag = True
                        break
                elif robot_data["orientation"] == 'W' :
                    robot_data["coordinates"][0] = robot_data["coordinates"][0] - 1
                    if robot_data["coordinates"][0] < 0 and check_for_scent(robot_data["coordinates"],robot_data["orientation"], scents):
                        robot_data["coordinates"][0] = robot_data["coordinates"][0]
                    elif robot_data["coordinates"][0] < 0 and not check_for_scent(robot_data["coordinates"],robot_data["orientation"], scents):
                        robot_data["coordinates"][0] = robot_data["coordinates"][0] + 1
                        print(f'{robot_data["coordinates"][0]} {robot_data["coordinates"][1]} {robot_data["orientation"]} LOST')
                        scents.append(robot_data["coordinates"])
                        flag = True
                        break
                elif robot_data["orientation"] == 'E':
                    robot_data["coordinates"][0] = robot_data["coordinates"][0] + 1
                    if robot_data["coordinates"][0] > width and check_for_scent(robot_data["coordinates"],robot_data["orientation"], scents):
                        robot_data["coordinates"][0] = robot_data["coordinates"][0]
                    elif robot_data["coordinates"][0] > width and not check_for_scent(robot_data["coordinates"],robot_data["orientation"], scents):
                        robot_data["coordinates"][0] = robot_data["coordinates"][0] - 1
                        print(f'{robot_data["coordinates"][0]} {robot_data["coordinates"][1]} {robot_data["orientation"]} LOST')
                        scents.append(robot_data["coordinates"])
                        flag = True
                        break
        if not flag:
            print(f'{robot_data["coordinates"][0]} {robot_data["coordinates"][1]} {robot_data["orientation"]}')

P1()