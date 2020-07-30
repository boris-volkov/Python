from trainer import Player, Problem
import sys
import pickle

if __name__ == '__main__':
    student = sys.argv[1] + '.dat'
    with open(student, 'rb') as record:
        student = pickle.load(record)
    repr(student)
