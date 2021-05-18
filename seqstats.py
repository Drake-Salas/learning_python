#!/usr/bin/env python3

import argparse
import mcb185
import statistics
# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Make useful functions and add them to your library

parser = argparse.ArgumentParser(description='Provides sequence data on  fasta file')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='required fasta file')
arg = parser.parse_args()

lengths = []
for name, seq in mcb185.read_fasta(arg.file):
    lengths.append(len(seq))

lengths.sort()
print(f'number of sequences is {len(lengths)}')

sum1 = 0
for leng in lengths:
    sum1 += leng

print(f'total sequence length is {sum1}')

print(f'min is {lengths[0]}, max is {lengths[-1]}')

print(f'mean length is {sum1/(len(lengths))}')

print(f'median length is {statistics.median(lengths)}')

#n50
sum2 = 0
for leng in lengths:
    sum2 += leng
    if sum2 > (sum1/2):
        print(f'n50 is {leng}')
        break
    
    


