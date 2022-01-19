t=int(input())
for i in range(0,t):
	tong=1
	fuck=1
	n=int(input())
	for d in range(2,n+1):
		fuck=fuck+d
		tong = tong + (1/fuck) 
	print(round(tong,8))