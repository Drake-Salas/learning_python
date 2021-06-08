import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='required string argument')
parser.add_argument('--window', required=True, type=int,
	metavar='<int>', help='required integer argument', default = 11)
parser.add_argument('--thresh', required=True, type=float,
	metavar='<float>', help='required float number', default = 3)

arg = parser.parse_args()

file = arg.file
w = arg.window
thr = arg.thresh

for name, seq in mcb185.read_fasta(file):
	seq.upper()
	winseq = ''
    #create windows of sequence
	for i in range(len(seq) -w +1):
		win = seq[i:i + w]
		h = mcb185.entropy(win)
		if h < thr: winseq += seq[i].lower()
		else: winseq += seq[i]
	print(f'>{name}')
	for j in range(0,len(winseq), 80): print(winseq[j:j + 80]) 		
#print(f'>{name} {winseq}')
# for loop where it skips by 80
	
		
		#calculate entropy of window
		#ask if below threshhold
		#lowercase it
"""
    for letter in seq[0: len(seq) - w]:
        dictionary1 = {}
        for i in seq[letter:letter + w]:
            if letter in dictionary1: dictionary1[letter] += 1
            else: dictionary1[letter] = 1
            winseq.append(letter)
        probs = []
        for key in dictionary1:
            probs.append((dictionary1[key] / w))
#dictionary[val] or just val? or neither?
        print(probs)
        for prob in probs:
            h = prob * (math.log2(prob))
            totalentropy += h
        if totalentropy < thr:
            winseq.lower
"""


