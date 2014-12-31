#!/usr/bin/python

def fib(n,k):
	a = 0
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1,k) + fib(n-2,k)*k

b = fib(36,4)
print b