#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random
size = int(sys.argv[1])
rn = int(sys.argv[2])
rl = int(sys.argv[3])

genome = [0] * size
count = 0
for i in range(rn):
    begin = random.randint(0, size - rl)
    end = begin + rl
    for l in range(begin, end):
        genome[l] += 1
mi = genome[rl]
ma = genome[rl]
tot = 0
for t in genome[rl: size - rl]:
    if t < mi: mi = genome[t]
    if t > ma: ma = genome[t]
    tot += t


print(mi, ma, tot / (size -(2 * rl)))




"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
