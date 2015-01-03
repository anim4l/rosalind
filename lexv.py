#!/usr/bin/python
import math
import itertools

def lexv(s,n):
	alpha = list(s.split(" "))
	copy = list()
	for i in (range(0, n)):
		for p in itertools.product(alpha, repeat=n-i):
			copy.append("".join(p))
	ooo = sorted(copy, key=lambda word: [alpha.index(c) for c in word])
	for o in ooo:
		print o

s = "Y T O W Q X G U E N K"
n = 4
lexv(s, n)