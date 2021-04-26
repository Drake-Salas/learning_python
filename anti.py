#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
rcdna = ""
for i in range(len(dna) -1, -1, -1):
    if dna[i] == 'A': nt = 'T'
    elif dna[i] == 'T': nt = 'A'
    elif dna[i] == 'G': nt = 'C'
    elif dna[i] == 'C': nt = 'G'
    rcdna += nt
print(rcdna)
"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
