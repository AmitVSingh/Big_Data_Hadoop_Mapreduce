import sys
import re

def bar():
    with open('stderr_logs.txt') as f:
        for line in f:
            if sys.argv[1] in line:
                line = line.split("=")[1]
                print(line)
        
if __name__ == '__main__':
    bar()