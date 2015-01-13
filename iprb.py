from decimal import *

def iprb(k,m,n):

	# getcontext().prec = 5
	# ex1Total = k+m+n
	# BB_Bb = k/ex1Total * m/(ex1Total-1) + m/ex1Total * k/(ex1Total-1)
	# BB_BB = k/ex1Total * (k-1)/(ex1Total-1)
	# Bb_Bb = (m/ex1Total * (m-1)/(ex1Total-1))*3/4
	# BB_bb = k/ex1Total * n/(ex1Total-1) + n/ex1Total * k/(ex1Total-1)
	# Bb_bb = (m/ex1Total * n/(ex1Total-1) + n/ex1Total * m/(ex1Total-1))*0.5
	# return Decimal(BB_Bb) + Decimal(BB_BB) + Decimal(Bb_Bb) + Decimal(BB_bb) + Decimal(Bb_bb)

	population = [(1., k), (0.5, m), (0., n)]
	combinations = [(a, b) for a in population for b in population]	
	t = (k + m + n)
	return sum([(x + y - (x*y)) * (a * (b if x!=y else b-1))/(t*(t-1)) for (x,a), (y,b) in combinations])

print ('%.5f' % iprb(16,28,30))
# print ('%.5f' % iprb(2,2,2))

