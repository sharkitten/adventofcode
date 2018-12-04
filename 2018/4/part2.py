#!/usr/bin/env python3
import collections
from datetime import datetime

sleep = collections.defaultdict(lambda: [0] * 60)

a = [x.strip() for x in open("input.txt","r")]
a = sorted(a,key=lambda x: datetime.strptime(x[:18], '[%Y-%m-%d %H:%M]'))
i = 0

while i < len(a):
    b = a[i].split(" ")
    if len(b) == 6:
        no = int(b[3][1:])
    elif b[-1] == "asleep":
        start = int(b[1][3:5])
    else:
        end = int(b[1][3:5])
        sleep[no] = [sum(x) for x in zip(sleep[no], [0 if x <= start or x > end else 1 for x in range(0,60)])]
    i+=1

k = list(sleep.keys())
n = [max(sleep[m]) for m in k].index(max([max(sleep[m]) for m in k]))
j = sleep[k[n]].index(max([max(sleep[m]) for m in k]))
print((j-1)*k[n])
