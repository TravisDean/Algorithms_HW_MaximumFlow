import functools
import sys
import numpy as np

__author__ = 'Travis Dean'
debug = True

def solve(requests, classes):

    return True

def read_data(filename):
    with open(filename) as f:
        registrations, courses, numclasses = [int(x) for x in f.readline().split()]
        if (registrations is 0 and courses is 0 and numclasses is 0): return
        requests = {}
        for _ in range(registrations):
            student, course = f.readline().split()
            if (requests.get(student)):
                requests[student].append(course)
            else:
                requests[student] = [course]
        classes = {}
        for _ in range(courses):
            course, capacity = f.readline().split()
            classes[course] = capacity

        print("Yes") if solve(requests, classes) else print("No")

        f.readline()    # Remove blank line

if __name__ == "__main__":
    if not debug:
        try:
            read_data(sys.argv[1])
        except Exception as e:
            print('Invalid input: ' + str(e))
    else:
        read_data("input.txt")
