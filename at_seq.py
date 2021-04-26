#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence
bp = 30
print(bp)
atc = 0
seq = ""
for i in range(bp):
    r = random.random()
    if r < 0.3:
        nt = 'A'
        atc = atc + 1
    if 0.3 < r and r < 0.6:
        nt = 'T'
        atc = atc + 1
    if 0.6 < r and r < 0.8: nt = 'G'
    if r < 1 and r > 0.8: nt = 'C'
    frac = atc / bp
    seq = seq + nt
print(frac)
print(seq)

"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
