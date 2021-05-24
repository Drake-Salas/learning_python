#!/usr/bin/env python3

import argparse
import mcb185
import matplotlib

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

parser = argparse.ArgumentParser(description='Brief description of program.')
# required arguments
parser.add_argument('--size', required=False, type=int,
	metavar='<str>', help='required string argument')
parser.add_argument('--orfmin', required=False, type=int,
	metavar='<int>', help='required integer argument')
parser.add_argument('--GC', required=False, type=float,
	metavar='<float>', help='required floating point argument')
parser.add_argument('--info', action='store_true',
	help='give info')
parser.add_argument('--seed', action='store_true',
	help='give seed number')
arg = parser.parse_args()

seq = mcb185.randseq(arg.size, arg.GC)






lengths = []
for i in range(len(seq) - 2):
    start = None
    stop = None
    if seq[i:i + 3] == 'ATG':
        start = i
        for j in range(i, len(seq) - 2, 3):
            codon = seq[j:j + 3]
            if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
                stop = j
                break
    if stop != None: lengths.append((stop - start) // 3)

#create histogram
binsize = 10

hist = [0] * ((max(lengths) // binsize) + 1)
for n in lengths: hist[n // binsize] += 1

for i in range(len(hist)): print(i * binsize, hist[i])
count = 0
for n in lengths:
    if n >= arg.orfmin: count += 1
print(count)
    
#matplotlib.hist(lengths, range(0, 10000, 20), bins = 20, color = 'purple', edgecolor = 'black')

