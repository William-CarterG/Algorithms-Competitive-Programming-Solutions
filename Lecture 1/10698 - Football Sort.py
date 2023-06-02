from collections import defaultdict
import sys
import io

#Problem 5
txt = """11 54
a
b
c
d
e
f
g
h
i
j
k
a 1 - 0 b
a 1 - 0 c
a 1 - 0 d
a 1 - 0 e
a 1 - 0 f
a 1 - 0 g
a 1 - 0 h
a 1 - 0 i
a 1 - 0 j
a 1 - 0 k
b 1 - 0 c
b 1 - 0 d
b 1 - 0 e
b 1 - 0 f
b 1 - 0 g
b 1 - 0 h
b 1 - 0 i
b 1 - 0 j
b 1 - 0 k
c 1 - 0 d
c 1 - 0 e
c 1 - 0 f
c 1 - 0 g
c 1 - 0 h
c 1 - 0 i
c 1 - 0 j
c 1 - 0 k
d 1 - 0 e
d 1 - 0 f
d 1 - 0 g
d 1 - 0 h
d 1 - 0 i
d 1 - 0 j
d 1 - 0 k
e 1 - 0 f
e 1 - 0 g
e 1 - 0 h
e 1 - 0 i
e 1 - 0 j
e 1 - 0 k
f 1 - 0 g
f 1 - 0 h
f 1 - 0 i
f 1 - 0 j
f 1 - 0 k
g 1 - 0 h
g 1 - 0 i
g 1 - 0 j
g 1 - 0 k
h 1 - 0 i
h 1 - 0 j
h 1 - 0 k
i 1 - 0 j
i 1 - 0 k
0 0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def P5():
    lines = stdin.readlines()
    i = 0
    while True:
        T, G = map(int, lines[i].split())
        if T == 0 and G == 0:
            break
        i += 1

        #Create a dictionary with each team's statistics
        #Team position ; Games played ; Scored goals ; Received goals ; Points
        stats = defaultdict(lambda: [0, 0, 0, 0, 0])

        #Read the team names
        teams = []
        for j in range(i, i + T):
            team = lines[j].strip()

            tmp = ""
            for character in team:     
                if character == "-":
                    #Change is to avoid problems later.'*' will be replaced wHen printing
                    tmp += "*"
                elif character.isalpha():
                    tmp += character
                else:
                    #INPUT ERROR: Name may only contain letters or '-'
                    return print(0, 0)
            team = tmp
            teams.append(team)

            #Give initial position
            stats[team][0] = j - i

        i += T

        #Read in the game scores and update the statistics
        for j in range(i, i + G):
            #Process data
            home, away = lines[j].strip().split(' - ')
            home_team, home_goals = home.split()
            away_goals, away_team = away.split()

            home_goals = int(home_goals)
            away_goals = int(away_goals)

            #Update games played
            stats[home_team][1] += 1
            stats[away_team][1] += 1

            #Update goals scored
            stats[home_team][2] += home_goals
            stats[away_team][2] += away_goals

            #Update goals received
            stats[home_team][3] += away_goals
            stats[away_team][3] += home_goals

            #Update points
            if home_goals > away_goals:
                stats[home_team][4] += 3
            elif home_goals < away_goals:
                stats[away_team][4] += 3
            else:
                stats[home_team][4] += 1
                stats[away_team][4] += 1

        i += G

        #Fixing teams names by replacing temporary '*' for '-'
        actual_teams = []
        for team in teams:
            tmp = ""
            for character in team:
                if character == "*":
                    tmp += "-"
                else:
                    tmp += character
            stats[team].append(tmp) 

        #Sort the teams accordingly to the standings defined order
        sorted_teams = sorted(teams, key=lambda x: (-stats[x][4], -stats[x][2], -stats[x][3], x))

        #Print out the statistics table
        #Used this websites to learn how to copy the printing format from the sample output
        #https://note.nkmk.me/en/python-rjust-center-ljust/
        #https://realpython.com/python-formatted-output/
        printed_points = set()  #keeps tracked of draws in points
        for j in range(T):
            if stats[sorted_teams[j]][4] not in printed_points:  # check if value has not been printed yet
                print('{:>2}. '.format(j + 1), end='')  # print position for first time
                printed_points.add(stats[sorted_teams[j]][4])  # adds points to set
            else:
                print('{:>3} '.format(" "), end='')  # print position if repeated

            print('{:15s}{:>3} {:>3} {:>3} {:>3} {:>3} {:6.2f}'.format(
                stats[sorted_teams[j]][-1],
                stats[sorted_teams[j]][4],
                stats[sorted_teams[j]][1],
                stats[sorted_teams[j]][2],
                stats[sorted_teams[j]][3],
                stats[sorted_teams[j]][2] - stats[sorted_teams[j]][3],
                stats[sorted_teams[j]][4] / (stats[sorted_teams[j]][1] * 3) * 100 if stats[sorted_teams[j]][1] > 0 else 0
            ))

P5()