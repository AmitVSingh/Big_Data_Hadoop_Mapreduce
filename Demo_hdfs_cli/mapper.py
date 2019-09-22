
from __future__ import print_function
import os
import sys
import re



for line in sys.stdin:
    article_id, content = line.split("\t", 1)
    words = re.findall("\w+", content)
    for index, word in enumerate(words):
        print(word, 1, sep = "\t")
        print("reporter:finalstatus:processed {} words"
             .format(index+1), file=sys.stderr)
