#!/usr/bin/env python3

a = [[x.count(l) for l in set(x)] for x in open("input.txt","r")]
print(sum([1 for b in a if 3 in b]) * sum([1 for b in a if 2 in b]))
