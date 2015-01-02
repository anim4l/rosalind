#!/usr/bin/python
realDataSet = "CGTTCAATAACCACAGCGAAGTAGCTACAATTATTCTCGTGTCATCAGTTCTCACGGAGTGACTTGCGATTATGGGCCACTGCCTACTCAGAGTAAATGTTGTTTGGCAGCACCTAACATCCGGGAATGCTACAGTCCCGACTCTGCACAGTCTGCCGGAGTTTGACGGGTCCCACACAAATGATTCAAAACTGCATAATTACGGCAGGCCGCGGCCGATCGCTATGGAGTTAGTGATTCACGACTGCTGACCCTTTTACCTCTGAAGGGTAGGCGTCCCAGTGCGTACGGGCCGAAATGGTCTGACGGTAGTTAGGTTAGTTACAGTACCCCCGTCCTTGCGATAAGATCCAGAGCGAAGTCCGGGGATTAACAAGATCCTATCCGTAGCTTTCTTTTCTAACAGTTCCCTGCTTGAGCCTAAGACAGCGTTGTGCCTGAATAGAGCAAAATGGTCGGAGCGCATATTTAGTACCGGCAAGAGGACTAGCGGCTGAATCTATCTATAATCGCGAGACGTTGTAGTCAAATCGCTCACCTATCCAGTCGAACGTGCTACGGAACGAGAGTAATTGAACCGCTCCTGCCCAACTGGTCGCAATGACCTTTCGGCATCTTATGCTCAAGTGCAACGCAAAATCAATTAGGCACGCATATGGTGGCGAGTGAGTGATTCTTAGTATTGCCTAGCCGTTGGATACGTAACGATAGCATTACCAGTATGCGGTGGAAGAACAATCTGCCTATTATTGGAAAGGCCTGTAGTGCCTAATACCCTGTCGATAATTAACATCTAGACGCTTAGTACTTACTCATAAATGTGTGACCGACGCTAATAT"



def dataSetSize(rawData):
	a = c= g = t = 0
	for x in range(len(rawData)):
		molecule = rawData[x]
		if molecule == "A":
			a += 1
		elif molecule == "C":
			c +=1
		elif molecule == "G":
			g +=1
		else:
			t +=1
	print `a` +" " + `c` +" " +`g` +" " +`t`

dataSetSize(realDataSet)