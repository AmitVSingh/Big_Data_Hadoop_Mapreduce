
#! /usr/bin/env python

import sys

# Your functions may be here.
def bar():
    with open('stderr_logs.txt') as f:
        for line in f:
            if sys.argv[1] in line:
                stop_words = line.split("=")[1]
                stop_words = int(stop_words)
            if sys.argv[2] in line:
                total_words = line.split("=")[1]
                total_words = int(total_words)
                ratio = stop_words/total_words
                print(ratio*100)
        
if __name__ == '__main__':
    bar()