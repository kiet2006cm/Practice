t=int(input())
for i in range(0,t):
	tong=0
	n=int(input())
	for d in range(1,n+1):
		if n%d == 0:
			tong = tong+d
	print(tong)
