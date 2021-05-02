#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys
p = []
for i in sys.argv[1:]:
    p.append(float(i))
H = 0
for j in range(len(p)):
    v = p[j] * math.log2(p[j])
    H -= v
print(H)

"""
python3 entropy.py 0.1 0.2 0.3 0.4
1.846
"""
