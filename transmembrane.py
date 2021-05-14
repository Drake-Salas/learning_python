#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

hedrs = []

proteins = []

def contains_proline(sequence):
    for aa in sequence:
        if aa == 'P': return True
    return False

def ha(sequence, w, t):
    for i in range(len(sequence) - w):
        count = 0
        window = sequence[i:i + w]
        for f in window:
            if f == 'L': count += 3.8
            elif f == 'I': count += 4.5
            elif f == 'V': count += 4.2
            elif f == 'F': count += 2.8
            elif f == 'M': count += 1.9
            elif f == 'C': count += 2.5
            elif f == 'A': count += 1.8
            elif f == 'T': count -= 0.7
            elif f == 'G': count -= 0.4
            elif f == 'N': count -= 3.5
            elif f == 'Q': count -= 3.5
            elif f == 'D': count -= 3.5
            elif f == 'R': count -= 4.5
            elif f == 'E': count -= 3.5
            elif f == 'K': count -= 3.5
            elif f == 'P': count -= 1.6
            elif f == 'S': count -= 0.8
            elif f == 'W': count -= 0.9
            elif f == 'Y': count -= 1.3
            elif f == 'H': count -= 3.2
        if count / w > t and not contains_proline(window): return True
    return False


with open(sys.argv[1]) as fp:
    seq = []
    for line in fp.readlines():
        line = line.rstrip()
        if line.startswith('>'):
            words = line.split()
            hedrs.append(words[0][1:])
            if len(seq) > 0: proteins.append(''.join(seq))
            seq = []
        else:
            seq.append(line)
    proteins.append(''.join(seq))
    
for id, seq in zip(hedrs, proteins):
    nterm = seq[:30]
    cterm = seq[30:]
    if ha(nterm, 8, 2.5) and ha(cterm, 11, 2.0): print(id)

"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
