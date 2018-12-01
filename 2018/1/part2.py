#!/usr/bin/env python3

frequencies = [0]
i = 0

changes = [int(x.strip()) for x in open("input.txt","r")]
while len(set(frequencies)) == len(frequencies):
    frequencies.append(frequencies[-1] + changes[i%len(changes)])
    i+=1
print(frequencies[-1])
