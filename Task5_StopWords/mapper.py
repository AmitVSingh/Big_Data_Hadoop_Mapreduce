

import sys
import re


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

path = 'stop_words_en.txt'

# Your code for reading stop words here
def read_vocab(file_path):
    return set(word.strip() for word in open(file_path))

vocab = read_vocab(path)


for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue

    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)

    # Your code for mapper here.
    for word in words:
        if word in vocab:
            print >> sys.stderr, "reporter:counter:Wiki stats,Stop words,%d" % 1
            print "%s\t%d" % (word.lower(), 1)
        
            print >> sys.stderr, "reporter:counter:Wiki stats,Total words,%d" % 1
            print "%s\t%d" % (word.lower(), 1)
        
        else:
            print >> sys.stderr, "reporter:counter:Wiki stats,Total words,%d" % 1
            print "%s\t%d" % (word.lower(), 1)

            
        
        