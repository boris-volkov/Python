import sys
if __name__ == '__main__':
    with open('logfile.txt', 'a+') as fl:
        s = ' '.join(sys.argv[1:])
        print(s, file=fl)
