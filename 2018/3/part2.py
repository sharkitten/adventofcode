#!/usr/bin/env python3

import re
import collections

a = [x for x in open("input.txt","r")]

s = collections.defaultdict(int)
pattern = re.compile('#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')

for line in a:
    m = pattern.match(line)
    i = j = 0
    for i in range(0,int(m.group(4))):
        for j in range(0,int(m.group(5))):
            if s[(int(m.group(2))+i,int(m.group(3))+j)]>0:
                overlap = True
            s[(int(m.group(2))+i,int(m.group(3))+j)]+=1

for line in a:
    m = pattern.match(line)
    i = j = 0
    overlap = False
    for i in range(0,int(m.group(4))):
        for j in range(0,int(m.group(5))):
            if s[(int(m.group(2))+i,int(m.group(3))+j)]>1:
                overlap = True
    if not overlap:
        print(m.group(1))
