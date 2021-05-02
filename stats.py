#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math
val = []
for x in sys.argv[1:]:
    val.append(float(x))

mi = val[0]
ma = val[0]
for x in val:
    if x < mi: mi = x
    if x > ma: ma = x
print(mi, ma)

val.sort()
print(val, val[0], val[-1])
mid = len(val) // 2
if len(val) % 2 == 1: med = val[mid]
else: med = (val[mid - 1] + val[mid]) / 2
print(med)


su = 0.0
for v in val:
    su += v
mean = su / len(val)
print(mean)

std = 0
for s in val:
    std += (s / mean)
print(std)
"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
