#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for c in range(len(dna)):
    print (dna[c], end = "")
    if (c - 2) % 3 == 0: print ("")

    
    
    
    
        
            
    
   

"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
