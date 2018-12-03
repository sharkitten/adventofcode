#!/usr/bin/env python3

import re
import collections

a = [x for x in open("input.txt","r")]
s = collections.defaultdict(int)
pattern = re.compile('(\d+),(\d+):\s(\d+)x(\d+)')

for line in a:
    m = pattern.search(line)
    i = j = 0

    for i in range(0,int(m.group(3))):
        for j in range(0,int(m.group(4))):
            s[(int(m.group(1))+i,int(m.group(2))+j)]+=1

print(len(list(filter(lambda x: x > 1, s.values()))))
