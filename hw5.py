import sys
from network import Graph, Edge, Node

__author__ = 'Travis Dean'
debug = False

def makeGraph(requests, classes, numclasses):
    g = Graph()
    s = Node("S")
    t = Node("T")
    g.source = s
    g.terminus = t
    students = {}
    courses = {}
    for coursename in classes.keys():
        courses[coursename] = Node(coursename)
        g.connect(courses[coursename], t, classes[coursename])
    for name in requests.keys():
        studentnode = Node(name)
        students[name] = studentnode
        g.connect(s, studentnode, numclasses)
        for coursename in requests[name]:
            g.connect(studentnode, courses[coursename], 1)

    g.maxFlow(s, t)
    return g

def solve(requests, classes, numclasses):
    g = makeGraph(requests, classes, numclasses)
    return g.outflowSource()

def read_data(filename):
    with open(filename) as f:
        while True:
            registrations, courses, numclasses = [int(x) for x in f.readline().split()]
            if registrations is 0 and courses is 0 and numclasses is 0: return
            requests = {}
            for _ in range(registrations):
                student, course = f.readline().split()
                if requests.get(student):
                    requests[student].append(course)
                else:
                    requests[student] = [course]
            classes = {}
            for _ in range(courses):
                course, capacity = f.readline().split()
                classes[course] = int(capacity)

            print("Yes") if solve(requests, classes, numclasses) else print("No")

            f.readline()    # Remove blank line

if __name__ == "__main__":
    if not debug:
        try:
            read_data(sys.argv[1])
        except Exception as e:
            print('Invalid input: ' + str(e))
    else:
        read_data("input.txt")
