#!/usr/bin/env python3

i = 1

s = [x.strip() for x in open("input.txt","r")]
for x in s:
    for y in s[i:]:
        if sum(1 for a, b in zip(x, y) if a != b) == 1:
            print(''.join([a for a,b in zip(x, y) if a == b]))
    i+=1
