while True:
	A=[int(x) for x in input().split()]
	B=[]

	for i in range(0,len(A)):
		b=0
		if A[i] ==1:
			continue
		if A[i] == 2:
			B.append(A[i])
			continue
		for d in range(2,A[i]):
			if A[i]%d==0:
				b=b+1
		if b == 0:
			B.append(A[i])
	s = set(B)
	B = list(s)
	for i in range(0,len(B)):
		print(B[i],end=' ')
	print()

