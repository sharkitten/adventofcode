#!/usr/bin/env python3

seen = set([0])
cur = i = 0

changes = [int(x) for x in open("input.txt","r")]
l = len(changes)
while True:
    cur += changes[i%l]
    i += 1
    if cur in seen:
        print(cur); break
    seen.add(cur)
