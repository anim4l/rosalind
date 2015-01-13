#!/usr/bin/python
from decimal import *
import os.path

def getGC_Content(dna):
	a = 0.0
	# print dna.count("C")
	# print dna.count("G")
	# print len(dna)
	getcontext().prec = 8
	a = Decimal(dna.count("C")+dna.count("G"))/Decimal(len(dna))
	return a*100

def readFASTAFile(filename):
	f = open(filename)
	content = []
	dna = ""
	id = ""
	for line in f:
		if line.startswith(">"):
			if id != "" and dna!= "":
				content.append({'id':id,'dna':dna, 'gc':getGC_Content(dna)})	
			id = line[1:].replace("\n","")
			dna = ""
		else:
			dna = dna + line.replace("\n","")
	# Last line
	content.append({'id':id,'dna':dna, 'gc':getGC_Content(dna)})	
	f.close()
	return content

c = readFASTAFile("gc-data.fas")
s = sorted(c, key=lambda code: code['gc']) 

print c
print s[-1]["id"]
print s[-1]["gc"]
