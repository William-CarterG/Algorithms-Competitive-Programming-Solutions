import sys
import io

#Problem 6
txt = """UBQTS TXT
tthumb
LIVESPACE BLOGJAM
philton
aeinstein
YOUBOOK
j97lee
sswxyzy
j97lee
j97lee
aeinstein
SKINUX
1
0"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin

def P6():
    while True:
        projects = {}   # To keep track of projects
        students = set()    # To keep track of students
        banned_students = set() # For students that already signed up for a project
        for line in stdin.readlines():
            line = line.strip()
            if line == "0":
                #End condition
                return
            
            elif line == "1":
                #Test case ends
                break
            
            #If the line is not "0" or "1", it must be a project name or a student
            #If the line is all uppercase letters, it is a project name
            if line.isupper():
                project = line

                #Only save up to 100 projects from same university
                if len(projects.keys()) < 100:
                    projects[project] = set()   # Empty set to store the students who sign up for this project

            #If the line starts with a letter, it is a valid student
            elif line[0].isalpha():
                student = line            
                #There are not more than 1000 students in the same university
                if len(students) < 1000:
                    students.add(student)   
                    if student not in projects[project]:             
                        if student in banned_students:
                            #If he signed up for a project already, delete him from all projects
                            for key in projects.keys():
                                if student in projects[key]:
                                    projects[key].remove(student)
                        else:
                            #Add the student to the set of students who signed up for this project
                            projects[project].add(student)
                            banned_students.add(student)
            
            else:
                #INPUT ERROR
                #It is not specified what to do with it, so I'll just ignore it.
                pass
        
        #Create a list of tuples containing each project and the number of students who signed up, and then sorting it
        signups = [(project, len(projects[project])) for project in projects]
        signups.sort(key=lambda x: (-x[1], x[0]))
        
        for project, count in signups:
            print(f"{project} {count}")

P6()