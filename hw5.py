import functools
import sys
import numpy as np

__author__ = 'Travis Dean'
debug = True

def read_data(filename):
    with open(filename) as f:
        cases = []
        registrations, courses, numclasses = f.readline().split()
        for _ in range(int(registrations)):
            student, course = f.readline().split()
            pass


if __name__ == "__main__":
    if not debug:
        try:
            read_data(sys.argv[1])
        except Exception as e:
            print('Invalid input: ' + str(e))
    else:
        read_data("input.txt")
