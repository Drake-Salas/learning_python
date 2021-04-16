#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations
import math
n = 5
l = n * 3
x = 0
s = 1
for i in range(1, 6):
    s *= i
    x += i
    
print (n, l, s, x)


"""
python3 sumfac.py
5 15 120
"""
