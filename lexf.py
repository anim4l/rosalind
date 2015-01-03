#!/usr/bin/python
import math
import itertools

def pe(s,n):
	alpha = list(s.split(" "))
	copy = alpha[:]
	for p in itertools.product(copy, repeat=n):
		print "".join(p)
	
s = "D W B S V F T Z X"
n = 3
pe(s, n)