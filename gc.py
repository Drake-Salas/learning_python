#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gcc = 0
for i in range(len(dna)):
    if dna[i] == 'G' or dna[i] == 'C': gcc += 1
gcd = gcc / len(dna)
print(f'{gcd:.2f}')
print('{:.2}'.format(gcd))
print('%.2f' % (gcd))
"""
python3 gc.py
0.42
0.42
0.42
"""
