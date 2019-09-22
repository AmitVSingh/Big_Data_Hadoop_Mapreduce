
# Your code for mapper here.

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

def read_vocab(file_path):
    return set(word.strip() for word in open(file_path))

vocab = read_vocab('/datasets/stop_words_en.txt')

for line in sys.stdin:
        article_id, content = line.split('\t', 1)
        words = re.split("\W+", content)
        for word in words:
            if word in vocab:
                print "%d\t%s" %(word, 1)
