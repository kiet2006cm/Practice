t=int(input())
for hii in range(0,t):
	n=int(input())
	s=0
	for i in range(1,n+1):
		s = s + (1/i)
	print(round(s,5))
