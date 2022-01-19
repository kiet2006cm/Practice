t=int(input())
for i in range(0,t):
	tong=0
	# A=[int(x) for x  in input()]
	# for i in range(0,len(A)):
	# 	tong = tong + A[i]
	
	n=int(input())
	while n!=0:
		tong=tong+n%10
		n=n//10
		
	print(tong)