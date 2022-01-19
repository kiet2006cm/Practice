import math as m
t=int(input())
for i in range(0,t):
	n=int(input())
	s=0
	for i in range(0,n):
		s= m.sqrt(s+2)
	print(round(s,5))
